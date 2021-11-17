import pandas as pd

from {{cookiecutter.package_name}}.config.config import config
from {{cookiecutter.package_name}}.processing.data_manager import DataManager

def main():
    print('Starting...') # TODO: LOG HERE
    raw_data = DataManager.load_csv(config.package_config.raw_data)
    print(raw_data.columns)


    return 0

if __name__=='__main__':
    main()
    print('Finished.') # TODO: LOG HERE