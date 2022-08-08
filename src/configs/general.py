from os import environ

from dotenv import load_dotenv

load_dotenv()


PROJECT_ROOT = environ.get("PYTHONPATH")


if __name__ == "__main__":
    print(PROJECT_ROOT)