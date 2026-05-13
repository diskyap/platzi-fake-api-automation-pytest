# platzi-fake-api-automation-pytest
API Automation Testing project using Python and Pytest for Platzi Fake Store API. Demonstrating end-to-end testing, schema validation, and professional QA automation practices


[![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Pytest](https://img.shields.io/badge/pytest-7.4+-green.svg)](https://pytest.org)

## 📋 Table of Contents

- [Features](#-features)
- [Tech Stack](#️-tech-stack)
- [Prerequisites](#-prerequisites)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [How To Run](#-how-to-run)

## ✨ Features

- ✅ **Complete API Coverage** - Tests for Products, Categories, Users, and Auth endpoints
- 🔧 **Easy Configuration** - Environment-based configuration management
- 🎯 **Selective Testing** - Run tests by markers (smoke, regression, products}
- 📊 **HTML Reports** - Beautiful and detailed test execution reports

## 🛠️ Tech Stack

- **Python 3.7+** - Programming language
- **Pytest** - Testing framework
- **Requests** - HTTP client for API calls
- **Python-dotenv** - Environment variable management
- **Pytest-HTML** - HTML report generator
- **JSON Schema** - Response validation

## 📦 Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.7 or higher
- pip (Python package manager)
- git (for cloning the repository)
- virtualenv (recommended for isolated environment)

## 📁 Project Structure
```
└── 📁platzi-fake-api-automation
    └── 📁src
        └── 📁clients
            ├── base_client.py
        └── 📁endpoints
            ├── auth_endpoint.py
        └── 📁models
            ├── auth_model.py
        └── 📁services
            ├── auth_service.py
        └── 📁utils
            ├── helper.py
    └── 📁tests
        └── 📁api
            ├── 📁e2e
            ├── 📁functional
                    └── test_auth_api.py
        └── 📁mock
            └── auth_mock.py
        ├── conftest.py
    ├── pytest.ini
    └── requirements.txt
    └── README.md
```

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/diskyap/platzi-fake-api-automation-pytest.git
cd platzi-fake-api-automation-pytest
```

## 🏃 How to Run

Quick Start (One-time Setup & Run)
```bash
# 1. Clone and enter the project
git clone https://github.com/diskyap/platzi-fake-api-automation-pytest.git
cd platzi-fake-api-automation-pytest

# 2. Setup virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Setup environment variables
cp .env.example .env

# 5. Run all tests
pytest

# 6. Run with Selective by markers
pytest -m 'positive'