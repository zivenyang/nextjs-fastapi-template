from typing import Optional
from sqlmodel import Field, SQLModel
from datetime import datetime

class ItemBase(SQLModel):
    title: str = Field(max_length=256, nullable=False)
    description: str = Field(default=None ,nullable=True)
    completed: bool = Field(default=False, nullable=False)


class Item(ItemBase, table=True):
    __tablename__ = "Items"
    id: Optional[int] = Field(default=None, primary_key=True, nullable=False)
    created_at: datetime = Field(default_factory=datetime.now)


class ItemCreate(ItemBase):
    pass