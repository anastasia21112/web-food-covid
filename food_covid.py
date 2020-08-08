## save This
## cd into the directory with the file
## run the code by running python filename.py
# damn daph good job
import numpy as np
import pandas as pd
import numpy as np
import os

DATASETS_PATH = 'web_food_covid'

def load_data_from_csv(fileName, data_path=DATASETS_PATH):
    csv_path = os.path.join(data_path,fileName)
    return pd.read_csv(csv_path, low_memory=False,index_col=0)

#function to save a dataframe to csv
def save_data_to_csv(data,fileName, data_path=DATASETS_PATH):
    csv_path = os.path.join(data_path, fileName)
    data.to_csv(csv_path)

data = load_data_from_csv('Food_Supply_kcal_Data.csv')
data.head()
