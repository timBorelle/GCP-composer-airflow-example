import pandas as pd

# from sklearn import datasets
#from datasets import load_dataset

from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import RandomForestClassifier
#from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split


# gs://test-technique-folder-tim/data/train.csv
# gs://test-technique-folder-tim/data/test.csv
#dataset = load_dataset('csv', data_files={'train': ['data/data_train.csv'],
#                                          'test': 'data/data_test.csv'})
df = pd.read_csv("data/data_train.csv", sep=";")
df.sample(5, random_state=44)


df = df.dropna()

#train = dataset['train']        # .drop(['quality'], axis=1)
#test = dataset['test']

# Separating the features (X) and the Labels (y)
X = df.drop(["fixed acidity",
    "volatile acidity",
    "citric acid",
    "residual sugar",
    "chlorides",
    "free sulfur dioxide",
    "total sulfur dioxide",
    "density",
    "pH",
    "sulphates",
    "alcohol"], axis=1)
y = df["quality"]

print(X.head(5))
#print(train)

# Training our random forest model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=44)
## define the model
#model = RandomForestRegressor()
rf_model = RandomForestClassifier(n_estimators=50, max_features="sqrt", random_state=44)
rf_model.fit(X_train, y_train)

# fit the model on the whole dataset
#model.fit(X, y)

# Making predictions with our model
predictions = rf_model.predict(X_test)
print(predictions)

