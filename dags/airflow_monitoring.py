"""A liveness prober dag for monitoring composer.googleapis.com/environment/healthy."""
import airflow
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
#from airflow.operators.python import PythonOperator
from airflow.operators.python_operator import PythonOperator
from datetime import timedelta

import pandas as pd
import joblib

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from google.cloud import storage

default_args = {
    'start_date': airflow.utils.dates.days_ago(0),
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG(
    'airflow_monitoring',
    default_args=default_args,
    description='liveness monitoring dag',
    schedule_interval='1 0 */14 * 1',
    dagrun_timeout=timedelta(minutes=20))

# train a random forrest model
def trainModel():
    df = pd.read_csv("gs://test-technique-folder-tim/data/train.csv", sep=";")
    print("Success reading from GCS")
    df = df.dropna()
    # Separating the features (X) and the Labels (y)
    X = df.drop(["quality"], axis=1)
    y = df["quality"]
    pipeline = Pipeline([('normalize', StandardScaler()),
                     ('regressor', RandomForestRegressor())])
    # Fit the model
    pipeline.fit(X, y)
    # Making predictions with our model
    #predictions = rf_model.predict(X_test)
    # Save the model
    joblib.dump(pipeline, 'model_v2.joblib', compress=1)
    # read from GCS bucket
    storage_client = storage.Client()
    bucket_name = "test-technique-folder-tim"
    model_bucket = "model.joblib"
    model_local = "local.joblib"

    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(model_bucket)
    blob.download_to_filename(model_local)
    loaded_model = joblib.load(model_local)

    result = loaded_model.score(X, y)
    print(result)

train_model = PythonOperator(
    task_id="train_model",
    python_callable=trainModel,
    dag=dag
)

# deploy a new model version to GCS
copy_joblib_model = BashOperator(
    task_id='copy_joblib_model',
    bash_command="""
        export AIRFLOW_BUCKET="test-technique-folder-tim" && \
        gsutil cp copy_joblib_model* gs://${AIRFLOW_BUCKET}/model_v2.joblib
    """,
    dag=dag
)

train_model >> copy_joblib_model
