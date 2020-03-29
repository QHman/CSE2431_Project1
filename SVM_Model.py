import os
import pandas as pd
import csv
import numpy as np
import matplotlib.pyplot as plt
import pickle

trainingData = pd.read_csv("training.csv")
validationData = pd.read_csv("validation.csv")

print("Done: Data transfer")

trainingData.shape
validationData.shape

trainingData.head
validationData.head

xTrainingData = trainingData.drop('Class', axis=1)
yTrainingData = trainingData['Class']

xValidationData = validationData.drop('Class', axis=1)
yValidationData = validationData['Class']

from sklearn.svm import SVC
maleware_detector = SVC(kernel='linear')
maleware_detector.fit(xTrainingData, yTrainingData)

yPrediction = maleware_detector.predict(xValidationData)

from sklearn.metrics import classification_report, confusion_matrix
print(confusion_matrix(yValidationData, yPrediction))
print(classification_report(yValidationData, yPrediction))


filename = 'finalized_model30.sav'
print(filename)
pickle.dump(maleware_detector, open(filename, 'wb'))

# Code to load malware detector model
# loaded_malwareDetector = pickle.load(open(filename, 'rb'))

from sklearn.metrics import classification_report, confusion_matrix
print(confusion_matrix(yValidationData, yPrediction))
print(classification_report(yValidationData, yPrediction))
