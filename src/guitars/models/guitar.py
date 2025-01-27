from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.db import Base


class Guitar(Base):
    article: Mapped[str] = mapped_column(String(20), nullable=False)
    brand_id: Mapped[int] = mapped_column(ForeignKey("brands.id"), nullable=False)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    price: Mapped[int] = mapped_column(nullable=False)
    brand: Mapped[str] = relationship("Brand", back_populates="guitars", lazy="joined")
