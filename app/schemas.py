from pydantic import BaseModel

class URLBase(BaseModel):
    original_url: str

class URLCreate(URLBase):
    pass

class URL(URLBase):
    short_code: str

    class Config:
        orm_mode = True
