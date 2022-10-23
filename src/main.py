import logging
logging.basicConfig(level=logging.INFO)


from configs.environment_variables import INSTA_PASSWORD, INSTA_USERNAME
from constants.get import get_random_comments, get_random_friends

from services.instagram.extractions import extract_unique_attags_from_content
from services.instagram.actions import comment_post, connect, like_post, subscribe_to_multiple_users
from services.instagram.scraping import find_giveaway_posts, get_post_content

MAX_NUMBER_OF_SUBSCIRBTIONS = 5

def main():
    logging.info("Starting bot ...")
    giveaway_posts = find_giveaway_posts(None)
    # giveaway_posts = ['CkDEZaJMpR9', 'Cj-rwM-MDnk', 'CkA-WUnqxTH', 'CkBqDOtMYDm', 'CkAOlhZqDDv', 'CkBZ3mEokIG', 'CkDJSwkKA_z', 'CkDVXfwq7qX', 'Cj-6SYNMKK6']
    logging.info(f"Found {len(giveaway_posts)} giveaway posts.")
    
    driver = connect(INSTA_USERNAME, INSTA_PASSWORD)
    with driver:
        for post_id in giveaway_posts:
            post_url = f"https://www.instagram.com/p/{post_id}/"
            like_post(driver, post_url)
            comment = get_random_comments()[0]
            friends = get_random_friends()
            full_comment = comment + " @" + " @".join(friends)
            comment_post(driver, post_url, full_comment)
            content = get_post_content(driver, post_url)
            users_to_subscribe_to = extract_unique_attags_from_content(content)
            subscribe_to_multiple_users(driver, users_to_subscribe_to[:MAX_NUMBER_OF_SUBSCIRBTIONS])
    
    # TODO: add post ids to DB
    # Setup scheduler to optimize


if __name__ == "__main__":
    main()
