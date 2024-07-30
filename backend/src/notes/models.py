from typing import Optional
from sqlmodel import Field, SQLModel
from datetime import datetime

class NoteBase(SQLModel):
    ext: str
    completed: bool


class Note(NoteBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, nullable=False)
    created_at: datetime = Field(default_factory=datetime.now)

class NoteCreate(NoteBase):
    pass