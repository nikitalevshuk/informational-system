from fastapi import APIRouter

router = APIRouter(prefix = '/books')

@router.get('/')
async def books_get():
    return {'message': 'test'}