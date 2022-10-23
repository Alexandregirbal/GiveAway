import json
import os
from random import shuffle
from typing import List
from src.configs.environment_variables import PROJECT_ROOT

def get_comments() -> List[dict]:
    comments_file_path = os.path.join(PROJECT_ROOT, 'src', "constants", "comments.json")

    with open(comments_file_path) as comments_file:
        comments_json = comments_file.read()

    comments = json.loads(comments_json)
    return comments


def _get_comment_content(comment: dict) -> str:
    return comment.get("content")


def get_random_comment(length: int = -1, level: int = 0) -> str:
    comments = get_comments()
        
    filtered_comments = list(filter(lambda comment: comment.get("level") == level, comments))
    shuffle(filtered_comments)
    
    if length == -1:
        length = len(filtered_comments)
    
    return list(map(_get_comment_content, filtered_comments))[:length]
