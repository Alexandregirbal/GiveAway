import time
from typing import Any, List

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service as ChromeService
from services.instagram.utils import get_post_url_from_id

from src.configs.selenium_options import CHROMEDRIVER_PATH
from src.services.instagram.entities import PostInfo

def find_giveaway_posts(search_filters: List[Any], limit: str = 1000) -> List[str]:
    """Finds the posts that are doing a giveaway.
        # Returns
        - A list of the posts urls
    """
    driver = Chrome(service= ChromeService(CHROMEDRIVER_PATH))
    result = []
    with driver:
        driver.get("https://www.instagram.com/explore/tags/concours/")
        driver.implicitly_wait(5)
        time.sleep(8)
        all_giveaways = "article div div div div a"
        a_elements = driver.find_elements(By.CSS_SELECTOR, all_giveaways)
        for a_element in a_elements:
            href = a_element.get_attribute("href")
            result.append(href.replace("https://www.instagram.com/p/", "").replace("/", ""))
    
    return result


def get_post_info(driver: Chrome, post_id: str) -> PostInfo:
    """Gets the basic info for a giveaway post
        # Returns
        - A dict containing information about the post ...
    """
    post_url = get_post_url_from_id(post_id)
    driver.get(post_url)
    time.sleep(5)
    
    author = driver.find_element(
        By.CSS_SELECTOR,
        "h2 > div > span > a"
    ).get_attribute("href")[:-1].replace("https://www.instagram.com/", "@")

    media = {} 
    media_elements = driver.find_elements(
        By.CSS_SELECTOR,
        "article img"
    )
    media["url"] = media_elements[0].get_attribute("srcset") # first image only
    media["alt"] = media_elements[0].get_attribute("alt") # first image only

    content = driver.find_elements( # or div._a9zs
        By.CSS_SELECTOR,
        "div > div > div > div > div > ul > div > li > div > div > div > div > span"
    )[1].text

    publish_datetime = driver.find_elements(
        By.CSS_SELECTOR,
        "div > time"
    )[1].get_attribute("datetime")
    
    return {
        "id": post_id,
        "author": author,
        "media": media,
        "content": content,
        "publish_datetime": publish_datetime,
    }


def get_post_comments(post_url:str, limit: str = 1000): # Maybe only the number of comments, no real use case for all content
    """Gets all the comments of a post
        # Returns
        - A list of the posts urls
    """
    pass
