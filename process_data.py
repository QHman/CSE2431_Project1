import os
import pandas as pd
import csv
import pickle

def inputData(typeCalls):
    seqFreq = []
    numberSeqFreq = []
    benign = []
    txtfile = []
    f = open((typeCalls),'r')
    sequence = f.read()
    f.close()
    calls = sequence.split()
    gram = 3
    n = gram
    seqFreq = []
    numberSeqFreq = []
    # Take sequence from file, change to frequency
    while (len(calls) >= n ):
        k = 0
        seq = []
        while(k < gram):
            seq.append(calls[(n+k-gram)])
            k += 1
        k = 0
        passval = 0
        # Save each frequency, per text file
        while (k < len(seqFreq) and passval == 0):
            if(len(seqFreq) == 0):
                seqFreq.append(seq)
                numberSeqFreq.append(1)
            if(seqFreq[k] == seq):
                numberSeqFreq[k] += 1
                passval = 1
            k += 1
        if (passval == 0):
            seqFreq.append(seq)
            numberSeqFreq.append(1)
        n += 1
    txtfile.append([seqFreq, numberSeqFreq])
    print("Done: input")
    return txtfile

def toFreq(columns, mFreq, folder):
    for file in folder:
        newFreqSet = []
        for freq in mFreq:
            n = 0
            passval = 0
            while (n < len(file[0]) and passval == 0):
                if (file[0][n] == freq):
                    newFreqSet.append(file[1][n])
                    passval = 1
                n += 1
            if (passval == 0):
                newFreqSet.append(0)
        dfnewFreqSet = pd.DataFrame([newFreqSet], columns = columns)
    print('Done: Freq')
    return dfnewFreqSet


#Change 'topm30.data' to 'topm10.data' for the 10% machince
filename = 'finalized_model30.sav'
topm = open('topm30.data', 'rb')
mFreq = pickle.load(topm)
topm.close()
print(len(mFreq))
columns = []
for freq in mFreq:
    columns.append(' '.join(freq))
input = inputData('data.txt')
dataFreq = toFreq(columns,mFreq,input)

loaded_malwareDetector = pickle.load(open(filename, 'rb'))

prediction =loaded_malwareDetector.predict(dataFreq)
print('Prediction: ')
print(prediction)
