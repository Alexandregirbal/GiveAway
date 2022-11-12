from datetime import datetime
from typing import TypedDict


class Media(TypedDict):
    url: str
    alt: str
class PostInfo(TypedDict):
    id: str # uuid
    author: str # uuid
    media: Media # many urls for different formats
    content: str # post content
    publish_datetime: datetime # last edit datetime