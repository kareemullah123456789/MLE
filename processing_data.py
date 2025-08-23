import pandas as pd
import numpy as np
import seaborn as sns

from sklearn.preprocessing import StandardScaler,LabelEncoder,OneHotEncoder,OrdinalEncoder
import warnings
import matplotlib.pyplot as plt
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import FunctionTransformer
import pickle
from sklearn.pipeline import Pipeline
warnings.filterwarnings('ignore')

def div_by_30(x):
    return x/30
custom = FunctionTransformer(div_by_30)

def same(x):
    return x
passthru = FunctionTransformer(same)