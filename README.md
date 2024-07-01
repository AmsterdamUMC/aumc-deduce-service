# Deduce Service

> This is a fork from the original, no longer maintained/updated, repo from UMCU.

Web Service for [Deduce](https://github.com/AmsterdamUMC/aumc-deduce), to be used in pipelines such as [CogStack-NiFi](https://github.com/cogstack/cogstack-nifi).



## Installation
We do not use a docker container to run this.

- clone the repo to you r environment.
- pip install install Gunicorn and Flask with their dependencies
- start gunicorn with the installed dedice-service/app

The API should now be available at http://localhost:5000/

## Usage
- Use `/deidentify` for de-identification of a single text.
- Use `/deidentify_bulk` for de-identification of multiple texts.
See documentation in Swagger UI for the specific data format.
  
## Tests
In your IDE of choice, add a run configuration for `test/test_service.py` and set the working directory to the root directory of this repository.
