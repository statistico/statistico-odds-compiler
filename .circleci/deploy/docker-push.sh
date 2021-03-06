#!/bin/bash

set -e

aws ecr get-login --no-include-email --region $AWS_DEFAULT_REGION | bash

docker tag "statisticooddscompiler_grpc" "216629550457.dkr.ecr.eu-west-2.amazonaws.com/statistico-odds-compiler:$CIRCLE_SHA1"
docker push "216629550457.dkr.ecr.eu-west-2.amazonaws.com/statistico-odds-compiler:$CIRCLE_SHA1"
