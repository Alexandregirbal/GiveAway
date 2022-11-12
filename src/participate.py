from selenium.webdriver import Chrome

from constants.get import (
    MAX_NUMBER_OF_SUBSCIRBTIONS_PER_GIVEAWAY,
    get_random_comments, get_random_friends)
from services.instagram.actions import (
    comment_post,
    like_post,
    subscribe_to_multiple_users)
from services.instagram.entities import PostInfo
from services.instagram.extractions import extract_unique_attags_from_content
from services.instagram.scraping import get_post_info


def participate_to_giveaway(
    connected_account_driver: Chrome,
    post_id: str,
) -> PostInfo:
    post_infos: PostInfo = get_post_info(
        connected_account_driver,
        post_id
    )

    like_post(
        connected_account_driver,
        post_id
    )
    
    comment = get_random_comments()[0]
    friends = get_random_friends()
    full_comment = comment + " ".join(friends)
    comment_post(
        connected_account_driver,
        post_id, full_comment
    )
    
    users_to_subscribe_to = extract_unique_attags_from_content(
        post_infos["content"]
    )
    subscribe_to_multiple_users(
        connected_account_driver,
        users_to_subscribe_to[:MAX_NUMBER_OF_SUBSCIRBTIONS_PER_GIVEAWAY]
    )

    return post_infos