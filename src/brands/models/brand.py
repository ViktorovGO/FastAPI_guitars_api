from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.db import Base


class Brand(Base):
    name: Mapped[str] = mapped_column(String(20), nullable=False, unique=True)
    guitars: Mapped[list[str]] = relationship('Guitar', back_populates='brand', lazy='selectin', cascade='all, delete-orphan')


