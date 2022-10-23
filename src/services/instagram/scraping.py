import time
from typing import Any, List

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service as ChromeService

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
        time.sleep(10)
        all_giveways = "article div div div div a"
        a_elements = driver.find_elements(By.CSS_SELECTOR, all_giveways)
        for a_element in a_elements:
            href = a_element.get_attribute("href")
            print(href)
            result.append(href.replace("https://www.instagram.com/p/", "").replace("/", ""))
    
    return result


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

def get_post_content(driver: Chrome, post_url: str) -> str:
    """Gets the content of a post
        # Returns
        - A string containing the post content
    """
    driver.get(post_url)
    driver.implicitly_wait(5)
    
    content_element = driver.find_elements(By.CSS_SELECTOR, "div._a9zs")[0]
    return content_element.text