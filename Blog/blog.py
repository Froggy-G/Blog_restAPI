from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from Core.utils import get_db

router = APIRouter()


@router.get("/")
def blogs_list(db: Session = Depends(get_db)):                            
    print(db)
    return {}