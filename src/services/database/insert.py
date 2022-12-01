from datetime import datetime
import os
from typing import List

import pandas as pd

from src.services.database.tables import MANDATORY_FIELDS
from src.configs.environment_variables import PROJECT_ROOT


def insert_data(table: str, data: List[dict] | dict ) -> None:
    """Inserts data in the database."""
    now = datetime.now()
    data.update({"insert_datetime": now.isoformat()})
    table_filepath = os.path.join(PROJECT_ROOT, "database", f"{table}.csv")
    if not os.path.exists(table_filepath):
        with open(table_filepath, "w") as file:
            file.write(";".join(MANDATORY_FIELDS.get(table)+["insert_datetime"]))
            file.write("\n")
    
    with open(table_filepath, "a") as file:
        
        parsed_data = ";".join([str(value) for value in data.values()])
        file.write(parsed_data)
        file.write("\n")


def insert_in_giveaways(giveaways: pd.DataFrame) -> None:
    """Inserts giveaways in the database."""
    for field in MANDATORY_FIELDS.get("giveaways"):
        if field not in giveaways.columns:
            raise ValueError(f"Field '{field}' is not in the dataframe.")
    
    for giveaway in giveaways.to_dict("records"):
        insert_data("giveaways", giveaway)
    
    return None


if __name__ == "__main__":
    insert_in_giveaways(pd.DataFrame([
        {"id": "Test_id_1", "author": "Test_author_1"},
        {"id": "Test_id_2", "author": "Test_author_2"}
    ]))