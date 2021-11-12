import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin

from typing import List


'''
Rationale for BaseEstimator and TransformerMixin:

Each project is unique in its details, similar to others in terms of overarching functionality.
Sklearn offers well established functionality which is highly compatible with other services.
Useful core functionalities of Sklearn can be implemented project specific classes through
inheritance of methods from the BaseEstimator and TransformerMixin classes.

By inheriting the methods of the BaseEstimator and TransformerMixin, the preprocessors defined
here can be directly integrated into a Sklearn pipeline.

The user can find a template for a Preprocessing unit which is ready to be extended with
purpose-specific code, as well as a simple usecase below.

'''

class PreprocessorUnitTemplate(BaseEstimator, TransformerMixin):
    def __init__(self, variables: List[str]) -> None:
        '''
        Specify variable input as list of strings representing column names of a pd.DataFrame.
        '''
        # YOUR CODE HERE
        return None
    
    def fit(self, X: pd.DataFrame, y: pd.Series = None):
        '''
        Required method for Sklearn TransformerMixin class.
        Remains inactive and performs no action for now.
        Leave as is.
        '''
        return self

    def transform(self, X: pd.DataFrame, y: pd.Series = None):
        '''
        Creates a copy of input dataframe, which is passed to method via the sklearn Pipeline.
        This method performs changes to the dataframe with reference to specified variables.
        The modified copy of the original dataframe is then returned and passed to the next step in pipeline.
        Define your specific transformation here.
        '''
        X = X.copy()
        # YOUR CODE HERE

        return X

class ExtractSubsetVariables(BaseEstimator, TransformerMixin):
    def __init__(self, variables: List[str]):
        ''' Extracts selected variables only. '''

        if not isinstance(variables, list):
            raise ValueError("variables must be given as elements of list.")
        
        self.variables = variables

    def fit(self, X: pd.DataFrame, y: pd.Series = None):
        return self

    def transform(self, X: pd.DataFrame):
        
        X = X.copy()
        X = X[self.variables]

        return X