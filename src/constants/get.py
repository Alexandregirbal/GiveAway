import json
import os
from random import shuffle
from typing import List
from configs.environment_variables import PROJECT_ROOT

def get_comments() -> List[dict]:
    comments_file_path = os.path.join(PROJECT_ROOT, 'src', "constants", "comments.json")

    with open(comments_file_path) as comments_file:
        comments_json = comments_file.read()

    comments = json.loads(comments_json)
    return comments

def get_random_comment(length: int = 0) -> str:
    comments = get_comments()
    shuffle(comments)
    
    if length == 0:
        return comments
    
    return comments[:length]
    