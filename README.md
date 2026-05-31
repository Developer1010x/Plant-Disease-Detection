# 🌿 Plant Disease Classification with ResNet50

A deep learning-based solution for **accurate plant disease detection** using the **ResNet50 architecture**, enriched with a user-friendly **chatbot interface** for real-time interaction, information, and preventive recommendations.

---

## 📌 Key Features

- 📷 **Leaf Image-Based Detection** using ResNet50
- 🧠 **Hyperparameter-Tuned** for optimal performance
- 🤖 **Chatbot Integration** for disease info and guidance
- 🌍 **Supports Multiple Plant Species & Diseases**
- 🧪 Tested on **diverse datasets** including PlantVillage & BLPD

---

## 📊 Model Overview

- **Architecture**: ResNet50 + Dense layers + GlobalAvgPooling
- **Accuracy**: Achieved **96.1% validation accuracy**
- **Training Enhancements**:
  - Otsu thresholding & Gaussian Blur preprocessing
  - Data augmentation (flip, shear, zoom)
  - Learning rate: `0.001`, Batch size: `32`, Epochs: `50`
  - Optimizer: `Adam`, Loss: `Categorical Crossentropy`

---

## 📂 Project Structure

├── freshplant.ipynb # Jupyter notebook for training & evaluation
├── model.py # Model architecture (ResNet50 + tuning)
├── train.py # Training logic
├── gui.py # Main GUI script
├── chat.py # Chatbot script
├── web.py # Flask web interface (optional)
├── nltk_utils.py # NLP utilities for chatbot
├── README.md # Project documentation


---

## 🚀 Getting Started

### 🔧 Requirements

Install dependencies:

```bash
pip install -r requirements.txt
```

### 🏁 Setup & Run

The chatbot needs an intents file and a trained model before the GUI can run:

```bash
# 1. Scrape disease info and generate intents.json
python web.py

# 2. Train the chatbot (produces data.pth)
python train.py

# 3. Launch the GUI (needs the ResNet model file reseven.h5 in this folder)
python gui.py
```

In the GUI, click **Upload Leaf** to pick a leaf image — the ResNet model
predicts the disease and the chatbot automatically returns treatment guidance.
You can also type a disease name directly to query the bot.

To explore training/evaluation interactively:

```bash
jupyter notebook freshplant.ipynb
```



📚 Datasets Used

PlantVillage Dataset
PlantDoc
Blackgram-specific dataset (BLPD)
🤖 Chatbot Integration

A natural language interface to ask about:

Identified disease name
Symptoms & treatment suggestions
Prevention techniques
🔬 Results

Validation Accuracy: 96.1%
Performance Improved through:
Custom preprocessing
Data augmentation
Learning rate scheduling & callbacks
📌 Future Scope

Real-time mobile/web deployment
Multilingual chatbot responses
Integration with soil/environment data
Expansion to more plant species
📄 License

MIT License

👨‍🔬 Authors

Abhishek R
Aditya S
S Prajwall Narayana
Dr. Suma B
(RV College of Engineering, Bengaluru)


📬 Contact

📧 For collaborations: abhishekr.cs21@rvce.edu.in


---
