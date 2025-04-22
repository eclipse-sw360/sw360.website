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
All relevant source files can be found at github/sw360.website (https://github.com/eclipse/sw360.website). 
The page is published at eclipse.org/sw360 and build with a jenkins job, which is configured in a jenkins file in the repository of the website.

If you want to add content to the page, please checkout the git repository (https://github.com/eclipse/sw360.website.git) and add your content.

The page will be build as soon as you push to upstream main branch. There is also a staging area at the Eclipse Foundation page at staging.eclipse.org/sw360, which is protected by your Eclipse Foundation user credentials and filled with the content that is fund at the staging branch in https://github.com/eclipse/sw360.website. If you want to check out your changes first, just push to the staging branch. The content is published the same way as with the main branch.

The jenkins instance is operated by the Eclipse Foundation and can be found here: https://jenkins.eclipse.org/sw360/job/sw360.website/.
The result of the jenkins build is pushed to: http://git.eclipse.org/c/www.eclipse.org/sw360.git.

The jenkins jobs looks every 15 minutes after changes on the repository. If it detects changes it will start the hugo build and copy the generated static html files to git.eclipse.org. From there another job fetches the files and copies them to the actual static webspace of the Eclipse Foundation.

# SW360 Website Setup Guide

This guide provides instructions to set up and run the SW360 website locally using Docker.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation Guide Using Docker](#installation-guide-using-docker)
- [Troubleshooting](#troubleshooting)
- [Project Structure](#project-structure)
- [Support](#support)

---

## Prerequisites

Before you begin, make sure [Docker](https://docs.docker.com/get-docker/) is installed and running on your system.

- **Verify installation** by running:
    ```bash
    docker --version
    ```

## Installation Guide Using Docker

### Set Up the Local Server

#### Linux/macOS Setup

1. Open a terminal and ensure you’re in the project root directory.
2. Run the Docker script to start the local server:
    ```bash
    bash docker_serve_local.sh
    ```
3. Once the server starts, open your browser and visit:
    ```text
    http://localhost:1313/sw360
    ```
4. Changes to the code will automatically reload in the browser.

#### Windows Setup

1. Ensure Docker Desktop is Running: Open Docker Desktop and confirm the Docker engine is active.
2. Choose one of the following methods:

**1: Using Git Bash**

1. Make the script executable (if needed):
    ```bash
    chmod +x docker_serve_local.sh
    ```
2. Run the script:
    ```bash
    bash docker_serve_local.sh
    ```

**2: Using WSL**

1. Ensure WSL is installed and Docker Desktop is configured for WSL 2 integration:
    - In Docker Desktop, go to Settings > Resources > WSL Integration and enable your Linux distribution.
2. Make the script executable (if needed):
    ```bash
    chmod +x docker_serve_local.sh
    ```
3. Run the script:
    ```bash
    bash docker_serve_local.sh
    ```
4. Once running, access the site at `http://localhost:1313/sw360` (check the script output for the exact port).

**Note:** The Hugo development server includes live reload functionality. Any changes to content or layouts will update in real-time, enabling rapid development and testing.

## Troubleshooting

1. **Permission Denied**

    **Issue:** Permission denied when running `docker_serve_local.sh`
    **Solution:**
    1. Grant execute permissions:
        ```bash
        chmod +x docker_serve_local.sh
        ```
    2. Retry:
        ```bash
        bash docker_serve_local.sh
        ```

2. **Line Ending Errors**

    **Issue:** `$'r': command not found` (common when the script has Windows-style line endings)
    **Solution:**
    1. Convert the script to Unix format:
        ```bash
        dos2unix docker_serve_local.sh
        ```
    2. Run it again:
        ```bash
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
