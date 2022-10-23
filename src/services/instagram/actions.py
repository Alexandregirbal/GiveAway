from time import sleep
import time
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
    return driver


def like_post(driver: Chrome, post_url:str) -> None:
    """Likes a post with its url.
        # Returns
        - None if everything went well
    """
    driver.get(post_url)
    driver.implicitly_wait(5)
    driver.find_element(By.CSS_SELECTOR, "span > svg[aria-label='Like']").click()
    print("Post liked with success.")


def comment_post(driver: Chrome, post_url:str, comment: str) -> None:
    """Comments a post with its url.
        # Returns
        - None if everything went well
    """
    driver.get(post_url)
    driver.implicitly_wait(5)
    
    driver.find_element(
        By.CSS_SELECTOR,
        "form[method='post'] textarea" # Comment input
    ).send_keys(comment)
    time.sleep(1)
    
    driver.find_element(
        By.CSS_SELECTOR,
        "button[type='submit']" # Post button
    ).click()
    
    print("Comment sent with success.")


def share_post_in_story(driver: Chrome, post_url: str) -> None:
    """Comments a post with its url.
        # Returns
        - None if everything went well
    """
    pass


def subscribe_to_user(driver: Chrome, user: str) -> None:
    """Subscribes to a user with its name."""
    username = user.replace("@", "")
    driver.get(f"https://www.instagram.com/{username}")
    driver.implicitly_wait(5)
    
    driver.find_element(By.CSS_SELECTOR, "button._acan._acap._acas").click()
    


def subscribe_to_multiple_users(driver: Chrome, users: List[str]) -> None:
    for user in users:
        subscribe_to_user(driver, user)
        time.sleep(2)


if __name__ == '__main__':
    connect(env.INSTA_USERNAME, env.INSTA_PASSWORD)