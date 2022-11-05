import os
from typing import List

import pandas as pd

from src.configs.environment_variables import PROJECT_ROOT

def get_data(table: str, return_dataframe: bool = False) -> List[dict] | pd.DataFrame:
    """Gets data from the database."""
    table_filepath = os.path.join(PROJECT_ROOT, "database", f"{table}.csv")
    with open(table_filepath, "r") as file:
        data = file.readlines()
        data = [line.strip().split(";") for line in data]
        data = [dict(zip(data[0], line)) for line in data[1:]]
    
    if return_dataframe:
        return pd.DataFrame(data)
    
    return data


if __name__ == "__main__":
    print(get_data("giveaways", True))