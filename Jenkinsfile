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
                sh "sudo chmod 777 /var/www/jenkins-react-app/"
              //  sh "sudo rm -rf /var/www/jenkins-react-app/*"
                sh "unzip -o ${BUILDTAG}.zip"
                sh "sudo cp -r build/* /var/www/jenkins-react-app/"
                sh "sudo chmod 555 /var/www/jenkins-react-app/*"
              //  sh "service nginx start"
            }
        }  
     }
}
