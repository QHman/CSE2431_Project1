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
    # sequence is a string containing the calls seperated by spaces
    sequence = f.read()
    f.close()
    # split changes the string to an array of calls that splits at the spaces
    calls = sequence.split()
    # gram = the size of the frequency sliding window
    gram = 3
    n = gram
    seqFreq = []
    numberSeqFreq = []
    # Take sequence from file, change to frequency using sliding window of size gram
    while (len(calls) >= n ):
        k = 0
        seq = []
        # Slide along the call sequence
        while(k < gram):
            seq.append(calls[(n+k-gram)])
            k += 1
        k = 0
        passval = 0
        # Save each frequency, if a sequence is repeated, it increments the frequency for that sequence
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
            #Goes through the call sequence and checks if one matches a top m% frequecy,
            while (n < len(file[0]) and passval == 0):
                #if there is a match for a top m% frequecy in the data set, it sets the frequecy from the dataset to be in the postion for said top m% frequecy sequence
                if (file[0][n] == freq):
                    newFreqSet.append(file[1][n])
                    passval = 1
                n += 1
            #If it doesn't exist in the data set, it puts a zero
            if (passval == 0):
                newFreqSet.append(0)
        dfnewFreqSet = pd.DataFrame([newFreqSet], columns = columns)
    print('Done: Freq')
    #Returns the dataframe of the frequecy set
    return dfnewFreqSet


#Change 'topm30.data' to 'topm10.data' for the 10% machince
#filemane is the name of the file containing the already trained SVM
filename = 'finalized_model10.sav'
topm = open('topm10.data', 'rb')
# loads in the top m% frequency set so that the data can be the correct format to be in the machine
mFreq = pickle.load(topm)
topm.close()

#Takes the top m% frequencies and turns them into a an array of strings so that they can be used as columns in the DataFrame variable
columns = []
for freq in mFreq:
    columns.append(' '.join(freq))

input = inputData('system_calls.txt')

dataFreq = toFreq(columns,mFreq,input)

#loads the trained SVM
loaded_malwareDetector = pickle.load(open(filename, 'rb'))

#makes and prints a prediction
prediction =loaded_malwareDetector.predict(dataFreq)
print('Prediction: ')
print(prediction)
print('\n')
if (prediction == 1):
    print("Its malware \n")
else:
    print("Its benign \n")
