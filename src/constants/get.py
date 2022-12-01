import os
from random import shuffle
from typing import List

from configs.environment_variables import PROJECT_ROOT
from utils.files import load_json_file

### CONSTANTS ###

MAX_NUMBER_OF_SUBSCIRBTIONS_PER_GIVEAWAY = 5


### FROM FILES ###

def _get_friends_from_json() -> List[dict]:
    friends_file_path = os.path.join(PROJECT_ROOT, 'src', "constants", "friends.json")
    friends = load_json_file(friends_file_path)
    return friends


def _get_comments_from_json() -> List[dict]:
    comments_file_path = os.path.join(PROJECT_ROOT, 'src', "constants", "comments.json")
    comments = load_json_file(comments_file_path)
    return comments


def _get_comment_content(comment: dict) -> str:
    return comment.get("content")


def get_random_comments(length: int = 1, level: int = -1) -> List[str]:
    """Gets a random comment from the comments.json file.
        Returns 1 comment by default.
    """
    comments = _get_comments_from_json()
    
    if level == -1:
        filtered_comments = comments
    else:
        filtered_comments = list(filter(lambda comment: comment.get("level") == level, comments))
    
    shuffle(filtered_comments)
    
    return list(map(_get_comment_content, filtered_comments))[:length]


def get_random_friends(length: int = 2) -> List[str]:
    """Gets a random friend from the friends.json file.
        Returns 2 friends by default.
    """
    friends = _get_friends_from_json()
    shuffle(friends)
    return friends[:length]
