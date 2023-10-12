# Theyyam Classifier API
## Description
This project is a REST API developed using Django and Django REST Framework. The objective of this project is to wrap a TensorFlow-based image classification model into a REST API. The API was then deployed on an Azure Virtual Machine using NGINX.

## Features
The API provides an endpoint to upload an image and receive the prediction from the TensorFlow model. Please note that this API does not implement any authentication.

## Installation
1. Clone the repository to your local machine using `git clone https://github.com/abdulhakkeempa/theyyam-classifier-api.git`.
2. Navigate to the project directory and install the necessary dependencies using `pip install -r requirements.txt`.
3. Create a folder named 'model' in the root directory. Place your model, checkpoints, and label encoder (`label_encoder.pkl`) in this folder. If your label encoder has a different name, please update the code accordingly.
4. Run the application using `python manage.py runserver`.

## Usage
After successful installation, you can use the API endpoint to upload an image and receive the prediction from the TensorFlow model.

## Contributing
Contributions are welcome. Please feel free to submit a pull request or open an issue.
