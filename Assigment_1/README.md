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

Navigate to the folder kubernetes, it contains Kubernetes manifests.

Deploy MySQL:

First, set up the persistent storage for MySQL:

```
kubectl apply -f mysql-pv.yaml
kubectl apply -f mysql-pvc.yaml
```
Then, deploy the MySQL service and deployment:
```
kubectl apply -f mysql-deployment.yaml
kubectl apply -f mysql-service.yaml
```

Deploy Flask Application:

Deploy the Flask application service and deployment:
```
kubectl apply -f app-deployment.yaml
kubectl apply -f app-service.yaml
```

Access the Application:

If you've set up the Flask application service as a **LoadBalancer**, it might take a few minutes for the external IP to be provisioned (especially on cloud providers). Once provisioned, you can access the application using that IP.

To get the external IP:
```
kubectl get svc phonebook-app
```
Look for the "EXTERNAL-IP" column in the output.

Scaling & Management:

To scale the Flask application, adjust the **replicas** field in **app-deployment.yaml** and reapply the configuration:

```
kubectl apply -f k8s/app/app-deployment.yaml
```

To monitor the pods and services:
```
kubectl get pods
kubectl get svc
```

To check logs for a specific pod:
```
kubectl logs <POD_NAME>
```

Clean Up (Optional):

If you want to remove the deployed resources:

```
kubectl delete -f k8s/app/app-deployment.yaml
kubectl delete -f k8s/app/app-service.yaml
kubectl delete -f k8s/mysql/mysql-deployment.yaml
kubectl delete -f k8s/mysql/mysql-service.yaml
kubectl delete -f k8s/mysql/mysql-pvc.yaml
kubectl delete -f k8s/mysql/mysql-pv.yaml
```
This will delete the application and database deployments, services, and persistent storage configurations.
