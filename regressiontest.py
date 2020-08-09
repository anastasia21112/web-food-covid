import numpy as np
import pandas as pd
import numpy as np
import os

import math


from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso
from sklearn.linear_model import ElasticNet
from sklearn.linear_model import Ridge

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors


FOLDER = '/Users/anastasiadunca/web-food-covid/'
#load data from csv
def load_data_from_csv(fileName, data_path=FOLDER):
    csv_path = os.path.join(data_path,fileName)
    return pd.read_csv(csv_path, low_memory=False,index_col=0)

#function to save a dataframe to csv
def save_data_to_csv(data,fileName, data_path=FOLDER):
    csv_path = os.path.join(data_path, fileName)
    data.to_csv(csv_path)

data = load_data_from_csv('Food_Supply_kcal_Data.csv')


#data_complete = data.copy().drop(['Obesity', 'Undernourished', 'Deaths',
       #'Recovered', 'Active', 'Population', 'Unit (all except Population)'], axis = 1)

cols = ['Meat', 'Fish, Seafood', 'Milk - Excluding Butter', 'Eggs',
        'Starchy Roots', 'Sugar & Sweeteners', 'Fruits - Excluding Wine', 'Vegetables', 'Treenuts', 'Alcoholic Beverages', 'Confirmed']

data_complete = data[cols]

data_complete.isnull().sum()

data_complete[data_complete['Confirmed'].isnull()].index.tolist()

data_complete.shape

data_complete = data_complete.drop(['French Polynesia',
 'Kiribati',
 'Korea, North',
 'Myanmar',
 'New Caledonia',
 'Samoa',
 'Solomon Islands',
 'Turkmenistan',
 'Vanuatu'])

data_complete[data_complete['Confirmed'].isnull()].index.tolist()

data_complete.reset_index(drop=True, inplace=True)

np.corrcoef(data['Alcoholic Beverages'], data['Confirmed'])

fig, axes = plt.subplots(nrows=8, ncols=3, sharey=False, figsize=(15,40))
plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=0.25, hspace=0.25)
coeffs = []

for ax, feature in zip(axes.flat, data_complete.columns):
    ax.scatter(data_complete[feature], data_complete.Confirmed,s=10, c='b', marker="o")
    ax.set_title(feature)
    ax.grid(True)
    ax.set_xlabel(feature)
    ax.set_ylabel('Confirmed Cases')
    corr = np.corrcoef(data_complete[feature], data_complete.Confirmed)
    coeffs.append(corr[0][1])

    # these are matplotlib.patch.Patch properties
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)

    # place a text box in upper left in axes coords
    ax.text(0.65, 0.95, "R = %.3f"%corr[0][1], transform=ax.transAxes, fontsize=14,
        verticalalignment='top', bbox=props)
def plot_scatter(feature):
    plt.scatter(data_complete[feature], data_complete['Confirmed'])
    plt.xticks(rotation=25)

    corr = np.corrcoef(data_complete[feature], data_complete.Confirmed)

    plt.title("%s v. Confirmed Coronavirus Cases"%feature, fontsize=20)
    plt.xlabel("Age", fontsize = 12)
    plt.ylabel("Value", fontsize=12)
    plt.figure(figsize=(2, 2))
    m, b = np.polyfit(data_complete[feature], data_complete['Confirmed'], 1)
    plt.plot(data_complete[feature], m*data_complete[feature] + b)

for feature in data_complete.columns:
    plot_scatter(feature)
    plt.savefig('Correlations')

y = pd.DataFrame(data_complete['Confirmed'])
X = data_complete.copy().drop(['Confirmed'], axis = 1)
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.25, random_state=25)


lin_reg = LinearRegression()
lin_reg.fit(X_train, y_train)

train_r2 = lin_reg.score(X_train, y_train)
test_r2 = lin_reg.score(X_test, y_test)
y_pred = lin_reg.predict(X_test)

train_mse = mean_squared_error(y_train, lin_reg.predict(X_train))
test_mse = mean_squared_error(y_test, lin_reg.predict(X_test))



print('Training mean squared error: %.2f' % train_mse)
print('Testing mean squared error: %.2f' % test_mse)
print(' ')
#print('Training correlation coefficient, R: %.3f' % math.sqrt(train_r2))
#print('Testing correlation coefficient, R: %.3f' % math.sqrt(test_r2))
print(" ")
print('Training coefficient of determination, R^2: %.3f' % train_r2)
print('Testing coefficient of determination, R^2: %.3f' % test_r2)


plt.scatter(y_test, y_pred)
