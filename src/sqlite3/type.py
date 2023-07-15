from pydantic import BaseModel

class library(BaseModel):
    book_name: str
    published_year: int
    publisher_name: str = 'Jhon'

data = {
    'book_name': 'Magic',
    'published_year': 1985,
}

lib = library(**data)

print(lib.published_year)

print(lib.model_dump())