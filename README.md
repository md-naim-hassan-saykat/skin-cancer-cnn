# Skin Cancer Classification (CNN)

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/md-naim-hassan-saykat/skin-cancer-cnn/blob/main/BachelorThesis/skin-cancer.ipynb)

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/downloads/release/python-390/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange)](https://www.tensorflow.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

This project implements a **Convolutional Neural Network (CNN)** for automated skin cancer classification.  
It leverages **deep learning** to classify dermatoscopic images into multiple lesion categories, supporting early diagnosis and medical decision-making.

---

## Overview
- **Dataset**: HAM10000 skin lesion dataset  
- **Model**: Convolutional Neural Network (CNN) built with Keras/TensorFlow  
- **Features**:
  - Custom CNN model trained from scratch
  - Image preprocessing and augmentation
  - Evaluation using accuracy, precision, recall, F1-score
  - Visualization: loss/accuracy curves, confusion matrix 
  - Web interface for image upload and prediction (Django + Bootstrap)
- **Goal**: Demonstrate how deep learning can assist dermatologists by classifying skin lesion images automatically.

---

## Dataset
The dataset used is **HAM10000** (Human Against Machine with 10000 training images).  
It includes dermatoscopic images of common pigmented skin lesions.

Dataset reference:  
> Tschandl P, Rosendahl C, Kittler H. *The HAM10000 dataset: A large collection of multi-source dermatoscopic images of common pigmented skin lesions*. Sci Data 5, 180161 (2018).  
🔗 [Dataset Link (Kaggle)](https://www.kaggle.com/kmader/skin-cancer-mnist-ham10000)

---

## Pre-trained Model
The trained CNN model is available here:  
[Download mymodel.h5 (Google Drive)](https://drive.google.com/drive/u/2/folders/1MG7tE-8BslsMz34m-EtOGDHvOdXGjrbB)

After downloading, place it into the `kerasModel/` folder:
skin-cancer-cnn/
├── kerasModel/
│   └── mymodel.h5   # Pre-trained CNN model

---

## Repository Structure
skin-cancer-cnn/
├── core/                 # Django app (models, views, urls, migrations)
├── docInterface/         # Django project settings
├── kerasModel/           # Saved CNN model (mymodel.h5)
├── media/                # Uploaded/test images
├── static/               # CSS, JS, Bootstrap, logo, theme
├── templates/            # Frontend HTML templates
├── manage.py             # Django project manager
├── requirements.txt      # Python dependencies
└── db.sqlite3            # SQLite database (local only, don’t upload)

---

## Installation & Setup

### 1. Create and activate a virtual environment
```bash
python -m venv .venv
# Activate
source .venv/bin/activate        # Mac/Linux
.venv\Scripts\activate           # Windows

## Install dependencies
pip install -r requirements.txt

## Apply database migrations
python manage.py migrate

## Create a superuser (for Django Admin)
python manage.py createsuperuser

## Run the server
python manage.py runserver

## Open in browser
http://127.0.0.1:8000

## Troubleshooting
	•	Page doesn’t open?
	•	Ensure the server is actually running (you should see:
“Starting development server at http://127.0.0.1:8000/” in the terminal).
	•	Check ALLOWED_HOSTS in docInterface/settings.py includes:
ALLOWED_HOSTS = ["127.0.0.1", "localhost"]

## Port 8000 is busy?
Run on a different port:
python manage.py runserver 8001

## Then open:
http://127.0.0.1:8001

## Running on a remote machine / Colab?
Expose the server to all hosts:
python manage.py runserver 0.0.0.0:8000

---

# Results

- Training and validation accuracy improve steadily over epochs.
- Confusion matrix shows class-wise performance.
- Test accuracy demonstrates robust classification across lesion types.

 ---

# Web Interface

The project includes a simple Django web app:
	•	Upload an image
	•	Model predicts the skin lesion category
	•	Result displayed on the frontend (Bootstrap-based UI)

---

# Requirements
Main dependencies (full list in requirements.txt):
	•	Python 3.9+
	•	Django 4.x
	•	TensorFlow / Keras
	•	scikit-learn
	•	matplotlib
	•	numpy
	•	bootstrap (via static files)

 ---

# License
This project is licensed under the MIT License.
Feel free to use and adapt it for research and educational purposes.

---

# Author

 **Md Naim Hassan Saykat**  
*MSc in Artificial Intelligence, Université Paris-Saclay*  

[LinkedIn](https://www.linkedin.com/in/md-naim-hassan-saykat/)  
[GitHub](https://github.com/md-naim-hassan-saykat)  
[Academic Email](mailto:md-naim-hassan.saykat@universite-paris-saclay.fr)  
[Personal Email](mailto:mdnaimhassansaykat@gmail.com) 
