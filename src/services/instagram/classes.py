from typing import List

class AccountActionStats():
    """Actions stats on Instagram"""
    class __OneAccount():
        def __init__(self, account: str):
            self.account = account
            self.subscriptions_counter = 0
            self.likes_counter = 0
            self.comments_counter = 0
        
        def is_account(self, account: str) -> bool:
            return self.account == account
        
        def __str__(self) -> str:
            return f"Account: {self.account}, Subscriptions: {self.subscriptions_counter}, Likes: {self.likes_counter}, Comments: {self.comments_counter}"
    
    # Static variable
    accounts: List[__OneAccount] = []
    
    @staticmethod
    def get_account(account: str) -> __OneAccount:
        """Returns the account object if it exists, otherwise creates it."""
        for action_account in AccountActionStats.accounts:
            if action_account.is_account(account):
                print("Account already exists.")
                return action_account
        
        new_account = AccountActionStats.__OneAccount(account)
        AccountActionStats.accounts.append(new_account)
        return new_account 
    
    def __init__(self, account: str):
        self.account: AccountActionStats.__OneAccount = AccountActionStats.get_account(account)
        
    def get_subscriptions_counter(self) -> int:
        return self.account.subscriptions_counter
    
    def get_likes_counter(self) -> int:
        return self.account.likes_counter
    
    def get_comments_counter(self) -> int:
        return self.account.comments_counter
    
    def increment_subscriptions_counter(self, number: int = 1) -> int:
        self.account.subscriptions_counter += number
        return self.account.subscriptions_counter
        
    def increment_likes_counter(self, number: int = 1) -> int:
        self.account.likes_counter += number
        return self.account.likes_counter
    
    def increment_comments_counter(self, number: int = 1) -> int:
        self.account.comments_counter += number
        return self.account.comments_counter
    
    def __str__(self) -> str:
        return str(self.account)


if __name__ == "__main__":
    account_A = AccountActionStats("account_A")
    account_B = AccountActionStats("account_B")

    account_A.increment_likes_counter(100)
    account_B.increment_likes_counter()
    print("A", account_A.get_likes_counter())
    print("B", account_B.get_likes_counter())
    
    account_A2 = AccountActionStats("account_A")
    print("A2", account_A2.get_likes_counter())
    
