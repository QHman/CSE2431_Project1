import os
import pandas as pd
import csv
import numpy as np
import matplotlib.pyplot as plt
import pickle

# Transfer data from files.
trainingData = pd.read_csv("training.csv")
validationData = pd.read_csv("validation.csv")

print("Done: Data transfer")

# Validify data format and shape
trainingData.shape
validationData.shape
trainingData.head
validationData.head

# Extract training/validation data into attributes and labels
# Label is binary numeric (1 for malware / 0 for benign)
xTrainingData = trainingData.drop('Class', axis=1)
yTrainingData = trainingData['Class']

xValidationData = validationData.drop('Class', axis=1)
yValidationData = validationData['Class']

# Createe SVM model with linear regression
from sklearn.svm import SVC
maleware_detector = SVC(kernel='linear')

# Train SVM algorithm
maleware_detector.fit(xTrainingData, yTrainingData)

# Predict malware and benign software from validation data
yPrediction = maleware_detector.predict(xValidationData)

# Print out confusion matrix and classification report for algorithm prediction
from sklearn.metrics import classification_report, confusion_matrix
print(confusion_matrix(yValidationData, yPrediction))
print(classification_report(yValidationData, yPrediction))

# Store finalized SVM model in .sav file for later use
filename = 'finalized_model10.sav'
print(filename)
pickle.dump(maleware_detector, open(filename, 'wb'))

# Code to load malware detector model
# loaded_malwareDetector = pickle.load(open(filename, 'rb'))

from sklearn.metrics import classification_report, confusion_matrix
print(confusion_matrix(yValidationData, yPrediction))
print(classification_report(yValidationData, yPrediction))
