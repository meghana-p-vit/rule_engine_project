# Rule Engine Project

![Deployment Status](https://img.shields.io/badge/deployed-success-green)  
**Live Demo:** [https://rule-engine-project.onrender.com](https://rule-engine-project.onrender.com)

## Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Technology Stack](#technology-stack)
4. [Setup and Installation](#setup-and-installation)
5. [API Endpoints](#api-endpoints)
6. [Usage](#usage)
7. [Project Structure](#project-structure)
8. [License](#license)

## Overview

The **Rule Engine Project** is a web-based application that evaluates complex business rules against user-provided data. Using a flexible rule structure, the application takes in criteria such as `age`, `department`, `salary`, and `experience` to determine if specific conditions are met.

## Features

- **Rule Evaluation**: Allows users to input criteria that are evaluated against pre-set rules.
- **Dynamic Output**: Displays results based on rules evaluating to "passed" or "failed."
- **Real-time Processing**: Uses an API-based approach for real-time rule evaluation and immediate feedback.
- **User-friendly Interface**: Simple and responsive frontend for easy data input.

## Technology Stack

- **Backend**: Python with Flask API
- **Frontend**: HTML, CSS, JavaScript
- **Deployment**: Hosted on Render

## Setup and Installation

### Prerequisites

- Python 3.x
- Git

### Installation Steps

1. **Clone the repository**:
   ```bash
   git clone <repository_url>
   cd rule_engine_project
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   docker build -t rule-engine-app .
   docker run -p 8080:80 rule-engine-app

### License

Replace [`<repository_url>`](https://github.com/meghana-p-vit/rule_engine_project) with the actual GitHub URL of your project. This file provides setup, installation, Docker instructions, and usage details for your project.

   
