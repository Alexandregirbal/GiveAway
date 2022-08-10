from typing import List


def like_post(post_url:str) -> None:
    """Likes a post with its url.
        # Returns
        - None if everything went well
    """
    pass


def comment_post(post_url:str, comment: str) -> None:
    """Comments a post with its url.
        # Returns
        - None if everything went well
    """
    pass


def share_post_in_story(post_url: str) -> None:
    """Comments a post with its url.
        # Returns
        - None if everything went well
    """
    pass


def subscribe_to_user(user: str) -> None:
    """Subscribes to a user with its uuid."""
    pass


def subscribe_to_multiple_users(users: List[str]) -> None:
    for user in users:
        subscribe_to_user(user)
