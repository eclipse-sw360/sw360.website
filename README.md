<p align="center">
  <a href="https://eclipse.dev/sw360/">
    <img src="static/img/logos/logo_full.svg" alt="SW360 Logo" width="450">
  </a>
  <h1 align="center">sw360.website</h1>
  <p align="center">
    <a href="https://eclipse.dev/sw360/"><strong>Learn more »</strong></a>
    <br />
    <br />
    <a href="https://sw360chat.slack.com/">Discussions</a> ·
    <a href="https://eclipse.dev/sw360/">Website</a> ·
    <a href="https://github.com/eclipse-sw360/sw360.website/issues">Issues</a> ·
    <a href="https://eclipse.dev/sw360/docs/">Documentation</a> ·
    <a href="https://eclipse.dev/sw360/gsoc/">GSoC</a>
  </p>
</p>

<p align="left">
  <a href="https://github.com/eclipse-sw360/sw360.website/graphs/contributors" alt="SW360 GitHub Contributors">
    <img src="https://img.shields.io/github/contributors/eclipse-sw360/sw360.website?color=orange" />
  </a>
  <a href="https://github.com/eclipse-sw360/sw360.website/issues?q=is%3Aopen" alt="SW360 Website Open Issues">
    <img src="https://img.shields.io/github/issues/eclipse-sw360/sw360.website?color=%23DDDD22&label=open%20issues" />
  </a>
  <a href="https://www.repostatus.org/#active" alt="Repo Status">
    <img src="https://www.repostatus.org/badges/latest/active.svg" />
  </a>
  <a href="https://sw360chat.slack.com/" alt="Join SW360 Slack">
    <img src="https://img.shields.io/badge/Slack-Join%20SW360-yellow?logo=slack" />
  </a>
</p>

<p>
  The website is based on the Hugo static page generator. All relevant source files can be found at <a href="https://github.com/eclipse/sw360.website">github/sw360.website</a>.
  The page is published at <a href="https://eclipse.org/sw360">eclipse.org/sw360</a> and built with a Jenkins job, which is configured in a Jenkins file in the repository of the website.
</p>

<p>
  If you want to add content to the page, please checkout the git repository <a href="https://github.com/eclipse/sw360.website.git">sw360.website.git</a> and add your content.
</p>

<p>
  The page will be built as soon as you push to the upstream main branch. There is also a staging area at the Eclipse Foundation page at <a href="https://staging.eclipse.org/sw360">staging.eclipse.org/sw360</a>, which is protected by your Eclipse Foundation user credentials and filled with content found at the staging branch in <a href="https://github.com/eclipse/sw360.website">sw360.website repository</a>.
  If you want to check out your changes first, just push to the staging branch. The content is published the same way as with the main branch.
</p>

<p>
  The Jenkins instance is operated by the Eclipse Foundation and can be found here: <a href="https://jenkins.eclipse.org/sw360/job/sw360.website/">Jenkins SW360 Website</a>.
  The result of the Jenkins build is pushed to: <a href="http://git.eclipse.org/c/www.eclipse.org/sw360.git">git.eclipse.org/sw360</a>.
</p>

<p>
  The Jenkins job looks every 15 minutes for changes in the repository. If it detects changes, it will start the Hugo build and copy the generated static HTML files to git.eclipse.org. From there, another job fetches the files and copies them to the actual static webspace of the Eclipse Foundation.
</p>

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation Steps](#installation-steps)
- [Troubleshooting](#troubleshooting)
- [Project Structure](#project-structure)
- [Contributors](#contributors)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

Ensure you have the following installed before proceeding:

1.  **[Docker Desktop](https://www.docker.com/products/docker-desktop/)**
    * **Windows/macOS**: Download and install from the official site.
    * **Linux**: Install via your package manager (e.g., `sudo apt install docker.io` on Ubuntu) and start the service (`sudo systemctl start docker`).
    * Verify: `docker --version`
2. **Bash (Available by default on macOS and Linux; for Windows, use Git Bash or WSL)**
    * **macOS/Linux**: Bash is available by default in the terminal.
    * **Windows**: You can use Git Bash or install Windows Subsystem for Linux (WSL) to get Bash.
    * Verify: Run `bash --version` to ensure Bash is installed.
3.  **[Go](https://go.dev/doc/install)** (optional)
    * Required only for Hugo development or customization.
    * Install following OS-specific instructions.
    * Verify: `go version`

## Installation Steps

Follow these steps to set up and serve the SW360 website locally:

### Clone the Repository

* Clone the project repository, replacing `{{your_username}}` with your GitHub username:

    ```bash
    git clone https://github.com/{{your_username}}/sw360.website.git
    ```

* Navigate into the project directory:

    ```bash
    cd sw360.website
    ```

### Serve the Site Locally with Docker

* Ensure Docker is running:
    * **Windows/macOS**: Launch Docker Desktop.
    * **Linux**: Start the service with `sudo systemctl start docker`.

* Run the provided script to build and serve the site:

    ```bash
    bash docker_serve_local.sh
    ```

* **Windows Users (Git Bash/WSL):**
    * Make the script executable if needed:

        ```bash
        chmod +x docker_serve_local.sh
        ```

    * Then run:

        ```bash
        ./docker_serve_local.sh
        ```

* Once running, access the site at `http://localhost:1313` (confirm the port in the script output).

**Note:** The local development environment uses Hugo's built-in live reload functionality. Any changes made to the site's content or layout will be automatically reflected in your browser in real-time. This allows for rapid iteration and immediate visual feedback during development.

## Troubleshooting

### Docker is not running

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

## Contributors

Thanks to all the amazing contributors to this project:

[![Contributors](https://contrib.rocks/image?repo=jeclipse-sw360/sw360.website)](https://github.com/eclipse-sw360/sw360.website/graphs/contributors)

Want to join the list? Check out our [Contributing Guide](CONTRIBUTING.md) to get started!

## Contributing

We’re thrilled to have you join our open-source community! Whether you’re a developer, designer, writer, or enthusiast, your contributions can make a big impact on the SW360 website project. We’ve created a detailed **[CONTRIBUTING.md](CONTRIBUTING.md)** file to guide you, but here’s a quick overview of how you can get involved:

* **Report Bugs & Request Features**
    Found something broken or have an idea to make the project better? Open an issue on our [GitHub Issues page](https://github.com/eclipse-sw360/sw360.website/issues) with clear details to help us address it quickly.

* **Contribute Code**
    Want to fix a bug or add a feature? Fork the repository, make your changes, and submit a pull request. Check [CONTRIBUTING.md](CONTRIBUTING.md) for coding guidelines and best practices.

* **Improve Documentation**
    Clear docs are key to a thriving project. Help us refine setup instructions, add examples, or clarify existing content by submitting updates to this file or others.

* **Enhance the User Interface**
    Have design skills? Improve the site’s look and feel—whether it’s tweaking the Docsy theme, optimizing layouts, or suggesting accessibility upgrades.

### Connect with the SW360 Community

We’re excited to connect with you! Whether you have questions, feedback, or simply want to chat about the SW360 website, here’s how to reach out and join our community:

* **GitHub Issues**
    For bug reports, feature requests, or project-related questions, please [open an issue](https://github.com/eclipse-sw360/sw360.website/issues) on our repository. This is the fastest way to get a tracked and timely response!
* **Slack**
    Join us on Slack for real-time collaboration, quick questions, or to connect with contributors:
    <a href="https://sw360chat.slack.com/" target="_blank"><img align="center" src="https://img.icons8.com/color/48/null/slack-new.png" alt="SW360 Slack" height="30" width="40" style="margin-right: 5px;" /></a>

* **Email**
    For private inquiries, collaboration ideas, or direct feedback, email us at:
    <a href="mailto:sw360-dev@eclipse.org"><img align="center" src="https://img.icons8.com/color/48/null/gmail.png" alt="SW360 Email" height="30" width="40" style="margin-right: 5px;" /></a>

## License

The contents of this repository are licensed under the Eclipse Public License 2.0 (EPL-2.0). See [LICENSE](./LICENSE).
