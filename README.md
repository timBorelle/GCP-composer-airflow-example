# GCP-composer-airflow-example

Deploy a dag under Airflow to train a regression model (random forrest with scikit-learn) every 2 weeks using training and test data available on Cloud Storage (GCS).

## Installation

### Set up a python environment with the necessary dependencies to composer-airflow  

```bash
terraform init
terraform plan
terraform apply
```

### Create virtual env
```bash
python3 -m venv venv
```

### Activate virtual env
```bash
source venv/bin/activate
```
