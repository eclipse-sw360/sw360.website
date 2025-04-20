<p align="center">
  <a href="https://eclipse.dev/sw360/">
   <img src="static/img/logos/logo_full.svg" alt="SW360 Logo" width="450">
  </a>
    <h1 align="center">sw360.website</h1>
  
  <p align="center">
    <a href="https://eclipse.dev/sw360/"><strong>Learn more »</strong></a>
    <br />
    <br />
    <a href="https://sw360chat.slack.com/">Discussions</a>
    ·
    <a href="https://eclipse.dev/sw360/">Website</a>
    ·
    <a href="https://github.com/eclipse-sw360/sw360.website/issues">Issues</a>
    .
    <a href="https://eclipse.dev/sw360/docs/">Documentation</a>
    ·
    <a href="https://eclipse.dev/sw360/gsoc/">GSoC</a>
  </p>
</p>

The website is based on the Hugo static page generator. 
All relevant source files can be found at [github.com/eclipse/sw360.website](https://github.com/eclipse/sw360.website).
The page is published at eclipse.org/sw360 and built with a Jenkins job, which is configured in a jenkins file in the repository of the website.

If you want to add content to the page, please checkout the git repository (https://github.com/eclipse/sw360.website.git) and add your content.

The page will be build as soon as you push to upstream main branch. There is also a staging area at the Eclipse Foundation page at staging.eclipse.org/sw360, which is protected by your Eclipse Foundation user credentials and filled with the content that is found at the staging branch in https://github.com/eclipse/sw360.website. If you want to check out your changes first, just push to the staging branch. The content is published the same way as with the main branch.

The Jenkins instance is operated by the Eclipse Foundation and can be found here: https://jenkins.eclipse.org/sw360/job/sw360.website/.
The result of the Jenkins build is pushed to: http://git.eclipse.org/c/www.eclipse.org/sw360.git.

The Jenkins job checks for changes in the repository every 15 minutes.If it detects changes it will start the Hugo build and copy the generated static html files to git.eclipse.org. From there another job fetches the files and copies them to the actual static webspace of the Eclipse Foundation.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Local Development Using Docker](#local-development-using-docker)
- [Troubleshooting](#troubleshooting)
- [Project Structure](#project-structure)
- [Support](#support)

## Prerequisites

Ensure you have the following installed before proceeding:

- **Docker** (Check installation by running `docker --version` in the terminal)
- **Bash** (Available by default on macOS and Linux; for Windows, use Git Bash or WSL)

## Local Development Using Docker

If you have Docker installed on your system, you can quickly set up a local development environment and test changes in real time.

## Setting Up the Local Server

1. Open a terminal and navigate to the project root directory.

2. Run the following command to start the local server:

   ```sh
   bash docker_serve_local.sh
   ```

3. Once the server starts, open your browser and visit:

   ```sh
   http://localhost:1313/sw360
   ```

4. Any changes made to the code will automatically reflect in the browser.

## Troubleshooting

### 1. Docker is not running

**Issue:** `bash: docker: command not found`

**Solution:**

- Ensure Docker is installed and running.
- On macOS or Windows, open Docker Desktop.
- On Linux, start Docker with:
  ```sh
  sudo systemctl start docker
  ```

### 2. Permission issues running the script

**Issue:** `Permission denied` error when executing `docker_serve_local.sh`. 

**Solution:**

- Give execution permission to the script:
  ```sh
  chmod +x docker_serve_local.sh
  ```
- Run it again:
  ```sh
  bash docker_serve_local.sh
  ```

## Project Structure
```
sw360.website/
├── content/               # Website content (pages, posts, etc.)
├── layouts/               # Custom layout templates
├── static/                # Static assets (images, CSS, JS)
├── config.toml            # Hugo configuration
├── docker_serve_local.sh  # Docker development script
└── README.md              # Project documentation and contribution guidelines
```
## Support

- Report issues: [GitHub Issues](https://github.com/eclipse/sw360.website/issues)
- Community: [SW360 Mailing List](https://dev.eclipse.org/mailman/listinfo/sw360-dev)
- Documentation: [SW360 Documentation](https://eclipse.dev/sw360/docs/)
