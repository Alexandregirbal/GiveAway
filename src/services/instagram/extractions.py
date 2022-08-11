import datetime
import re
from typing import List, Tuple
from dateparser.search import search_dates

def extract_unique_attags_from_content(content: str) -> List[str]:
    """Extracts all the people ids tagged in a post content.
        # Arguments
        - `content`: The content of the post
        
        # Returns
        - A list of the people id tagged.
        
        # Example
        >>> extract_unique_attags_from_content("Picture from @instagram_user_1, thanks @instagram_user_2 for participating, thanks again @instagram_user_1.")
        # Returns: ['instagram_user_1', 'instagram_user_2']
    """
    regex = r"@[a-zA-Z0-9_]+"
    return list(set(re.findall(regex, content)))


def extract_unique_hashtags_from_content(content: str) -> List[str]:
    """Extracts all the hashtags in a post content.
        # Arguments
        - `content`: The content of the post

        # Returns
        - A list of the hashtags
        
        # Example
        >>> extract_unique_hashtags_from_content("Picture from @instagram_user_1. #l4l #IamaHashTag #Tropbeau")
        # Returns: ['#l4l', '#IamaHashTag', '#Tropbeau']
    """
    regex = r"#[a-zA-Z0-9_]+"
    return list(set(re.findall(regex, content)))


def extract_unique_dates_from_content(content: str) -> List[Tuple[str, datetime.datetime]]:
    """Extracts all the dates in a post content. Implicitely adds the current year if not provided.
        # Arguments
        - `content`: The content of the post

        # Returns
        - A list of the dates
        
        # Example
        >>> extract_unique_dates_from_content("Picture from @instagram_user_1. taken the 22nd of July, see you on the 1st of September 2022 #l4l")
        # Returns: ['2022-07-22', '2022-09-01']
    """
    return search_dates(content)
    

if __name__ == "__main__":
    res = extract_unique_dates_from_content("Picture from @instagram_user_1. taken the 22nd of July, see you on the 2nd of September")
    print(res)
