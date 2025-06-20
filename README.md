# CNN-Based Skin Cancer Detection and Classification

A deep learning project using Convolutional Neural Networks (CNNs) to classify dermoscopic skin lesion images into 7 types of cancer. A full-stack deployment was implemented using Django to enable real-time predictions via a web interface.

---

## Overview

- Built a custom CNN to classify lesions using the HAM10000 dataset  
- Compared performance with transfer learning models (VGG-16, ResNet-50, Xception)  
- Achieved 81% accuracy on the test set  
- Developed a Django web interface for user-friendly diagnosis  

---

## Model Architecture

- Input: 64×64×3 dermoscopic images  
- Layers: Conv → ReLU → MaxPool → Dropout → Fully Connected  
- Optimizer: Adam | Loss: Categorical Crossentropy | Metrics: Accuracy  

> Compared against VGG-16, ResNet-50, and Xception architectures  

![Architecture](./static/model_diagram.png)

---

## Dataset

- **Source:** [HAM10000](https://www.kaggle.com/datasets/kmader/skin-cancer-mnist-ham10000)  
- **Classes:**
  - Melanoma (mel)
  - Melanocytic Nevi (nv)
  - Basal Cell Carcinoma (bcc)
  - Benign Keratosis (bkl)
  - Actinic Keratoses (akiec)
  - Dermatofibroma (df)
  - Vascular Lesions (vasc)

- Preprocessing: resizing, normalization, and class balancing

---

## Results

| Model         | Accuracy | Loss   |
|---------------|----------|--------|
| CNN (proposed)| 81.0%    | 0.63   |
| ResNet-50     | 79.0%    | 1.15   |
| VGG-16        | 76.0%    | 1.78   |
| Xception      | 73.0%    | 11.64  |

> Also evaluated using confusion matrix, precision, recall, and F1-score

---

## Web Interface (Local Deployment)

This project includes a Django-based web application for classifying skin lesion images. The app was developed for **local use only** and is **not hosted online**.

---

Project Files
	•	notebooks/skin-cancer.ipynb – CNN training, testing, and evaluation
	•	thesis.pdf – Full academic thesis
	•	presentation.pdf – Final presentation slides
	•	webapp/ – Django web frontend
	•	requirements.txt – Required packages
	•	README.md – Project documentation
