
xAttackTrainFreq = attackTrainFreqs.drop('Class', axis=1)
yAttackTrainFreq = attackTrainFreqs['Class']

# Separate benign data into attributes and labels (Training)
xBenignTrainFreq = benignTrainFreqs.drop('Class', axis=1)
yBenignTrainFreq = benignTrainFreqs['Class']

# Separate attack data into attributes and labels (Validation)
xAttackValFreq = attackValFreqs.drop('Class', axis=1)
yAttackValFreq = attackValFreqs['Class']

# Separate benign data into attributes and labels (Validation)
xBenignValFreq = benignValFreqs.drop('Class', axis=1)
yBenignValFreq = benignValFreqs['Class']

# Train SVM algorithm using linear regression (Attack & Benign)
from sklearn.svm import SVC
svclassifier = SVC(kernel='linear')
svclassifier.fit(xAttackTrainFreq, yAttackTrainFreq)
svclassifier.fit(xBenignTrainFreq, yBenignTrainFreq)

# Algorithm predictions and evaluation (Attack)
yPredAttack = svclassifier.predict(xAttackValFreq)
from sklearn.metrics import classification_report, confusion_matrix
print(confusion_matrix(yAttackValFreq,yPredAttack))
print(classification_report(yAttackValFreq,yPredAttack))

# Train SVM algorithm using linear regression (Benign)
svclassifier.fit(x_trainBenign, y_trainBenign)

# Algorithm predictions and evaluation (Benign)
yPredBenign = svclassifier.predict(xBenignValFreq)
print(confusion_matrix(yBenignValFreq,yPredBenign))
print(classification_report(yBenignValFreq,yPredBenign))
