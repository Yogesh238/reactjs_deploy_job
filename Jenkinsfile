pipeline {
    agent any
    parameters {
        choice(choices: ['stage', 'prod'], description: 'Choose the environment in which you want to deploy:', name: 'ENVIRONMENT')
        string(defaultValue: 'latest', description: 'Enter BUILD NUMBER to deploy [Default Value: latest]:', name: 'BUILDTAG', trim: false)
    }
 stages {
     stage('Pull from Artifactory') {
         steps {
                script {
                     if ( params.ENVIRONMENT=='prod') {
                         sh 'aws s3 cp s3://kupos-reactjs-prod/${BUILDTAG}.zip .'
                    }
                     else if ( params.ENVIRONMENT=='stage') {   
                         sh 'aws s3 cp s3://kupos-reactjs-stage/${BUILDTAG}.zip .'
                                }
                            }
                }
        }
          stage("Deploy"){
             steps{
                sshagent(credentials : ['applicationserver']) { 
                     script {
                     if ( params.ENVIRONMENT=='prod') {
                          sh 'sh deploy.sh $PROD_SERVER /home/ubuntu/reactjs/prod nginx.service'
                    }
                     else if ( params.ENVIRONMENT=='stage') {                   
                          sh 'sh deploy.sh $STAGE_SERVER /home/ubuntu/reactjs/stage nginx.service'
                         
                                }
                            }
                        }
                    }
                }
     stage('Infra Sanity Check') {
          steps{
           script {
                     if ( params.ENVIRONMENT=='prod') {
                        sh 'python3 infra_sanity_test.py PROD http://$PROD_SERVER:2001'
                    }
                     else if ( params.ENVIRONMENT=='stage') {
                        sh 'python3 infra_sanity_test.py STAGE http://$STAGE_SERVER:2000'
                                }
                           }
                }
          }      
     }
}
