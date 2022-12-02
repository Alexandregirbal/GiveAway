import os
from time import sleep
import time
from typing import List

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.chrome.service import Service as ChromeService

from src.configs.selenium_options import CHROMEDRIVER_PATH
from src.configs.environment_variables import PROJECT_ROOT
from src.services.instagram.classes import AccountActionStats
from src.services.instagram.exceptions import BlockedByInstagramException
from src.services.instagram.utils import driver_get_if_not_here_already, get_post_url_from_id

def connect(username: str, password: str) -> Chrome:
    """Connects to Instagram with user credentials. Uses the same chrome user every time."""
    print("Connecting to Instagram with user:", username)
    chrome_options = ChromeOptions()
    browser_cache_folder = os.path.join(PROJECT_ROOT, "browser-cache")
    chrome_options.add_argument(f"--user-data-dir={browser_cache_folder}")
    chrome_options.add_argument(f"--profile-directory={username}")

    driver = Chrome(
        service=ChromeService(CHROMEDRIVER_PATH),
        options=chrome_options,
    )
    driver.get("https://www.instagram.com/")
    driver.implicitly_wait(5)
    
    # Accept cookies
    try:
        driver.find_element(By.XPATH, "//button[text()='Only allow essential cookies']").click()
    except NoSuchElementException:
        pass
    
    try:
        driver.find_element(By.CSS_SELECTOR, "input[name='username']").send_keys(username)
        driver.find_element(By.CSS_SELECTOR, "input[name='password']").send_keys(password)
        login_element = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    except NoSuchElementException:
        print("Already logged in.")
        return driver
    
    try: 
        login_element.click()
    except ElementClickInterceptedException:
        login_element.click()
        
    sleep(8)
    return driver


def like_post(driver: Chrome, post_id:str) -> None:
    """Likes a post with its url.
        # Returns
        - None if everything went well
    """
    driver_get_if_not_here_already(driver, get_post_url_from_id(post_id))
    driver.implicitly_wait(5)
    
    try: 
        driver.find_element(By.CSS_SELECTOR, "span > svg[aria-label='Like']").click()
        print("Post liked with success.")
    except NoSuchElementException:
        driver.find_element(By.CSS_SELECTOR, "span > svg[aria-label='Unlike']")
        print("Post already liked.")
    
    return


def comment_post(driver: Chrome, post_id:str, comment: str) -> None:
    """Comments a post with its url.
        # Returns
        - None if everything went well
    """
    driver_get_if_not_here_already(driver, get_post_url_from_id(post_id))
    time.sleep(5)
    
    comment_text_area = driver.find_element(
        By.CSS_SELECTOR,
        "form[method='post'] textarea" # Comment input
    )
    comment_text_area.click()
    ActionChains(driver).send_keys(comment).perform()
    # comment_text_area.send_keys(comment)
    time.sleep(1)
    
    driver.find_element(
        By.CSS_SELECTOR,
        "form div[role='button']" # Post button
    ).click()
    
    print("Comment sent with success.")


def share_post_in_story(driver: Chrome, post_url: str) -> None:
    """Comments a post with its url.
        # Returns
        - None if everything went well
    """
    pass


def _subscribe_to_user(driver: Chrome, user: str, account_stats: AccountActionStats) -> None:
    """Subscribes to a user with its name."""
    username = user.replace("@", "")
    driver.get(f"https://www.instagram.com/{username}")
    time.sleep(3)
    
    driver.find_element(
        By.CSS_SELECTOR,
        "button._acan._acap._acas"
    ).click() # Subscribe button
    time.sleep(2)
    
    try:
        driver.find_element(
            By.CSS_SELECTOR,
            "_acan _acap _acat"
        ).click() # Unsubscribe button
        print("Subscribed to user with success.")
        account_stats.increment_subscriptions_counter()
    
    except NoSuchElementException:
        print("Could not subscribe to user. Trying to understand why...")
        try:
            error_element = driver.find_element(
                By.CSS_SELECTOR,
                "div > h3"
            )
            print(error_element.text)
            if error_element.text == "Try Again Later":
                raise BlockedByInstagramException()
            
            no_subscribe_reason = f"Message: {error_element.text}"
        
        except NoSuchElementException:
            no_subscribe_reason = "Reason unknown"
            print(f"No idea what happened. Please check manually for this user: {user}")
        
        raise Exception(f"Could not subscribe to user ({no_subscribe_reason}).")


def subscribe_to_multiple_users(account: str, driver: Chrome, users: List[str]) -> None:
    account_stats = AccountActionStats(account)
    for user in users:
        _subscribe_to_user(driver, user, account_stats)
        time.sleep(2)


if __name__ == '__main__':
    connect("Test", "Test")