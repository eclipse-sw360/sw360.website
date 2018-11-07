// See documentation on: https://wiki.eclipse.org/Jenkins#Build_my_project.27s_website_with_Jenkins.3F

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
                sh '''
if ! grep -q "^git.eclipse.org" ~/.ssh/known_hosts; then
  mkdir -p ~/.ssh
  ssh-keyscan -t rsa git.eclipse.org >> ~/.ssh/known_hosts
fi
'''
                dir('www') {
                    git branch: "master",
                        url: "ssh://genie.${PROJECT_NAME}@git.eclipse.org:29418/www.eclipse.org/${PROJECT_NAME}.git",
                        credentialsId: 'b0848941-4b29-491c-9886-f5a0009202b9'
                }
            }
        }
        stage('Build website with Hugo') {
            steps {
                container('hugo') {
                    dir('hugo') {
                        sh 'hugo -b https://www.eclipse.org/sw360/'
                    }
                }
            }
        }
        stage('Push www') {
            steps {
                sh 'cp -Rvf hugo/public/* www/'
                dir('www') {
                    sshagent(['b0848941-4b29-491c-9886-f5a0009202b9']) {
                        sh """
git add -A
if ! git diff --cached --exit-code; then
  echo "Changes have been detected, publishing to repo 'www.eclipse.org/sw360'"
  git config --global user.email "sw360-bot@eclipse.org"
  git config --global user.name "SW360 Bot"
  git commit -m "Website build ${JOB_NAME}-${BUILD_NUMBER}"
  git log --graph --abbrev-commit --date=relative -n 5
  git push origin HEAD:master
else
  echo "No change have been detected since last build, nothing to publish"
fi
"""
                    }
                }
            }
        }
    }
}
