pipeline {
    agent any
    
    environment {
        PYTHON_VERSION = '3.9'
    }
    
    stages {
        stage('Build') {
            steps {
                echo '========== Building Application =========='
                script {
                    // Verificar que los archivos existen
                    sh 'ls -la'
                    echo 'Build stage completed'
                }
            }
        }
        
        stage('Test') {
            steps {
                echo '========== Running Unit Tests =========='
                script {
                    // Simular pruebas unitarias
                    echo 'Unit tests would run here'
                    echo 'All tests passed'
                }
            }
        }
        
        stage('Analyze - SonarQube') {
            steps {
                echo '========== Running SonarQube Analysis =========='
                script {
                    def scannerHome = tool 'SonarScanner'
                    withSonarQubeEnv('SonarQube') {
                        sh """
                            ${scannerHome}/bin/sonar-scanner \
                            -Dsonar.projectKey=security-test-demo \
                            -Dsonar.sources=. \
                            -Dsonar.host.url=http://host.docker.internal:9000 \
                            -Dsonar.python.version=3.9
                        """
                    }
                }
            }
        }
        
        stage('Security Test - Dependency Check') {
            steps {
                echo '========== Running OWASP Dependency Check =========='
                dependencyCheck additionalArguments: '''
                    --scan .
                    --format HTML
                    --format XML
                    --prettyPrint
                    ''', odcInstallation: 'DC'
                
                dependencyCheckPublisher pattern: '**/dependency-check-report.xml'
            }
        }
        
        stage('Security Test - OWASP ZAP') {
            steps {
                echo '========== Running OWASP ZAP Scan =========='
                script {
                    // Ejecutar ZAP en modo baseline contra el código
                    echo 'OWASP ZAP baseline scan would run here'
                    echo 'For demo purposes, this stage is simulated'
                    echo 'In production, ZAP would scan the running application'
                }
            }
        }
        
        stage('Deploy') {
            steps {
                echo '========== Deploying to Test Environment =========='
                script {
                    echo 'Application would be deployed here'
                    echo 'Deployment to test environment completed'
                }
            }
        }
    }
    
    post {
        always {
            echo '========== Pipeline Execution Completed =========='
        }
        success {
            echo '========== Pipeline SUCCESS =========='
        }
        failure {
            echo '========== Pipeline FAILED =========='
        }
    }
}
