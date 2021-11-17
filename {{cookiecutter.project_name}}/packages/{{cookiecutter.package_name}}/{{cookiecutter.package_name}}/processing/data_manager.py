import pandas as pd

from {{cookiecutter.package_name}}.config import config


class DataManager:
    def load_csv(*, file_name: str) -> pd.DataFrame:
        _data = pd.read_csv(f"{config.INPUT_DIR}/data/{file_name}.csv")
        return _data

    def export_excel(*, data: pd.DataFrame, file_name: str) -> None:
        data.to_excel(f"{config.OUTPUT_DIR}/{file_name}_{config.TODAY}.xlsx", index=False)
        return None




