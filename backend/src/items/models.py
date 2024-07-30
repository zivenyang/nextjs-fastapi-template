from typing import Optional
from sqlmodel import Field, SQLModel
from datetime import datetime

class ItemBase(SQLModel):
    ext: str
    completed: bool


class Item(ItemBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, nullable=False)
    created_at: datetime = Field(default_factory=datetime.now)


class ItemCreate(ItemBase):
    pass