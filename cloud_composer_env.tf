resource "google_composer_environment" "example" {
  provider = google-beta
  name = "airflow"
  region = "europe-west1"

  config {
    software_config {
      image_version = "composer-1.20.0-airflow-1.10.15"
    }
  }
}
