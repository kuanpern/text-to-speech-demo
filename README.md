# Text to speech using GCP service

This repository showcases the use of GCP [Text-to-Speech AI
](https://cloud.google.com/text-to-speech?hl=en) to generate audio file (mp3) from text.

## GCP Project Setup

Create a project with name `PROJECT_NAME`.

[Create a service account](https://console.cloud.google.com/iam-admin/serviceaccounts) and download the service account credential file (json)

```sh
# set environment variable to point to the service file
export GOOGLE_APPLICATION_CREDENTIALS=/path/to/key.json
# list all projects
gcloud projects list
# set quota project for the project
gcloud auth application-default set-quota-project $PROJECT_ID
```

You may test the setup by printing the access token
```sh
gcloud auth application-default print-access-token
```


## Sample project
Currently only a minimal python file is included to demonstrate the capability. To run
the run, simply do

```sh
python main.py
```


## Quick notes

List of support voices
* https://cloud.google.com/text-to-speech/docs/voices

