// See documentation on: https://wiki.eclipse.org/Jenkins#How_to_build_my_project.27s_website_with_Jenkins.3F

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
    - name: "jnlp"
      volumeMounts:
      - mountPath: /home/jenkins/.ssh
        name: volume-known-hosts
      env:
      - name: "HOME"
        value: "/home/jenkins"
    - name: hugo
      image: klakegg/hugo:0.111.3-ext-ubuntu
      command:
      - cat
      tty: true
  volumes:
  - configMap:
      name: known-hosts
    name: volume-known-hosts
"""
        }
    }

    environment {
        PROJECT_NAME = "sw360" // must be all lowercase.
        PROJECT_BOT_NAME = "SW360 Bot" // Capitalize the name
        BRANCH_NAME = "main"
    }

    triggers {
      pollSCM('H/10 * * * *')
    }

    options {
        buildDiscarder(logRotator(numToKeepStr: '5'))
        checkoutToSubdirectory('hugo')
    }

    stages {
      stage('Checkout www repo') {
          steps {
              dir('www') {
                sshagent(['github-bot-ssh']) {
                  sh '''
                    git clone git@github.com:eclipse-sw360/sw360.website.published.git .
                    git checkout ${BRANCH_NAME}
                  '''
              }
          }
        }
      }

      stage('Build main website with Hugo') {
        when {
          branch 'main'
        }
        steps {
            container('hugo') {
                dir('hugo') {
                    sh 'mkdir -p themes/docsy'
                    sh 'hugo --minify -b https://www.eclipse.org/sw360/'
                }
            }
        }
      }

      stage('Build staging website with Hugo') {
        when {
          branch 'staging'
        }
        steps {
            container('hugo') {
                dir('hugo') {
                    sh 'mkdir -p themes/docsy'
                    sh 'hugo --minify -b https://www.eclipse.org/${PROJECT_NAME}/'
                }
            }
        }
      }

      stage('Push www') {
        when {
          anyOf {
            branch "main"
            branch "staging"
          }
        }
        steps {
          sh 'rm -rf www/* && cp -Rvf hugo/public/* www/'
          dir('www') {
            sshagent(['github-bot-ssh']) {
              sh '''
              git add -A
              if ! git diff --cached --exit-code; then
                echo "Changes have been detected, publishing to repo 'www.eclipse.org/${PROJECT_NAME}'"
                git config user.email "${PROJECT_NAME}-bot@eclipse.org"
                git config user.name "${PROJECT_BOT_NAME}"
                git commit -m "Website build ${JOB_NAME}-${BUILD_NUMBER}"
                git log --graph --abbrev-commit --date=relative -n 5
                git push origin HEAD:${BRANCH_NAME}
              else
                echo "No changes have been detected since last build, nothing to publish"
              fi
              '''
            }
          }
        }
      }
    }
  }

