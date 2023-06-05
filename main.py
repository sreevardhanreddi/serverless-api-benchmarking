import os
from typing import Any, List, Optional, Union

from fastapi import Depends, FastAPI, HTTPException, status
from motor.core import Database
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel, Field

app = FastAPI()


class _Id(BaseModel):
    _oid: str = Field(..., alias="$oid")


class CreatedAt(BaseModel):
    _date: str = Field(..., alias="$date")


class CompaniesSchema(BaseModel):
    _id: _Id
    name: Optional[str]
    permalink: Optional[str]
    crunchbase_url: Optional[str]
    homepage_url: Optional[str]
    blog_url: Optional[str]
    blog_feed_url: Optional[str]
    twitter_username: Optional[str]
    category_code: Optional[str]
    number_of_employees: Optional[int]
    founded_year: Optional[int]
    founded_month: Optional[int]
    founded_day: Optional[int]
    deadpooled_year: Optional[int]
    tag_list: Optional[str]
    alias_list: Optional[str]
    email_address: Optional[str]
    phone_number: Optional[str]
    description: Optional[str]
    created_at: Union[CreatedAt, Any]
    overview: Optional[str]


def get_db():
    db = AsyncIOMotorClient(os.getenv("MONGODB_URI"))
    try:
        yield db.sample_training
    finally:
        db.close()


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
