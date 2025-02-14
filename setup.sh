#!/bin/bash

# Install Python dependencies
echo "Installing dependencies from requirements.txt..."
pip install -r requirements.txt

# Download movies_dict.pkl from Google Drive
echo "Downloading movies_dict.pkl..."
FILE_ID="1lGGJ6rqaKU1lCzTyR7joWL1YosvgeNna"
FILE_NAME="movies_dict.pkl"
curl -L -o ${FILE_NAME} "https://drive.google.com/uc?export=download&id=${FILE_ID}"

# Download similarity.pkl from Google Drive
echo "Downloading similarity.pkl..."
FILE_ID="1Jfy8zB_MwJg343HbtvD4tPutADg4Ak_F"
FILE_NAME="similarity.pkl"
curl -L -c cookies.txt "https://drive.google.com/uc?export=download&id=${FILE_ID}" | grep -o 'confirm=[^&]*' | cut -d '=' -f 2 > confirm.txt
CONFIRM=$(cat confirm.txt)
curl -L -b cookies.txt -o ${FILE_NAME} "https://drive.google.com/uc?export=download&id=${FILE_ID}&confirm=${CONFIRM}"
rm cookies.txt confirm.txt

echo "Setup complete!"