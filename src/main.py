import logging
from pprint import pprint

import pandas as pd

from services.database.insert import insert_in_giveaways
from services.instagram.entities import PostInfo
logging.basicConfig(level=logging.INFO)


from configs.environment_variables import INSTA_PASSWORD, INSTA_USERNAME
from constants.get import get_random_comments, get_random_friends

from services.instagram.extractions import extract_unique_attags_from_content
from services.instagram.actions import comment_post, connect, like_post, subscribe_to_multiple_users
from services.instagram.scraping import find_giveaway_posts, get_post_info

MAX_NUMBER_OF_SUBSCIRBTIONS = 5

def main():
    logging.info("Starting bot ...")
    giveaway_posts = find_giveaway_posts(None)
    print(giveaway_posts)
    # giveaway_posts = ['Ck06aNFKeYB', 'Ck1DUQgKASA', 'Ck3DyqWtlgh', 'Ck1AoCJMnPy', 'Ck1AA0PKCQ6', 'Ck2wqEVqaee', 'CkxWCWIqAYL', 'Ck3PjaFL7IG', 'Ck0RuuKskrw', 'Ck3Tw1Xsa3r', 'Ck3TIYUqzLQ', 'Ck3Sy9_owEf', 'Ck3RzGWo6-D', 'Ck3RUgaq8up', 'Ck3RIXEIg4r', 'Ck3RBQgIUhW', 'Ck3RAstKaq3', 'Ck3Q-paqn_E', 'Ck3Q6I7K-sO', 'Ck3Qv-nKg_2', 'Ck3QumDo_KD', 'Ck3QpMwoMmy', 'Ck3QnZsqzTM', 'Ck3Qk5GOnS2', 'Ck3QO-ZIpDh', 'Ck3QOONtpKP', 'Ck3QLMGLAAy', 'Ck3QBxMIbO3', 'Ck3Pr39Kzr5', 'Ck3Pj3hjBXu', 'Ck3OuguAJuE', 'Ck3PX4kKeEo', 'Ck3PRy8q6to']
    # giveaway_posts = giveaway_posts[16:20]
    logging.info(f"Found {len(giveaway_posts)} giveaway posts.")
    driver = connect(INSTA_USERNAME, INSTA_PASSWORD)
    # giveaway_posts_with_infos = []
    with driver:
        for post_id in giveaway_posts:
            post_infos: PostInfo = get_post_info(driver, post_id)

            like_post(driver, post_id)
            
            comment = get_random_comments()[0]
            friends = get_random_friends()
            full_comment = comment + " ".join(friends)
            comment_post(driver, post_id, full_comment)
            
            users_to_subscribe_to = extract_unique_attags_from_content(post_infos["content"])
            subscribe_to_multiple_users(driver, users_to_subscribe_to[:MAX_NUMBER_OF_SUBSCIRBTIONS])

            del post_infos['media']
            del post_infos['content']
            print("Post infos", post_infos)
            insert_in_giveaways(pd.DataFrame([post_infos]))
    
    # insert_in_giveaways(pd.DataFrame(giveaway_posts_with_infos))


if __name__ == "__main__":
    main()
