from fastapi import APIRouter
import src.items.urls as item_urls
root_router = APIRouter()
root_router.include_router( item_urls.router)

