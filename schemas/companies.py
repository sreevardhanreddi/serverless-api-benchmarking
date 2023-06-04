from __future__ import annotations

from typing import Any, Optional, Union

from pydantic import BaseModel, Field


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
