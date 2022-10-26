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
      image: klakegg/hugo:0.93.2-ext-ubuntu
      command:
      - cat
      tty: true
    - name: "jnlp"
      env:
      - name: "HOME"
        value: "/home/jenkins/agent"
"""
        }
    }

    environment {
        PROJECT_NAME = "sw360" // must be all lowercase.
        PROJECT_BOT_NAME = "SW360 Bot" // Capitalize the name
        BRANCH_NAME = "main"
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
                    git branch: "${BRANCH_NAME}",
                        url: "ssh://git@github.com/eclipse/sw360.website.published.git",
                        credentialsId: 'github-bot-ssh'
                }
            }
        }
        stage('Build website with Hugo') {
            steps {
                container('hugo') {
                    dir('hugo') {
                        sh 'mkdir -p themes/docsy'
                        sh 'hugo -b https://www.eclipse.org/sw360/'
                    }
                }
            }
        }
        stage('Push www') {
            steps {
                sh '''
echo "copy and update files"
rm -rf www/* || ls -alF www/
cp -Rvf hugo/public/* www/
'''
                dir('www') {
                    sshagent(['git.eclipse.org-bot-ssh']) {
                        sh """
echo "handling git for branch: ${BRANCH_NAME}"
git config --global user.email "sw360-bot@eclipse.org"
git config --global user.name "SW360 Bot"
git add -A
if ! git diff --cached --exit-code; then
  echo "Changes have been detected, publishing to repo 'www.eclipse.org/sw360'"
  git commit -m "Website build ${JOB_NAME}-${BUILD_NUMBER}"
else
  echo "No change have been detected since last build, nothing to publish"
fi

git log --graph --abbrev-commit --date=relative -n 5
git push origin HEAD:${BRANCH_NAME} ||
  echo "failed to push to ${BRANCH_NAME}"
"""
                    }
                }
            }
        }
    }
}
