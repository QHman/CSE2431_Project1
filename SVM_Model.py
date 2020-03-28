import os
import pandas as pd
import csv
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

trainingData = pd.read_csv("training.csv")
validationData = pd.read_csv("validation.csv")

trainingData.shape
validationData.shape

trainingData.head
validationData.head

xTrainingData = trainingData.drop('Class', axis=1)
yTrainingData = trainingData['Class']

xValidationData = validationData.drop('Class', axis=1)
yValidationData = validationData['Class']

from sklearn.svm import SVC
svclassifier = SVC(kernel='linear')
svclassifier.fit(xTrainingData, yTrainingData)

yPrediction = svclassifier.predict(xValidationData)

from sklearn.metrics import classification_report, confusion_matrix
print(confusion_matrix(yValidationData, yPrediction))
print(classification_report(yValidationData, yPrediction))
