pipeline {
    agent {label 'Jenkins-agent'}
     tools {
        jdk 'local_setup_jdk'
        maven 'maven3_6'
    }

    stages{
        stage("Cleanup Workspace"){
            steps{
                cleanWs()
            }
            
        }

        stage("Checkout from SCM"){
            steps{
                git branch: 'main',credentialsId: 'github', url:'https://github.com/dineshroyal9121687814/register-app'
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
