from tutorial.functions import *
from tutorial.utils import *

# This is the task for Tutorial 1
# It does an end-to-end job, from generating the dataset
# to making the predictions and scoring the model

def generate_train_step(dataset_name, model_name):
    # Reading the data
    data = generate_dataset(dataset_name)

    # Processing the data
    features, labels = preprocess_data(data)
    
    # Training the model
    model = train_model(features, labels, model_name)
    
    # Making predictions
    predictions = make_predictions(model, features)
    
    # Calculating the accuracy of the model
    accuracy = calculate_accuracy(predictions, labels)
    
    # Outputs the predictions and the accuracy of the model
    return predictions, accuracy