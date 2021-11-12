from sklearn.pipeline import Pipeline
#TODO: Import preprocessors and analyzers needs setup of config files.


'''
This module contains the Sklearn pipelines which gathers the preprocessors and analyzers
into an ordered sequence of operations. These pipelines are then executed by the main.py module.
'''


### DATA PREPROCESSING
preprocessing_pipeline = Pipeline(
    [
        (
            "Preprocessing pipeline step One",
            print('Step one')
        ),
        (
            "Preprocessing pipeline Step Two",
            print('Step two')
        )
    ]
)


### DATA FILTERING AND VARIABLE SELECTION
filtering_pipeline = Pipeline(
    [
        (
            "Filtering pipeline step One",
            print('Step one')
        ),
        (
            "Filtering pipeline Step Two",
            print('Step two')
        )
    ]
)