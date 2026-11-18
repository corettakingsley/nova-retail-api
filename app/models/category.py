
from sqlalchemy import Column, Integer, String, Text
from app.database import Base
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)
    description = Column(Text, nullable=True)
    products = relationship("Product", back_populates="category")
