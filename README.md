# Introduction
This is a demo of how to use KEDA and Kubernetes to scale RabbitMQ consumers based on the number of messages in the queue.

# Steps

## Enable k8s in docker desktop
Settings -> Kubernetes -> Enable Kubernetes

## Run rabbitmq in local docker

    ```bash
    docker run -d --hostname my-rabbit --name some-rabbit -p 5672:5672 -p 15672:15672 rabbitmq:3-management
    ```

### Get rabbitmq container ip

    ```bash
    docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' some-rabbit
    ```

    write that ip in the consumer.py file
    and the consumer-scaler.yaml file (this should go, for instance, in a config map in the real application)


## Install keda in the k8s cluster
    
    ```bash
    kubectl apply --server-side -f https://github.com/kedacore/keda/releases/download/v2.11.0/keda-2.11.0.yaml
    ```

## Create the consumer docker image
In Visual Studio Code, right click on the Dockerfile file and select "Build Image"

## Deploy the consumer to k8s

    ```bash
    kubectl apply -f .\consumer-deployment.yaml
    ```

## Deploy the scaler to k8s

    ```bash
    kubectl apply -f .\consumer-scaler.yaml
    ```

## Send messages to the queue

    ```bash
    python .\producer.py
    ```

## Check the scaler logs

    ```bash
    kubectl describe hpa
    ```
