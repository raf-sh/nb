import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

train_data = pd.read_csv("data/train.csv")
test_data = pd.read_csv("data/test.csv")

train_data.head()

train_data.drop('PassengerId', axis=1, inplace=True)
# train_data.describe()

# fig = plt.figure(figsize=(10,4))
# fig.add_subplot(121)
train_data.Survived[train_data['Sex'] == 'male'].value_counts().plot()