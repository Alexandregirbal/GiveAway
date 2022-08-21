import requests
import wget
import zipfile
import os

from src.configs.environment_variables import PROJECT_ROOT

def get_latest_chromedriver_version():
    """Returns the latest chromedriver version"""
    url = 'https://chromedriver.storage.googleapis.com/LATEST_RELEASE'
    response = requests.get(url)
    return response.text


def download_chromedriver(version_number: str, os_binary: str = "linux64"):
    """Downloads the chromedriver binary from a given version number.
        # Arguments
        - `version_number`: The version number of the chromedriver binary.
        - `os_binary`: The operating system of the chromedriver binary. It can be one of the following:
            - linux64 (default)
            - mac64
            - mac64_m1
            - win32
    """
    download_url = f"https://chromedriver.storage.googleapis.com/{version_number}/chromedriver_{os_binary}.zip"

    driver_zip = wget.download(download_url,'chromedriver.zip')

    with zipfile.ZipFile(driver_zip, 'r') as zip_ref:
        zip_ref.extractall(PROJECT_ROOT)
    
    os.remove(driver_zip)
    
if __name__ == '__main__':
    version_number = get_latest_chromedriver_version()
    download_chromedriver("102.0.5005.61")