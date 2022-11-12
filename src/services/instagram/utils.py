from selenium.webdriver import Chrome
def get_post_url_from_id(post_id) -> str:
    """Gets the post full url from its id."""
    return f"https://www.instagram.com/p/{post_id}/"

def driver_get_if_not_here_already(driver: Chrome, url: str) -> None:
    if driver.current_url != url:
        driver.get(url)