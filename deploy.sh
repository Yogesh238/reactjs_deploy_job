#!/bin/bash
ssh -o StrictHostKeyChecking=no ubuntu@${1} sudo systemctl stop ${3}
scp ${BUILDTAG}.zip ubuntu@${1}:${2}
ssh -o StrictHostKeyChecking=no ubuntu@${1} unzip -o ${2}/${BUILDTAG}.zip -d ${2}
ssh -o StrictHostKeyChecking=no ubuntu@${1} sudo systemctl start ${3}
