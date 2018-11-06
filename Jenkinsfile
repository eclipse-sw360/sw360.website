pipeline {
 
  agent {
    kubernetes {
      label 'hugo-agent'
      yaml """
apiVersion: v1
metadata:
  labels:
    run: hugo
  name: hugo-pod
spec:
  containers:
    - name: hugo
      image: eclipsecbi/hugo:0.42.1
      command:
      - cat
      tty: true
"""
    }
  }
 
  environment {
    PROJECT_NAME = "sw360" // must be all lowercase.
    PROJECT_BOT_NAME = "SW360 Bot" // Capitalize the name
 
  }
 
 options {
    buildDiscarder(logRotator(numToKeepStr: '5'))
    checkoutToSubdirectory('hugo')
  }
 
  stages {
    stage('Checkout www repo') {
      steps {
        dir('www') {
            git branch: '$env.BRANCH_NAME',
                url: 'ssh://genie.${PROJECT_NAME}@git.eclipse.org:29418/www.eclipse.org/${PROJECT_NAME}.git',
                credentialsId: 'git.eclipse.org-bot-ssh'
        }
      }
    }
    stage('Build website with Hugo') {
      steps {
        container('hugo') {
            dir('hugo') {
                sh 'hugo -b https://www.eclipse.org/${PROJECT_NAME}/'
            }
        }
      }
    }
    stage('Push to $env.BRANCH_NAME branch') {
      steps {
        sh 'cp -Rvf hugo/public/* www/'
        dir('www') {
            sshagent(['b0848941-4b29-491c-9886-f5a0009202b9']) {
                sh '''
                git add -A
                if ! git diff --cached --exit-code; then
                  echo "Changes have been detected, publishing to repo 'www.eclipse.org/${PROJECT_NAME}'"
                  git config --global user.email "${PROJECT_NAME}-bot@eclipse.org"
                  git config --global user.name "${PROJECT_BOT_NAME}"
                  git commit -m "Website build ${JOB_NAME}-${BUILD_NUMBER}"
                  git log --graph --abbrev-commit --date=relative -n 5
                  git push origin HEAD:$env.BRANCH_NAME
                else
                  echo "No change have been detected since last build, nothing to publish"
                fi
                '''
            }
        }
      }
    }
  }
}
