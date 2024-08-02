from fastapi import APIRouter, Depends
from sqlmodel import select

from ..database import get_session
from .models import Item, ItemCreate
from sqlmodel.ext.asyncio.session import AsyncSession

router = APIRouter(
    prefix="/items",
    tags=["items"],
    )

@router.get("/", response_model=list[Item])
async def get_items(*, session: AsyncSession = Depends(get_session)):
    result = await session.exec(select(Item))
    items = result.all()
    return items


@router.post("/", response_model=Item)
async def create_item(*,session: AsyncSession = Depends(get_session), item: ItemCreate):
    db_item = item.model_validate(item)
    session.add(db_item)
    session.commit()
    session.refresh(db_item)
    return db_item
