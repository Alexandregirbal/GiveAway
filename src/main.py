import logging
logging.basicConfig(level=logging.INFO)

from configs.environment_variables import INSTA_PASSWORD, INSTA_USERNAME
from constants.get import get_random_comments, get_random_friends

from services.instagram.actions import comment_post, connect, like_post
from services.instagram.scraping import find_giveaway_posts

NUMBER_OF_COMMENTS = 1
NUMBER_OF_TAGS = 2

def main():
    logging.info("Starting bot ...")
    # giveaway_posts = find_giveaway_posts(None)
    giveaway_posts = ['https://www.instagram.com/p/CkDEZaJMpR9/', 'https://www.instagram.com/p/Cj-rwM-MDnk/', 'https://www.instagram.com/p/CkA-WUnqxTH/', 'https://www.instagram.com/p/CkBqDOtMYDm/', 'https://www.instagram.com/p/CkAOlhZqDDv/', 'https://www.instagram.com/p/CkBZ3mEokIG/', 'https://www.instagram.com/p/CkDJSwkKA_z/', 'https://www.instagram.com/p/CkDVXfwq7qX/', 'https://www.instagram.com/p/Cj-6SYNMKK6/']
    logging.info(f"Found {len(giveaway_posts)} giveaway posts.")
    
    driver = connect(INSTA_USERNAME, INSTA_PASSWORD)
    with driver:
        for post in giveaway_posts:
            like_post(driver, post)
            comment = get_random_comments()[0]
            friends = get_random_friends()
            full_comment = comment + " @" + " @".join(friends)
            comment_post(driver, post, full_comment)
            # content = get_post_content(driver, post)
            # accounts_to_subscribe = extract_unique_attags_from_content(content)
            # subscribe_to_multiple_users(driver, accounts_to_subscribe)


if __name__ == "__main__":
    main()
