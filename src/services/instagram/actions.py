from time import sleep
from typing import List

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service as ChromeService

from src.configs.selenium_options import CHROMEDRIVER_PATH
import src.configs.environment_variables as env

def connect(username: str, password: str) -> Chrome:
    """Connects to Instagram with user credentials"""
    driver = Chrome(service= ChromeService(CHROMEDRIVER_PATH))
    with driver:
        driver.get("https://www.instagram.com/")
        driver.implicitly_wait(5)
        
        # Accept cookies
        try:
            driver.find_element(By.XPATH, "//button[text()='Only allow essential cookies']").click()
        except NoSuchElementException:
            pass
        
        driver.find_element(By.CSS_SELECTOR, "input[name='username']").send_keys(username)
        driver.find_element(By.CSS_SELECTOR, "input[name='password']").send_keys(password)
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        sleep(10)



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


if __name__ == '__main__':
    connect(env.INSTA_USERNAME, env.INSTA_PASSWORD)