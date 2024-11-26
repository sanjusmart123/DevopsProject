#!/bin/bash
set -ex
kubectl apply -f Deployment.yml
sleep 10
kubectl apply -f Service.yml
sleep 10
kubectl apply -f configmap.yml
sleep 10
kubectl apply -f secretes.yml
sleep 10
kubectl apply -f ingress.yml
sleep 10
kubectl apply -f eggress.yml
sleep 10
kubectl apply -f pv.yml
sleep 10
kubectl apply -f pvc.yml
sleep 10
kubectl apply -f role.yml
sleep 10
kubectl apply -f rolebinding.yml
sleep 10
kubectl apply -f serviceacount.yml
sleep 10
kubectl apply -f statefulset.yml
sleep 10
kubectl apply -f daemonset.yml
sleep 10
