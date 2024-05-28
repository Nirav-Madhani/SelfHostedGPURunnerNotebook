
# Self-hosted GitHub actions GPU runners using cloud Jupyter notebooks

## About

This project enables the use of free cloud-based Jupyter notebooks as runners for GitHub Actions, addressing the common challenge of setting up CI/CD pipelines for machine learning projects. Cloud based GPU runners for CI/CD are often costly and computers with GPU are expensive, which can be a barrier for many developers.

By integrating these cloud-based Jupyter notebook environments with GitHub Actions, this repository allows you to run workflows with GPU acceleration without additional costs. This ensures that your machine learning projects can maintain continuous integration and deployment, leveraging the power of free GPU resources.

Key Features:
- **Enables Free GPU Access**: Utilize free cloud-based Jupyter notebooks for your CI/CD pipelines.
- **Easy Integration**: Connect your GitHub repository with cloud-based Jupyer Notebooks easily.
- **Student-Friendly**: Avoid the expenses associated with cloud GPU VMs or local GPU machines. 

This project aims to streamline the development process for machine learning practitioners, providing an accessible and efficient solution for CI/CD workflows. Future updates will include support for additional platforms, and a full fledge sample workflow.

## Supported Notebooks
- [x] Colab
- [ ] Kaggle (Colab Notebook can be used with slight modifications)

## Setting Up Runner on Github
1. Open your repo on Github, copy and paste its url into  `<github repo url>` placeholder and Click Settings
2. Click `Runners` in `Actions`
3. Click `New Self Hosted Runner`
![Creating Runner 1](image.png)
4. Set `Runner Image` to `Linux` and
5.  `Architecture` to `x64`
![Creating Runner 2](image-1.png)
6. Verify that runner version in Notebook matches with latest from GitHub. Update notebook to match version if required.

![Creating Runner 3](image-2.png)
7. Copy the token as shown in Image and Paste it in notebook in `<token copied in step 7>` placeholder
8. Finally configure tensorboard path. It will be somewhere within `_work` directory inside runner depending on your code.
## How to Run Notebook

If you are running notebook first time after setting up runner:-

* Run all cells sequentially except for `Next Time Block`

else:-

* Run all cells sequentially except `First Time` Block

## Intended Audience
This repository is primarily intended for students and learners with limited access to GPUs, providing GPU resources for educational and learning purposes.

## Complying with Terms of Service

### Colab
To ensure compliance with Google Colab's terms of service while using it for CI/CD workflows, here are some general guidelines:

- **Usage Limits**: Do not use Colab for long-running processes or heavy workloads. Colab is intended for interactive use, and extended sessions can violate usage policies.
- **Resource Management**: Be mindful of resource consumption. Avoid excessive GPU usage or running multiple sessions simultaneously.
- **Code of Conduct**: Follow the community guidelines and Google's code of conduct for appropriate use of Colab services.

**Note:** These instructions do not necessarily suffice to ensure full compliance with Colab's terms of service. Always review the latest terms and policies directly from Google Colab. [Google Colab FAQ](https://research.google.com/colaboratory/faq.html)

### ⚠️ **Important: Avoid Using Self-Hosted Runners for Public Repositories**

When managing CI/CD workflows in public repositories, it's crucial to avoid using self-hosted runners, ***especially for workflows triggered by pull requests from forks***. Using self-hosted runners in this context poses significant security risks:

1. **Exposure to Malicious Code**: Self-hosted runners are vulnerable to attacks from malicious pull requests. An attacker can modify a workflow file in their fork to execute harmful code on your self-hosted runner, potentially stealing secrets or damaging your infrastructure [GitHub Docs](https://docs.github.com/en/actions/security-guides/security-hardening-for-github-actions), [Legit Security](https://www.legitsecurity.com/blog/securing-your-ci-cd-pipeline-exploring-the-dangers-of-self-hosted-agents).

2. **Access to Sensitive Information**: Self-hosted runners might have access to sensitive data and internal networks. If compromised, an attacker can exploit this access, leading to data breaches or further attacks on your network [Legit Security](https://www.legitsecurity.com/blog/securing-your-ci/cd-pipeline-exploring-the-dangers-of-self-hosted-agents).

3. **Cryptocurrency Mining**: Attackers can exploit self-hosted runners to run cryptocurrency mining operations, violating terms of service and leading to increased costs and resource depletion. This abuse can also result in poorer performance for legitimate users of the service [Cloud Security Alliance](https://cloudsecurityalliance.org/blog/2022/02/28/massive-cryptomining-operation-using-github-actions/).

4. **Theft of Google Drive and Other Google Data**: When using self-hosted runners on platforms like Google Colab, attackers can potentially access and steal data from your Google Drive and other linked Google services, leading to significant data breaches and privacy violations.

**References**:
- [GitHub Docs: Security hardening for GitHub Actions](https://docs.github.com/en/actions/security-guides/security-hardening-for-github-actions)
- [Legit Security: Securing Your CI/CD Pipeline](https://www.legitsecurity.com/blog/securing-your-ci/cd-pipeline-exploring-the-dangers-of-self-hosted-agents)
- [Cloud Security Alliance: Massive Cryptomining Operation Using GitHub Actions](https://cloudsecurityalliance.org/blog/2022/02/28/massive-cryptomining-operation-using-github-actions/)
- [GitGuardian: GitHub Actions Security Best Practices](https://blog.gitguardian.com/github-actions-security-best-practices/)


## Disclaimer

THE WORK IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE WORK OR THE USE OR OTHER DEALINGS IN THE WORK.
