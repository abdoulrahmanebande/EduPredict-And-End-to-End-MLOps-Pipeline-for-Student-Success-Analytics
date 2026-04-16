# Student Performance Indicator 🎓

[![Python Version](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/)
[![Docker](https://img.shields.io/badge/docker-enabled-blue.svg)](https://www.docker.com/)
[![AWS](https://img.shields.io/badge/aws-deployed-orange.svg)](https://aws.amazon.com/)
[![CI/CD](https://img.shields.io/badge/github--actions-automated-green.svg)](https://github.com/features/actions)

<br />
<div align="center">
  <a href="https://github.com/your-username/your-repo-name">
    <img src="https://raw.githubusercontent.com/your-username/your-repo-name/main/docs/banner.png" alt="Logo" width="100%" height="auto">
  </a>

  <h3 align="center">End-to-End MLOps Pipeline</h3>

  <p align="center">
    A production-ready Machine Learning application predicting student academic success, featuring automated CI/CD pipelines and containerized deployment.
    <br />
    <a href="#system-architecture"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="#preview">View Demo</a>
    ·
    <a href="https://github.com/your-username/your-repo-name/issues">Report Bug</a>
  </p>
</div>

---

## 📺 Project Preview <a name="preview"></a>

Below is a demonstration of the application in action, showing the web interface and the prediction results.

<div align="center">
  <img src="https://raw.githubusercontent.com/your-username/your-repo-name/main/docs/preview.gif" alt="Project Demo" width="80%">
  <p><i>Live prediction workflow on AWS EC2</i></p>
</div>

---

## 🚀 Overview

This project provides a comprehensive solution for predicting student performance based on demographic and socioeconomic factors. Beyond the model, the focus is on **modern MLOps practices**:
- **Deployment:** Containerized using **Docker** for environment consistency.
- **Infrastructure:** Hosted on **AWS EC2** with images stored in **Amazon ECR**.
- **Automation:** Fully automated **GitHub Actions** workflow for Testing, Building, and Deployment.
- **Efficiency:** Uses **`uv`** for lightning-fast package management and smaller build layers.

## 🏗 System Architecture



1. **Local Development:** Code built in VS Code, containerized with Docker.
2. **Version Control:** Push to GitHub triggers the workflow.
3. **CI/CD:** GitHub Actions builds the image and pushes to Amazon ECR.
4. **Production:** EC2 instance (Self-hosted runner) pulls the latest image and deploys.

## 🛠️ Tech Stack

- **Data Science:** Python 3.12, Scikit-Learn, Pandas, Numpy, Matplotlib.
- **Web Framework:** Flask.
- **Package Manager:** [uv](https://github.com/astral-sh/uv).
- **DevOps:** Docker, GitHub Actions, AWS (EC2, ECR).

## 📂 Project Structure

```text
├── .github/workflows      # CI/CD pipeline definitions
├── artifacts              # Trained model and preprocessor (Serialized .pkl)
├── src                    # Source code
│   ├── components         # Data Ingestion, Transformation, Model Training
│   ├── pipeline           # Train & Predict pipelines
│   └── logger.py          # Custom logging
├── templates              # HTML files for Flask
├── Dockerfile             # Container configuration
├── requirements.txt       # Project dependencies
└── app.py                 # Flask application entry point
