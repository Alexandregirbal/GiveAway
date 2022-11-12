import logging
logging.basicConfig(level=logging.INFO)

import pandas as pd

from configs.environment_variables import INSTA_PASSWORD, INSTA_USERNAME
from participate import participate_to_giveaway
from services.database.insert import insert_in_giveaways
from services.instagram.actions import connect
from services.instagram.entities import PostInfo
from services.instagram.scraping import find_giveaway_posts

def main():
    logging.info("Starting bot ...")
    giveaway_posts = find_giveaway_posts(None)
    print(giveaway_posts)
    # giveaway_posts = ['Ck06aNFKeYB', 'Ck1DUQgKASA', 'Ck3DyqWtlgh', 'Ck1AoCJMnPy', 'Ck1AA0PKCQ6', 'Ck2wqEVqaee', 'CkxWCWIqAYL', 'Ck3PjaFL7IG', 'Ck0RuuKskrw', 'Ck3Tw1Xsa3r', 'Ck3TIYUqzLQ', 'Ck3Sy9_owEf', 'Ck3RzGWo6-D', 'Ck3RUgaq8up', 'Ck3RIXEIg4r', 'Ck3RBQgIUhW', 'Ck3RAstKaq3', 'Ck3Q-paqn_E', 'Ck3Q6I7K-sO', 'Ck3Qv-nKg_2', 'Ck3QumDo_KD', 'Ck3QpMwoMmy', 'Ck3QnZsqzTM', 'Ck3Qk5GOnS2', 'Ck3QO-ZIpDh', 'Ck3QOONtpKP', 'Ck3QLMGLAAy', 'Ck3QBxMIbO3', 'Ck3Pr39Kzr5', 'Ck3Pj3hjBXu', 'Ck3OuguAJuE', 'Ck3PX4kKeEo', 'Ck3PRy8q6to']
    # giveaway_posts = giveaway_posts[16:20]
    logging.info(f"Found {len(giveaway_posts)} giveaway posts.")
    connected_driver = connect(INSTA_USERNAME, INSTA_PASSWORD)
    # giveaway_posts_with_infos = []
    with connected_driver:
        for post_id in giveaway_posts:
            post_infos: PostInfo = participate_to_giveaway(
                connected_driver,
                post_id
            )

            del post_infos['media']
            del post_infos['content']
            print("Post infos", post_infos)
            insert_in_giveaways(pd.DataFrame([post_infos]))
    
    # insert_in_giveaways(pd.DataFrame(giveaway_posts_with_infos))


if __name__ == "__main__":
    main()
