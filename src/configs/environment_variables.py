import os

from dotenv import load_dotenv

load_dotenv()

PROJECT_ROOT = os.environ.get("PYTHONPATH")
# os.environ["PYTHONPATH"] = os.path.join(PROJECT_ROOT, "src")


if __name__ == "__main__":
    print(PROJECT_ROOT)