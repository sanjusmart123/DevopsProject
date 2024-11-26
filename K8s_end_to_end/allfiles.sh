!#/bin/bash
set -ex
k create -f Deployment.yml
sleep 15
k create -f Service.yml
sleep 15
k create -f config.yml
sleep 15
k create -f secretes.yml
sleep 15
k create -f ingress.yml
sleep 15
k create -f eggress.yml
sleep 15
k create -f pv.yml
sleep 15
k create -f pvc.yml
sleep 15
k create -f role.yml
sleep 15
k create -f rolebinding.yml
sleep 15
k create -f serviceacount.yml
sleep 15
k create -f statefulset.yml
sleep 15
k create -f daemonset.yml
sleep 15
