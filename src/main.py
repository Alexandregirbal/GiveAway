import logging

import pandas as pd

from services.database.insert import insert_in_giveaways
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
    print(giveaway_posts)
    # giveaway_posts = ['Cki9RN7Ka84', 'Cki4HgOoZgj', 'CkjAyBjM_WZ', 'Cki_AUpK7Ve', 'Ckgn25aKYk8', 'CkiCy3VsVR1', 'CkiLe6Vo62g', 'CkgrG03MKAe', 'CkiNNgZKJY7', 'CklwKKupkA_', 'CklwFZFrj5F', 'CklvysNqjXi', 'CklvNfascJS', 'CklvL81Ngfr', 'Ckluyi6Ih_O', 'Cklur5OKlot', 'CkluqFzjLk0', 'CkluYGfqkF0', 'CkluH7ioPwZ', 'CkluDloMlhC', 'CkluAdeN6eT', 'Cklt_Vcq339', 'Cklt-cEqsEB', 'CkltkVBoZVk', 'CkltiZnq9nv', 'CkltcxdNJ79', 'CkltLNdLNsX', 'CkltA4aqDvH', 'CkltAUPMUtw', 'Ckls6Z1qJi3', 'Ckls6YdrScB', 'Ckls3G9rGsU', 'Ckls18yoITf']
    logging.info(f"Found {len(giveaway_posts)} giveaway posts.")
    
    driver = connect(INSTA_USERNAME, INSTA_PASSWORD)
    with driver:
        for post_id in giveaway_posts:
            post_url = f"https://www.instagram.com/p/{post_id}/"
            like_post(driver, post_url)
            comment = get_random_comments()[0]
            friends = get_random_friends()
            full_comment = comment + " ".join(friends)
            comment_post(driver, post_url, full_comment)
            content = get_post_content(driver, post_url)
            users_to_subscribe_to = extract_unique_attags_from_content(content)
            subscribe_to_multiple_users(driver, users_to_subscribe_to[:MAX_NUMBER_OF_SUBSCIRBTIONS])
    
    insert_in_giveaways(pd.DataFrame(
        [{"id": post_id} for post_id in giveaway_posts]
    ))


if __name__ == "__main__":
    main()
