# Cloud-Computing-och-Big-Data Assigment_1
This repository is a fork of https://github.com/muhammadhanif/crud-application-using-flask-and-mysql/.

In addition to the original project, this version includes functionality for deploying the applications using Kubernetes, with manifests (YAML files) for each application component located in the **kubernetes** folder. Furthermore, an implementation of REST API was added to the server application, allowing for programmatic access to phonebook entries.

The original project was developed using the following technologies:

- Python
- Python Libraries: Flask and PyMySQL
- MySQL
- AdminLTE 2

## Set up

### Build the Docker Images

```
docker build -t <DOCKERHUB_USERNAME>/phonebook-app:latest -f Dockerfile-app .
docker build -t <DOCKERHUB_USERNAME>/phonebook-mysql:latest -f Dockerfile-mysql .
```
### Push the Docker Images to Docker Hub
```
docker login

docker push <DOCKERHUB_USERNAME>/phonebook-app:latest
docker push <DOCKERHUB_USERNAME>/phonebook-mysql:latest
```
Replace <DOCKERHUB_USERNAME> with your Docker Hub username.

### Deploy the application on Kubernetes using the Docker images

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

### Access the Application:

If you've set up the Flask application service as a **LoadBalancer**, it might take a few minutes for the external IP to be provisioned (especially on cloud providers). Once provisioned, you can access the application using that IP.

To get the external IP:
```
kubectl get svc phonebook-app
```
Look for the "EXTERNAL-IP" column in the output.

### Scaling & Management:

To scale the Flask application, adjust the **replicas** field in **app-deployment.yaml** and reapply the configuration:

```
kubectl apply -f k8s/app/app-deployment.yaml
```
### Test the REST API 

You can test the REST API using tools like curl or Postman. Here are some examples of how you can use curl to test the REST API:

**Get all phonebook entries:**
```
curl http://localhost:8181/api/phonebook
```

**Get a single phonebook entry by ID:**
```
curl http://localhost:8181/api/phonebook/1
```

**Create a new phonebook entry:**
```
curl -X POST -H "Content-Type: application/json" -d '{"name": "Alice", "phone": "123-456-7890", "address": "123 Main St"}' http://localhost:8181/api/phonebook
```

**Update a phonebook entry by ID:**
```
curl -X PUT -H "Content-Type: application/json" -d '{"name": "Alice", "phone": "987-654-3210", "address": "456 Elm St"}' http://localhost:8181/api/phonebook/1
```

**Delete a phonebook entry by ID:**
```
curl -X DELETE http://localhost:8181/api/phonebook/1
```

### To monitor the pods and services:
```
kubectl get pods
kubectl get svc
```

### To check logs for a specific pod:
```
kubectl logs <POD_NAME>
```

### Clean Up (Optional):

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
