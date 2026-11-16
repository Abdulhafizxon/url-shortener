from pydantic import AnyHttpUrl, BaseModel


class LinkCreate(BaseModel):
    url: AnyHttpUrl


class LinkOut(BaseModel):
    code: str | None
    short_url: str
    original_url: str
