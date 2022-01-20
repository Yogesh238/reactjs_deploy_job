#!/bin/bash
sleep 60s
tag=`aws s3api head-object --bucket kt-session-yogesh-sachin --key KT_Demo/demo.zip --query ETag --output=text`
echo $tag
aws deploy create-deployment --application-name KT_Demo --deployment-config-name CodeDeployDefault.AllAtOnce --deployment-group-name KT_Demo_dg --description "deployment" --s3-location bucket=kt-session-yogesh-sachin,bundleType=zip,eTag=${tag},key=KT_Demo/demo.zip
