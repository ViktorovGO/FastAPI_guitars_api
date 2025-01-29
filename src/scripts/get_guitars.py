import asyncio
import aiohttp
import json
from bs4 import BeautifulSoup

global urls, guitars
urls = []
guitars = []


SEMAPHORE_LIMIT = 50  # Ограничение на количество одновременных запросов


async def fetch(session, url, semaphore):
    """Асинхронный запрос с использованием семафоры"""
    async with semaphore:
        async with session.get(url) as response:
            return await response.text()


async def get_urls(session: aiohttp.ClientSession, semaphore, url: str) -> list[str]:
    """Получение списка ссылок на гитары"""
    resp = await fetch(session, url, semaphore)
    soup = BeautifulSoup(resp, "lxml")
    items = soup.find_all("a", {"class": "catalog-card__name"})

    for item in items:
        urls.append("https://www.muztorg.ru/" + item.get("href"))
    return urls


async def get_guitar_info(session: aiohttp.ClientSession, semaphore, url: str):
    """Получение информации о гитаре"""

    resp = await fetch(session, url, semaphore)
    soup = BeautifulSoup(resp, "lxml")
    item = soup.find("a", {"class": "mt-button _red _large"})
    if item:
        guitars.append(
            {
                "article": item.get("data-id"),
                "brand": item.get("data-brand"),
                "title": item.get("data-title"),
                "price": item.get("data-product-price"),
            }
        )


async def get_guitars():
    url = "https://www.muztorg.ru/category/akusticheskie-gitary"
    semaphore = asyncio.Semaphore(SEMAPHORE_LIMIT)
    async with aiohttp.ClientSession() as session:
        # Получение количества страниц
        resp = await fetch(session, url, semaphore)
        soup = BeautifulSoup(resp, "lxml")
        pages = int(
            soup.find("li", {"class": "pagination-container__item _last"})
            .find("a")
            .text
        )

        # Сбор ссылок на гитары
        tasks = [
            get_urls(session, semaphore, url + f"?page={i}")
            for i in range(1, pages + 1)
        ]
        await asyncio.gather(*tasks)

        # Сбор данных по гитарам
        tasks = [get_guitar_info(session, semaphore, url) for url in urls]
        await asyncio.gather(*tasks)


async def main():
    await get_guitars()

    filtered_guitars = sorted(
        [
            guitar
            for guitar in guitars
            if all(value is not None for value in guitar.values())
        ],
        key=lambda x: int(x["price"]),
    )

    with open("src/scripts/guitars.json", "w", encoding="utf-8") as file:
        json.dump(filtered_guitars, file, ensure_ascii=False, indent=4)
    return filtered_guitars


if __name__ == "__main__":
    asyncio.run(main)
