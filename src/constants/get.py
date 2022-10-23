import json
import os
from random import shuffle
from typing import List
from src.configs.environment_variables import PROJECT_ROOT

def _load_json_file(file_path: str) -> dict:
    """Loads a json file and returns its content"""
    with open(file_path) as json_file:
        json_content = json_file.read()

    return json.loads(json_content)


def _get_friends_from_json() -> List[dict]:
    friends_file_path = os.path.join(PROJECT_ROOT, 'src', "constants", "friends.json")
    friends = _load_json_file(friends_file_path)
    return friends


def _get_comments_from_json() -> List[dict]:
    comments_file_path = os.path.join(PROJECT_ROOT, 'src', "constants", "comments.json")
    comments = _load_json_file(comments_file_path)
    return comments


def _get_comment_content(comment: dict) -> str:
    return comment.get("content")


def get_random_comments(length: int = 1, level: int = 0) -> str:
    """Gets a random comment from the comments.json file.
        Returns 1 comment by default.
    """
    comments = _get_comments_from_json()
        
    filtered_comments = list(filter(lambda comment: comment.get("level") == level, comments))
    shuffle(filtered_comments)
    
    return list(map(_get_comment_content, filtered_comments))[:length]


def get_random_friends(length: int = 2) -> str:
    """Gets a random friend from the friends.json file.
        Returns 2 friends by default.
    """
    friends = _get_friends_from_json()
    shuffle(friends)
    return friends[:length]
