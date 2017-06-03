#!/bin/bash
#"""
#cd hadan
#python setup.py sdist
#cd ..
#gcloud auth login#
#PACKAGE=hadan-0.0.0.tar.gz
#rm hadan-0.0.0.tar.gz
#tar zcvf $PACKAGE hadan PKG-INFO setup.py setup.cfg
#pip unsinstall hadan
#pip install --user $PACKAGE
#"""
#pip install --user --upgrade --force-reinstall --no-deps $PACKAGE
#gcloud auth application-default login

#gcloud config set project
#gcloud config set account telfordpan@gmail.com


BUCKET_NAME=gs://${USER}-hadan1-train
REGION="us-east1"
RUNTIME_VERSION="1.0"
# (One Time) Create a storage bucket to store training logs and checkpoints.
#gsutil mb -l $REGION $BUCKET_NAME
now=$(date +"%Y%m%d_%H%M%S")
JOB_NAME="hadan1_$now"

# Submit the training job.
#JOB_NAME=hadan1_train_$(date +%Y%m%d_%H%M%S); 
gcloud --verbosity=debug ml-engine jobs \
submit training $JOB_NAME \
--package-path hadan \
--module-name=hadan.trainer \
--staging-bucket=$BUCKET_NAME --region=us-east1 \
--config=hadan/cloudml-gpu.yaml 


