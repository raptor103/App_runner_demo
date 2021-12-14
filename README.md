**CI/CD demo container project with automatic deployment 
of a Machine learning app to
 AWS App runner**

This is a demo CI/CD project which aims to deploy a machine-learning
containerized app to AWS app runner. This app is a simple image classification model that is served on a Flask endpoint.

There are the following components:
1) Folder template - includes HTML files which serves as UI
2) app.py - core application that serves out predictions
3) Dockerfile - creates image from app

When code is pushed to Bitbucket, the commit is autodected and CI/CD Actions pipeline kicks in.
There can be several intermediate steps during build phase - just for testing purposes I use linting (flake8).
The application is deployed to AWS App runner.\

Run with:\
docker run -p 5000:5000 <name of built image>\

For local server, run on: localhost:5000