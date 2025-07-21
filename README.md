
# 🧾 Receipt Processor

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)
![Tesseract](https://img.shields.io/badge/Tesseract-3D8FC4?style=for-the-badge&logo=tesseract&logoColor=white)

A full-stack Django app to extract, manage, and analyze receipt data using OCR 🔍.

---

## 📸 Preview

<div align="center">
  <img src="https://github.com/yourusername/receipt-processor/raw/main/screenshots/dashboard.png" width="45%">
  <img src="https://github.com/yourusername/receipt-processor/raw/main/screenshots/upload.png" width="45%">
</div>

---

## 🚀 Overview

**Receipt Processor** is a powerful tool to extract key information from bills and receipts like vendor name, date, and total amount using OCR (Tesseract). It helps users track spending, organize receipts, and gain insights through analytics and visualizations.

---

## ✨ Features

- 📤 **Multi-format Uploads**: Supports **PDF**, **JPG**, **PNG**, and **TXT**
- 🧠 **OCR Data Extraction**: Detects:
  - Vendor Name
  - Transaction Date
  - Total Amount
  - Category
- 📊 **Visual Analytics**:
  - Spending overview
  - Vendor-based breakdowns
  - Trends over time
- 💡 **Clean, Responsive UI**:
  - Built with Bootstrap
  - Interactive tables and modals

---

## 🧰 Tech Stack

| Component        | Technology |
|------------------|------------|
| **Backend**      | ![Django](https://img.shields.io/badge/Django-092E20?style=flat-square&logo=django&logoColor=white) |
| **Frontend**     | ![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=flat-square&logo=bootstrap&logoColor=white) |
| **Database**     | ![SQLite](https://img.shields.io/badge/SQLite-07405E?style=flat-square&logo=sqlite&logoColor=white) |
| **OCR Engine**   | ![Tesseract](https://img.shields.io/badge/Tesseract-3D8FC4?style=flat-square&logo=tesseract&logoColor=white) |
| **Supported Formats** | ![PDF](https://img.shields.io/badge/PDF-FF0000?style=flat-square&logo=adobe-acrobat-reader&logoColor=white) ![Image](https://img.shields.io/badge/Images-FFA500?style=flat-square&logo=image&logoColor=white) ![Text](https://img.shields.io/badge/Text-000000?style=flat-square&logo=text&logoColor=white) |

---

## 📦 Installation

### 🔧 Prerequisites

- Python 3.8+
- Tesseract OCR engine  
  ➤ [Tesseract Installation Guide](https://github.com/tesseract-ocr/tesseract)

### 🛠️ Setup Steps

```bash
# Clone the repo
git clone https://github.com/yourusername/receipt-processor.git
cd receipt-processor

# Create and activate virtual environment
python -m venv venv
venv\Scripts\activate  # On Windows
# source venv/bin/activate  # On Unix

# Install dependencies
pip install -r requirements.txt

# Apply database migrations
python manage.py migrate

# (Optional) Create a superuser
python manage.py createsuperuser

# Start the development server
python manage.py runserver
```

---

## 🖥️ Usage Guide

- 🔼 **Upload Receipts**  
  ➤ Navigate to `/receipts/upload`  
  ➤ Upload PDF, image, or text files

- 📊 **View Dashboard**  
  ➤ Access spending stats at `/`

- 📁 **Manage Receipts**  
  ➤ Browse, search, sort, or delete via `/receipts`

---

## 📁 Project Structure

```
receipt_processor/
├── receipts/
│   ├── migrations/
│   ├── templates/receipts/
│   │   ├── base.html
│   │   ├── dashboard.html
│   │   ├── receipt_list.html
│   │   ├── receipt_upload.html
│   │   ├── receipt_detail.html
│   │   └── receipt_confirm_delete.html
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── parsers.py
│   ├── services.py
│   ├── tests.py
│   ├── utils.py
│   └── views.py
├── receipt_processor/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── db.sqlite3
├── manage.py
└── README.md
```

---

## 📷 Screenshots

> Place these inside a `/screenshots` folder in your repo:

- `dashboard.png` – analytics overview
- `upload.png` – file upload form
- `list.png` – receipt list with filters

---

## 🧠 Tips for Better UX

- ✅ Add a GIF showing upload-to-dashboard flow
- 🔍 Keep OCR logic modular (`parsers.py`, `utils.py`)
- 📱 Ensure UI is responsive on mobile

---

## 📜 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 📬 Contact

**Your Name**  
📧 harshac032@gmail.com  
🔗 [Project Repository](https://github.com/Harsha-032/OCR_PROJECT)

---

> 💡 *Built with Django, OCR, and a passion for clean data.*
