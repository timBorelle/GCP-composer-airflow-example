import pandas as pd
import joblib

from sklearn.ensemble import RandomForestRegressor
#from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

#df = pd.read_csv("gs://test-technique-folder-tim/data/train.csv", sep=";")
# gs://test-technique-folder-tim/data/test.csv
df = pd.read_csv("data/data_train.csv", sep=";")
#df.sample(5, random_state=44)

df = df.dropna()

# Separating the features (X) and the Labels (y)
X = df.drop(["quality"], axis=1)
#X = df.drop(["fixed acidity",
#    "volatile acidity",
#    "citric acid",
#    "residual sugar",
#    "chlorides",
#    "free sulfur dioxide",
#    "total sulfur dioxide",
#    "density",
#    "pH",
#    "sulphates",
#    "alcohol"], axis=1)
y = df["quality"]

#print(X.head(5))
#print(y.head(5))

# Training our random forest model
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=44)
# define the pipeline
pipeline = Pipeline([('normalize', StandardScaler()),
                     ('regressor', RandomForestRegressor())])

# Fit the model
pipeline.fit(X, y)

# Making predictions with our model
#predictions = rf_model.predict(X_test)
#print(predictions)

# Save the model
joblib.dump(pipeline, 'my_model.joblib')

