import logging
logging.basicConfig(level=logging.DEBUG)

from configs.environment_variables import INSTA_PASSWORD, INSTA_USERNAME
from constants.get import get_random_comment

from services.instagram.actions import comment_post, connect, like_post
from services.instagram.scraping import find_giveaway_posts

NUMBER_OF_COMMENTS = 1
NUMBER_OF_TAGS = 2

def main():
    logging.info("Starting bot ...")
    giveaway_posts = find_giveaway_posts(None)
    logging.info(f"Found {len(giveaway_posts)} giveaway posts.")
    logging.debug(f"Giveaway posts:\n{giveaway_posts}")

    # driver = connect(INSTA_USERNAME, INSTA_PASSWORD)
    # for post in giveaway_posts:
    #     like_post(post)
    #     comments = get_random_comment(NUMBER_OF_COMMENTS)
    #     for comment in comments:
    #         comment_post(post, comment)
    
if __name__ == "__main__":
    main()
