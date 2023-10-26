# Cloud-Computing-och-Big-Data Assigment_1
This repo is a clone of https://github.com/muhammadhanif/crud-application-using-flask-and-mysql/.

What is new is the kubernetes folder.

#### Built With

* Python
* Python Libraries: flask and pymysql
* MySQL
* AdminLTE 2

#### Installation
Build the Docker Images:

```
docker build -t <DOCKERHUB_USERNAME>/phonebook-app:latest -f Dockerfile-app .
docker build -t <DOCKERHUB_USERNAME>/phonebook-mysql:latest -f Dockerfile-mysql .
```
Push the Docker Images to Docker Hub:
```
docker login

docker push <DOCKERHUB_USERNAME>/phonebook-app:latest
docker push <DOCKERHUB_USERNAME>/phonebook-mysql:latest
```
Replace <DOCKERHUB_USERNAME> with your Docker Hub username.

Deploy the application on Kubernetes using the Docker images.



After executing, you will have 2 running cointainers on your Docker host: `phonebook-app` and `phonebook-mysql`. For accessing the web application, open your browser and go to http://your-docker-host-ip-address:8181

