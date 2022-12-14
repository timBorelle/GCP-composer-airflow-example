"""A liveness prober dag for monitoring composer.googleapis.com/environment/healthy."""
import airflow
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import timedelta

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

# priority_weight has type int in Airflow DB, uses the maximum.
t1 = BashOperator(
    task_id='echo',
    bash_command='echo test',
    dag=dag,
    depends_on_past=False,
    priority_weight=2**31 - 1,
    do_xcom_push=False
)

# train a random forrest model and deploy a new version model to GCP AI Platform
train_random_forest_model = BashOperator(
    task_id='train_random_forest_model',
    bash_command="""
        python3 gs://test-technique-folder-tim/model.joblib && \
        MY_BUCKET=europe-west1-airflow-981d3f00-bucket \
        gsutil cp ./model.joblib gs://$MY_BUCKET/data/model.joblib
    """,
    dag=dag
)
