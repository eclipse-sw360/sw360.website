# SW360 Website

The SW360 website is built using the **Hugo static site generator**. It serves as the main documentation site for SW360 and is published at [eclipse.org/sw360](https://www.eclipse.org/sw360). The site is automatically built and deployed using a **Jenkins job** configured in the repository.

## Repository & Contribution Guide

### **Repository Location**
- **GitHub Repository:** [eclipse/sw360.website](https://github.com/eclipse/sw360.website)
- **Staging Repository:** [staging.eclipse.org/sw360](https://staging.eclipse.org/sw360) (Requires Eclipse Foundation credentials)

### **How to Contribute**
To add content or make improvements to the website:
1. **Fork & Clone** the repository:
   ```sh
   git clone https://github.com/eclipse/sw360.website.git
   cd sw360.website
   ```
2. **Make Your Changes** in the appropriate Markdown files.
3. **Test Locally** using Docker (see instructions below).
4. **Commit & Push** your changes to the staging branch for review.
5. **Submit a Pull Request (PR)** to the `main` branch once validated.

The page is automatically built and deployed whenever changes are merged into the `main` branch.

## Jenkins Build Process
- **Jenkins Instance:** [Eclipse Jenkins for SW360](https://jenkins.eclipse.org/sw360/job/sw360.website/)
- The Jenkins job checks for updates **every 15 minutes**.
- If changes are detected, it:
  1. Runs the Hugo build.
  2. Pushes the generated static HTML files to `git.eclipse.org/c/www.eclipse.org/sw360.git`.
  3. Deploys the content to the Eclipse Foundation’s static webspace.

## Local Development & Testing with Docker
If you want to test your changes locally before pushing:

### **Prerequisites**
- Install [Docker](https://docs.docker.com/get-docker/) (Ensure your system meets the required version).

### **Run the Local Server**
```sh
bash docker_serve_local.sh
```
Then open your browser and navigate to:
```sh
http://localhost:1313/sw360
```

### **Stopping the Local Server**
Press `Ctrl + C` in the terminal to stop the local server.

## Troubleshooting
### **Common Issues & Fixes**
#### **1. Site Not Found (404 Error)**
- Ensure you are visiting `http://localhost:1313/sw360` and **not** `http://localhost:8080/`.
- Check if the `docker_serve_local.sh` script ran successfully.
- Run `docker ps` to verify the container is running.

#### **2. Changes Not Reflecting**
- Clear browser cache or open in an incognito window.
- Restart the local server using `bash docker_serve_local.sh`.

## Additional Resources
- **Hugo Documentation:** [https://gohugo.io/documentation/](https://gohugo.io/documentation/)
- **Eclipse Foundation Contribution Guide:** [https://www.eclipse.org/contribute/](https://www.eclipse.org/contribute/)

---

### **Maintainers**
For any issues or questions, reach out to the SW360 maintainers through the GitHub repository’s issue tracker.

