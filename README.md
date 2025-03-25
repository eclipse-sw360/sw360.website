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
    ·
    <a href="https://eclipse.dev/sw360/docs/">Documentation</a>
    ·
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

# 👋 Welcome to the SW360 Website!

This website serves as the central hub for the SW360 project. It is built using the following technologies:

* **Hugo:** A fast and flexible static site generator.
* **Docsy:** A Hugo theme optimized for documentation.

The source code for this website is open-source and available on GitHub: [https://github.com/eclipse-sw360/sw360.website](https://github.com/eclipse-sw360/sw360.website).

**Website Publication Process**

The website is published at [eclipse.org/sw360](https://eclipse.org/sw360) through an automated process:

1.  Changes are made to the website's content by contributing to the GitHub repository.
2.  A Jenkins job, configured in the `Jenkinsfile` within the repository, builds the site using Hugo.
3.  The generated static HTML files are pushed to `git.eclipse.org/c/www.eclipse.org/sw360.git`.
4.  Another job fetches these files and copies them to the Eclipse Foundation's webspace.

Jenkins checks for changes in the repository every 15 minutes. A staging area is also available at `staging.eclipse.org/sw360` (protected by Eclipse Foundation credentials) for previewing changes before they go live.

# Setting Up the SW360 Website Locally

This guide explains how to set up and run the SW360 website locally using Docker and Hugo with the Docsy theme. This setup allows for local development and testing. These instructions are compatible with **Windows**, **macOS**, and **Linux**.

## Prerequisites

Before starting, ensure the following tools are installed on your system:

1.  **[Docker Desktop](https://www.docker.com/products/docker-desktop/)**
    * **Windows/macOS**: Download and install from the official site.
    * **Linux**: Install via your package manager (e.g., `sudo apt install docker.io` on Ubuntu) and start the service (`sudo systemctl start docker`).
    * Verify: `docker --version`
2.  **[Git](https://git-scm.com/downloads)**
    * **Windows/macOS**: Install using the official installer.
    * **Linux**: Install via your package manager (e.g., `sudo apt install git` on Ubuntu).
    * Verify: `git --version`
3.  **[Hugo (Extended Version)](https://gohugo.io/installation/)**
    * Install the **extended version** of Hugo (required for SCSS support):
        * **Windows**: Use Chocolatey (`choco install hugo-extended`) or download from [releases](https://github.com/gohugoio/hugo/releases).
        * **macOS**: Use Homebrew (`brew install hugo`).
        * **Linux**: Download the extended version from [releases](https://github.com/gohugoio/hugo/releases) or use your package manager if available.
    * Verify: `hugo version` (ensure "extended" appears in the output).
4.  **[Go](https://go.dev/doc/install)** (optional)
    * Required only for Hugo development or customization.
    * Install following OS-specific instructions.
    * Verify: `go version`

## Installation Steps

Follow these steps to set up and serve the SW360 website locally:

### 1. Clone the Repository

* Clone the project repository, replacing `{{your_username}}` with your GitHub username:

    ```bash
    git clone [https://github.com/](https://github.com/){{your_username}}/sw360.website.git
    ```

* Navigate into the project directory:

    ```bash
    cd sw360.website
    ```

### 2. Set Up the Docsy Theme

* Create a `themes` directory to store the theme:

    ```bash
    mkdir themes
    ```

* Enter the `themes` directory:

    ```bash
    cd themes
    ```

* Clone the Docsy theme from Google’s repository:

    ```bash
    git clone [https://github.com/google/docsy.git](https://github.com/google/docsy.git)
    ```

* Navigate into the `docsy` directory:

    ```bash
    cd docsy
    ```

* Switch to version `v0.3.0` to ensure compatibility:

    ```bash
    git checkout v0.3.0
    ```

* Return to the project root directory:

    ```bash
    cd ../../
    ```

### 3. Serve the Site Locally with Docker

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