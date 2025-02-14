#!/bin/bash

# Install Python dependencies
echo "Installing dependencies from requirements.txt..."
pip install -r requirements.txt

# Download movies_dict.pkl from Google Drive
echo "Downloading movies_dict.pkl..."
wget -O movies_dict.pkl "https://drive.google.com/uc?export=download&id=1lGGJ6rqaKU1lCzTyR7joWL1YosvgeNna"

# Download similarity.pkl from Google Drive
echo "Downloading similarity.pkl..."
wget -O similarity.pkl "https://drive.google.com/uc?export=download&id=1Jfy8zB_MwJg343HbtvD4tPutADg4Ak_F"

echo "Setup complete!"