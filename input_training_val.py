import os
import pandas as pd
import csv
import pickle

# Takes in training and validation from the given files
def inputDataAttacks(startnum, endnumfile):
    typeCalls = 'Attack_Data_Master'
    seqFreq = []
    numberSeqFreq = []
    attacks = []
    file = []
    folder = []
    directory = '\\'.join(['ADFA-LD', 'ADFA-LD', typeCalls])
    # Types of attacks
    filetype = ('Adduser_', 'Hydra_FTP_', 'Hydra_SSH_', 'Java_Meterpreter_', 'Meterpreter_', 'Web_Shell_')
    # For each type of attack, there are several folders conatining files
    # Iterate through the types of attacks
    for files in filetype:
        startnumfile = startnum
        folder = []
        # Iterate through the folders of attack type "file", go through the files numbered "startnumfile" to "endnumfile"
        while(startnumfile <= endnumfile):
            directory2 = '\\'.join([directory, ''.join([files, str(startnumfile)])])
            listing = os.listdir(directory2)
            # Iterate through text files in folder... About 10
            for l in listing:
                f = open('\\'.join([directory2,l]),'r')
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
                file.append([seqFreq, numberSeqFreq]) # 7, [2]
            folder.append(file) # 7
            file = []
            startnumfile += 1
        attacks.append(folder) #6
    # print(attacks[0][0][0])
    # print(len(attacks))
    print("Done: Attack")
    return attacks

#Similar to inputDataAttacks, but the benign data is just a sigle folder containing a large amount of files
def inputDataBenign(typeCalls):
    seqFreq = []
    numberSeqFreq = []
    benign = []
    txtfile = []
    directory = '\\'.join(['ADFA-LD', 'ADFA-LD', typeCalls])
    filetype = os.listdir(directory)
    # Types of Attacks
    txtfile = []
    # Iterates through all the files contained in the benign file
    for file in filetype:
        f = open('\\'.join([directory,file]),'r')
        sequence = f.read()
        f.close()
        # split changes the string to an array of calls that splits at the spaces
        calls = sequence.split()
        # gram = the size of the frequency sliding window
        gram = 3
        n = gram
        seqFreq = []
        numberSeqFreq = []
        # Take sequence from file, mare an array of sequences with corresponding frequencies
        while (len(calls) >= n ):
            k = 0
            seq = []
            while(k < gram):
                seq.append(calls[(n+k-gram)])
                k += 1
            k = 0
            passval = 0
            # Save each frequency, per text file, put all in one largq array
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
    benign.append(txtfile)
    print("Done: Benign")
    return benign

#Takes the sequences in the different files it is given and adds the frequencies together, condensing them
def freqfindtot(folder): # [2xn], [calls, number]
    total = []
    seqFreq = []
    numberSeqFreq = []
    # Iterates for all the files in the array
    for file in folder:
        n = 0
        #This loop goes through and checks if an sequence is already in the final array, if so it adds the frequecy from the input to the final array
        #If the sequence is not in the final array, it appends the frequecy and sequnce to the final array
        while (n < len(file[0]))
            k = 0
            passval = 0
            while (k < len(seqFreq) and passval == 0):
                if(len(seqFreq) == 0):
                    seqFreq.append(file[0][n])
                    numberSeqFreq.append(file[1][n])
                if(seqFreq[k] == file[0][n]):
                    numberSeqFreq[k] += file[1][n]
                    passval = 1
                k += 1
            if (passval == 0):
                seqFreq.append(file[0][n])
                numberSeqFreq.append(file[1][n])
            n += 1
    # Returns the condensed frequecy sets
    return [seqFreq,numberSeqFreq]

# Finds top m percent of the set, need to give it array of arrays conatining the calls and the frequencies
# variable m is the percent.
def topm(totbytype, m):
    totalTopFreq = []
    calls = []
    count = []
    for  type in totbytype: # type
        # k is the number of sequences it will keep
        k = round(m*len(type[0]))
        topcount = []
        topcalls =[]
        n = 0
        # Iterate through all the sequences in the file and sort them from highest to lowest
        while (n < len(type[0])):
            l = 0
            count = type[1][n]
            calls = type[0][n]
            while (l < len(topcount)):
                if (count >= topcount[l]):
                    tempcount = topcount[l]
                    topcount[l] = count
                    count = tempcount

                    tempcalls = topcalls[l]
                    topcalls[l] = calls
                    calls = tempcalls
                l += 1
            topcount.append(count)
            topcalls.append(calls)
            n += 1
        totalFreq = []
        # topcount contains the sorted freque corresponding to the sequnces of calls in topcalls
        #This Iterates over the list of top frequencies and only keeps the top m% or k amount
        for x in range(int(k)):
            totalFreq.append(topcalls[x])
        # Implimented to remove duplicates in the top frequencies
        for freq in totalFreq:
            if (len(totalTopFreq) == 0):
                totalTopFreq.append(freq)
            else:
                for topFreq in totalTopFreq:
                    passval = 0
                    if (topFreq == freq):
                        passval == 1
                if (passval == 0):
                    totalTopFreq.append(freq)
    #Return the top m calls
    return totalTopFreq


#Combines the two variables since they are both multilayered to preserve infomation, but are needed together for some operations
def combine(attack,benign):
    totbytype = []
    for type in attack:
        totalFreq = []
        for folder in type:
            totalFreq = freqfindtot(folder)
            totbytype.append(totalFreq)
    totalFreq = []
    for folder in benign:
        totalFreq = freqfindtot(folder)
        totbytype.append(totalFreq)
    return totbytype


# Takes the top m% frequencies and sets the data to said frequencies and disregards the lower frequencies
def toFreq(columns, mFreq, sequence, mal):
    #Creates DataFrame with the top m% frequencies as the columns
    totalNewFreq = pd.DataFrame(columns = columns)
    for type in sequence:
        for folder in type:
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
                #This adds the final column for the training and valiidation. It is an identifier if it is malware or benign
                # 0 = Beign, 1 = Malware
                newFreqSet.append(mal)

                dfnewFreqSet = pd.DataFrame([newFreqSet], columns = columns)
                totalNewFreq = pd.concat([totalNewFreq,dfnewFreqSet],ignore_index = True)
    print('Done: Freq')
    #Returns the dataframe of the frequecy set
    return totalNewFreq

m = .1
attack = inputDataAttacks(1,7)

benign = inputDataBenign('Training_Data_Master')

benignVal = inputDataBenign('Validation_Data_Master')
attackVal = inputDataAttacks(7,10)

topmper = combine(attack,benign)
topMFreq = topm(topmper,m)
print(len(topMFreq))

#Saves the top m% frequencies into a file so that the set can be used in a different file
topm = open('topm10.data', 'wb')
pickle.dump(topMFreq, topm)
topm.close()

#Takes the top m% frequencies and turns them into a an array of strings so that they can be used as columns in the DataFrame variable
columns = []
for freq in topMFreq:
    columns.append(' '.join(freq))
#Adds 'Class' to the end of the columns for the identifier for malware or benign
# 0 = Beign, 1 = Malware
columns += ['Class']

attackTrainFreqs = toFreq(columns,topMFreq,attack, 1)
benignTrainFreqs = toFreq(columns,topMFreq,[benign], 0)

#Combines the training data and outputs it to a .csv file to be hadled in a different script
totTrainingData = pd.concat([benignTrainFreqs,attackTrainFreqs], ignore_index = True)
totTrainingData.to_csv('training.csv', index = False)

attackValFreqs = toFreq(columns,topMFreq, attackVal, 1)
benignValFreqs = toFreq(columns,topMFreq, [benignVal], 0)

#Combines the validation data and outputs it to a .csv file to be hadled in a different script
totValData = pd.concat([benignValFreqs,attackValFreqs], ignore_index = True)
totValData.to_csv('validation.csv', index = False)

#If yo want to put the benign and attavk training data together :
#totTrainingData = pd.concat([benignTrainFreqs,attackTrainFreqs], ignore_index = True)
