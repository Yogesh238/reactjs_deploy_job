pipeline {
    agent any
    parameters {
        string(defaultValue: 'latest', description: 'Enter BUILD NUMBER to deploy [Default Value: latest]:', name: 'BUILDTAG', trim: false)
    }
 stages {
     stage('Pull from Artifactory') {
            steps {
                sh 'aws s3 cp s3://kupos-reactjs-project/${BUILDTAG}.zip .'
            }
        }      
        stage("Deploy") {
            steps {
               // sh "service nginx stop"
                sh "chmod 777 /var/www/jenkins-react-app/*"
                sh "rm -rf /var/www/jenkins-react-app/*"
                sh "unzip -o ${BUILDTAG}.zip"
                sh "cp -r build/* /var/www/jenkins-react-app/"
                sh "chmod 555 /var/www/jenkins-react-app/*"
              //  sh "service nginx start"
            }
        }  
     }
}
