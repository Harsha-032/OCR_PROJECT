# 📄 Receipt Processor - Full Stack Application

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)
![Tesseract](https://img.shields.io/badge/Tesseract-3D8FC4?style=for-the-badge&logo=tesseract&logoColor=white)

<div align="center">
  <img src="https://github.com/yourusername/receipt-processor/raw/main/screenshots/dashboard.png" width="45%">
  <img src="https://github.com/yourusername/receipt-processor/raw/main/screenshots/upload.png" width="45%">
</div>

## 🚀 Overview

A full-stack Django application for processing receipts and bills with OCR capabilities. Extracts key information (vendor, date, amount) from uploaded receipts and provides spending insights.

## ✨ Features

- **Multi-format Support**: 
  ![PDF](https://img.shields.io/badge/PDF-FF0000?style=flat-square&logo=adobe-acrobat-reader&logoColor=white)
  ![Image](https://img.shields.io/badge/Images-FFA500?style=flat-square&logo=image&logoColor=white)
  ![Text](https://img.shields.io/badge/Text-000000?style=flat-square&logo=text&logoColor=white)

- **Smart Data Extraction**:
  - Vendor identification
  - Date parsing
  - Amount detection
  - Category classification

- **Powerful Analytics**:
  - Total spend tracking
  - Vendor breakdowns
  - Time-series trends
  - Category distributions

- **Intuitive UI**:
  - Responsive Bootstrap design
  - Interactive tables
  - Modal confirmations

## 🛠️ Technology Stack

| Component        | Technology |
|------------------|------------|
| **Backend**      | ![Django](https://img.shields.io/badge/Django-092E20?style=flat-square&logo=django&logoColor=white) |
| **Frontend**     | ![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=flat-square&logo=bootstrap&logoColor=white) |
| **Database**     | ![SQLite](https://img.shields.io/badge/SQLite-07405E?style=flat-square&logo=sqlite&logoColor=white) |
| **OCR Engine**   | ![Tesseract](https://img.shields.io/badge/Tesseract-3D8FC4?style=flat-square&logo=tesseract&logoColor=white) |
| **File Handling**| ![PDF](https://img.shields.io/badge/PDF-FF0000?style=flat-square&logo=adobe-acrobat-reader&logoColor=white) ![Image](https://img.shields.io/badge/Images-FFA500?style=flat-square&logo=image&logoColor=white) |

## 📦 Installation

### Prerequisites
- Python 3.8+
- Tesseract OCR ([Installation Guide](https://github.com/tesseract-ocr/tesseract))

```bash
# Clone the repository
git clone https://github.com/yourusername/receipt-processor.git
cd receipt-processor

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create superuser (optional)
python manage.py createsuperuser

# Run development server
python manage.py runserver

🖥️ Usage
Upload Receipts:

Navigate to /receipts/upload

Select a file (PDF, JPG, PNG, TXT)

System will automatically extract data

View Dashboard:

See spending overview at /

Visualize trends and distributions

Manage Receipts:

View all receipts at /receipts

Search, filter, and sort

Delete unwanted receipts

📂 Project Structure
