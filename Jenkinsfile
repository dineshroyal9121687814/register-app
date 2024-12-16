pipeline {
    agent {label 'Jenkins-agent'}
    Tools {
        jdk 'Java17'
        maven 'Maven3'
    }

    stages{
        stage("Cleanup Workspace"){
            steps{
                cleanWs()
            }
            
        }

        stage("Checkout from SCM"){
            steps{
                git branch: 'main',CredintialsId: 'github', url:'https://github.com/dineshroyal9121687814/register-app'
            }
        }

        stage("Build Application"){
            steps {
                sh "mvn clean package"
            }

       }
       stage("Test Application"){
           steps {
                 sh "mvn test"
           }
       }
    }
}
