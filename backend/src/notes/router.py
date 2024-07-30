from fastapi import APIRouter, Depends
from sqlmodel import select

from ..database import get_session
from .models import Note, NoteCreate
from sqlmodel.ext.asyncio.session import AsyncSession

router = APIRouter()

@router.get("/notes/", response_model=list[Note])
async def get_notes(*, session: AsyncSession = Depends(get_session)):
    result = await session.exec(select(Note))
    notes = result.scalars().all()
    return notes


@router.post("/notes/", response_model=Note)
async def create_note(*,session: AsyncSession = Depends(get_session), note: NoteCreate):
    db_note = note.model_validate(note)
    session.add(db_note)
    session.commit()
    session.refresh(db_note)
    return db_note
