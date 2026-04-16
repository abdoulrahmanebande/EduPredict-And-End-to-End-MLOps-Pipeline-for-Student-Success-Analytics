# Student Performance Indicator 🎓

[![Python Version](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/)
[![Docker](https://img.shields.io/badge/docker-enabled-blue.svg)](https://www.docker.com/)
[![AWS](https://img.shields.io/badge/aws-deployed-orange.svg)](https://aws.amazon.com/)
[![CI/CD](https://img.shields.io/badge/github--actions-automated-green.svg)](https://github.com/features/actions)

<br />
<div align="center">
  <a href="https://github.com/abdoulrahmanebande/EduPredict-And-End-to-End-MLOps-Pipeline-for-Student-Success-Analytics">
    <img src="https://raw.githubusercontent.com/abdoulrahmanebande/EduPredict-And-End-to-End-MLOps-Pipeline-for-Student-Success-Analytics/main/docs/banner.png" alt="Logo" width="100%" height="auto">
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
    <a href="https://github.com/abdoulrahmanebande/EduPredict-And-End-to-End-MLOps-Pipeline-for-Student-Success-Analytics/issues">Report Bug</a>
  </p>
</div>

---

## 📺 Project Preview <a name="preview"></a>

Below is a demonstration of the application in action, showing the web interface and the prediction results.

<div align="center">
  <img src="https://raw.githubusercontent.com/abdoulrahmanebande/EduPredict-And-End-to-End-MLOps-Pipeline-for-Student-Success-Analytics/main/docs/preview.gif" alt="Project Demo" width="80%">
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
├── .github/workflows/main.yaml    # CI/CD Pipeline
├── artifacts/              # Model.pkl and Preprocessor.pkl
├── docs/                   # Banner and Preview GIF
├── src/
│   ├── components/         # data_ingestion.py, data_transformation.py, model_trainer.py
│   ├── notebooks/          # Research folder
│   │   ├── data/
│   │   │   └── stud.csv
│   │   ├── eda for student performance indicator.ipynb
│   │   └── model training.ipynb
│   ├── pipeline/           # train_pipeline.py, predict_pipeline.py
│   ├── exception.py        # Custom Exception handling
│   ├── logger.py           # Logging configuration
│   └── utils.py            # Common utility functions (e.g., save_object, evaluate_models)
├── templates/              # Flask HTML files
├── static/              # Assets like icons, images, etc
├── app.py                  # Entry point
├── Dockerfile
├── requirements.txt
├── setup.py                # Building the project into a package
└── README.md  
``` 

## ⚙️ Installation & Setup

### 1. Prerequisites
Ensure you have **Docker** installed on your system. If you are on Windows, ensure **WSL2** or **Hyper-V** is enabled.

### 2. Local Execution
Follow these steps to run the application locally in a containerized environment:

**Clone the repository:**
```bash
git clone (https://github.com/abdoulrahmanebande/EduPredict-And-End-to-End-MLOps-Pipeline-for-Student-Success-Analytics.git)
cd EduPredict-And-End-to-End-MLOps-Pipeline-for-Student-Success-Analytics
```

**Build the Docker image:**
```bash
docker build -t student-success-analytics .
``` 

**Run the container:**
```bash
docker run -p 5000:5000 student-success-analytics
``` 

## 💡 Usage

Once the container is running:
  1. Open your web browser.
  2. Navigate to http://localhost:5000
  3. Input the student data (Gender, Ethnicity, Scores, etc.) into the form. 
  4. Click Predict to see the model's estimated result.


## 📜 License 

Distributed under the MIT License. See LICENSE for more information. 


<br />

<div align="center">
<p>Developed with 🚀 by <b>BANDE Abdoul-Rahmane</b></p>
<a href="www.linkedin.com/in/bandeabdoulrahmane">
<img src="https://commons.wikimedia.org/wiki/File:LinkedIn_logo_initials.png" alt="LinkedIn">
</a>
</div>