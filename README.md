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

This guide provides instructions to set up and run the SW360 website locally using Docker and Hugo.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation Steps](#installation-steps)
- [Troubleshooting](#troubleshooting)
- [Project Structure](#project-structure)
- [Contributors](#contributors)
- [Contributing](#contributing)
- [License](#license)

---

## Prerequisites

Before starting, ensure the following tools are installed on your system:

1. **[Docker Desktop](https://www.docker.com/products/docker-desktop/)**
    - **Windows/macOS**: Download and install from the official Docker website.
    - **Linux**: Install via your package manager (e.g., `sudo apt install docker.io` on Ubuntu), then start the service with `sudo systemctl start docker`.
    - **Verify**: Run `docker --version` to confirm installation.

2. **Bash Shell**
    - **macOS/Linux**: Bash is included by default in the terminal.
    - **Windows**: Use Git Bash (installed with Git) or Windows Subsystem for Linux (WSL).
    - **Verify**: Run `bash --version` to ensure Bash is available.

3. **[Go](https://go.dev/doc/install)** (Optional)
    - Required only for Hugo development or customization (e.g., building from source).
    - Follow the OS-specific installation instructions on the Go website.
    - **Verify**: Run `go version` to check the installation.

---

## Installation Steps

Follow these steps to clone the repository and serve the SW360 website locally.

### Step 1: Clone the Repository

1. Clone the project repository, replacing `{{your_username}}` with your GitHub username:
    ```bash
    git clone [https://github.com/](https://github.com/){{your_username}}/sw360.website.git
    ```
2. Navigate into the project directory:
    ```bash
    cd sw360.website
    ```

### Step 2: Set Up the Local Server

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

3. **Docker Daemon Not Running**

    **Issue:** `Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the daemon running?` or similar errors
    **Solution:**
    1. Ensure the Docker daemon is active:
        - **macOS/Windows**: Open Docker Desktop and wait for it to fully start (check the status in the bottom left corner).
        - **Linux**: Start the daemon manually with:
            ```bash
            sudo systemctl start docker
            ```
    2. Verify the daemon is running:
        ```bash
        docker info
        ```
    3. If the issue persists, restart Docker:
        - **Linux**: `sudo systemctl restart docker`
        - **macOS/Windows**: Restart Docker Desktop from the system tray.
4. **Port Already in Use**

    **Issue:** Error: `listen tcp 0.0.0.0:1313: bind: address already in use` (indicating port 1313 is occupied)
    **Solution:**
    1. Identify the process using the port:
        ```bash
        lsof -i :1313  # On macOS/Linux
        netstat -aon | findstr :1313  # On Windows (Command Prompt)
        ```
    2. Stop the conflicting process:
        - **macOS/Linux**: Kill the process using `kill -9 <PID>` (replace `<PID>` with the process ID from `lsof`).
        - **Windows**: Use `taskkill /PID <PID> /F` (replace `<PID>` with the process ID from `netstat`).




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