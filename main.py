from typing import List

from fastapi import Depends, FastAPI, HTTPException, status
from motor.core import Database

from database.connection import get_db
from schemas.companies import CompaniesSchema

app = FastAPI()


@app.get("/records", response_model=List[CompaniesSchema])
async def get_records(db: Database = Depends(get_db)):
    try:
        return await db.get_collection("companies").find(limit=100).to_list(length=100)
    except Exception as e:
        print(e)
        return HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Something went wrong",
        )
