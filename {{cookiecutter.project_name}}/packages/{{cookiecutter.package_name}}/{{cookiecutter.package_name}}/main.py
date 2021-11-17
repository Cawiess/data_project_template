import pandas as pd

from {{cookiecutter.package_name}}.config.config import config
from {{cookiecutter.package_name}}.processing.data_manager import DataManager
from {{cookiecutter.package_name}}.pipelines import pipelines

def main():
    print('Starting...') #TODO: LOG HERE
    raw_data = DataManager.load_csv(file_name=config.package_config.raw_data)

    print('Preprocessing data...') #TODO: LOG HERE
    processed_data = pipelines.preprocessing_pipeline.fit_transform(raw_data)
    DataManager.export_excel(data=processed_data, file_name=config.package_config.processed_data)


    return 0

if __name__=='__main__':
    main()
    print('Finished.') # TODO: LOG HERE