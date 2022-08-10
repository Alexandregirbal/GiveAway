from typing import TypedDict


class PostInfo(TypedDict):
    author: str # uuid
    media: str # url
    media_tags: str
    content: str
    likes: int