from typing import Any, List

from services.instagram.entities import PostInfo


def find_giveaway_posts(search_filters: List[Any], limit: str = 1000) -> List[str]:
    """Finds the posts that are doing a giveaway.
        # Returns
        - A list of the posts urls
    """
    pass


def get_post_info(url: str) -> PostInfo:
    """Gets the basic info for a giveway post
        # Returns
        - A dict containing information about the post at a moment T ...
    """
    pass


def get_post_comments(post_url:str, limit: str = 1000): # Maybe only the number of comments, no real use case for all content
    """Gets all the comments of a post
        # Returns
        - A list of the posts urls
    """
    pass
