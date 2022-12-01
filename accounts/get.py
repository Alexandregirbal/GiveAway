import os
from typing import Iterable

from src.configs.environment_variables import PROJECT_ROOT
from src.utils.files import load_json_file


def get_instagram_accounts(filter: str = None) -> Iterable[dict]:
    """Returns an iterable of Instagram accounts."""
    instagram_accounts_path = os.path.join(PROJECT_ROOT ,"accounts/instagram")
    for credentials_file in os.listdir(instagram_accounts_path):
        if credentials_file.startswith("template."):
            continue
        
        if filter and not credentials_file.startswith(filter):
            continue
        
        users_credentials = load_json_file(os.path.join(instagram_accounts_path, credentials_file))
        for user_credentials in users_credentials:
            yield user_credentials
            
if __name__ == "__main__":
    insta_accounts = get_instagram_accounts("new")
    for account in insta_accounts:
        print(account)