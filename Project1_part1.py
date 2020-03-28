import os
import pandas as pd
import csv
def inputDataAttacks(startnum, endnumfile):
    typeCalls = 'Attack_Data_Master'
    seqFreq = []
    numberSeqFreq = []
    attacks = []
    file = []
    folder = []
    directory = '\\'.join(['ADFA-LD', 'ADFA-LD', typeCalls])
    filetype = ('Adduser_', 'Hydra_FTP_', 'Hydra_SSH_', 'Java_Meterpreter_', 'Meterpreter_', 'Web_Shell_')
    # Types of Attacks
    for files in filetype:
        startnumfile = startnum
        folder = []
        while(startnumfile <= endnumfile):
            directory2 = '\\'.join([directory, ''.join([files, str(startnumfile)])])
            #   Folder in type ex. 1, 2, 3

            listing = os.listdir(directory2)
            # Text Doc in folder... About 10
            for l in listing:
                f = open('\\'.join([directory2,l]),'r')
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
                file.append([seqFreq, numberSeqFreq]) # 7, [2]
            folder.append(file) # 7
            file = []
            startnumfile += 1
        attacks.append(folder) #6
    # print(attacks[0][0][0])
    # print(len(attacks))
    print("Done: Attack")
    return attacks

def inputDataBenign(typeCalls):
    seqFreq = []
    numberSeqFreq = []
    benign = []
    txtfile = []
    directory = '\\'.join(['ADFA-LD', 'ADFA-LD', typeCalls])
    filetype = os.listdir(directory)
    # Types of Attacks
    txtfile = []
    for type in filetype:
        f = open('\\'.join([directory,type]),'r')
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
    benign.append(txtfile)
    print("Done: Benign")
    return benign

def freqfindtot(folder): # [2xn], [calls, number]
    total = []
    seqFreq = []
    numberSeqFreq = []
    for file in folder:
        n = 0
        while (n < len(file[0])):
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
    return [seqFreq,numberSeqFreq]

# finds top m, need to give it array of arrays conatining the calls and the frequencies
def topm(totbytype, m):
    totalTopFreq = []
    calls = []
    count = []
    for  type in totbytype: # type
        k = round(m*len(type[0]))
        topcount = []
        topcalls =[]
        n = 0
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
        for x in range(int(k)):
            totalFreq.append(topcalls[x])
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
    return totalTopFreq





 # attack: data in, m: percent top, ex .2, .3

def topmAttacksAndBenign(attack,benign):
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


def toFreq(columns, mFreq, sequence, mal):

    totalNewFreq = pd.DataFrame(columns = columns)
    for type in sequence:
        for folder in type:
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
                newFreqSet.append(mal)
                dfnewFreqSet = pd.DataFrame([newFreqSet], columns = columns)
                totalNewFreq = pd.concat([totalNewFreq,dfnewFreqSet],ignore_index = True)
    print('Done: Freq')
    return totalNewFreq

m = .3
attack = inputDataAttacks(1,7)

benign = inputDataBenign('Training_Data_Master')
print(len(benign))
print(len(benign[0]))
print(len(benign[0][0]))
print('attack:')
print(len(attack))
print(len(attack[0]))
print(len(attack[0][0]))
print(len(attack[0][0][0]))

benignVal = inputDataBenign('Validation_Data_Master')
attackVal = inputDataAttacks(7,10)

topmper = topmAttacksAndBenign(attack,benign)
topMFreq = topm(topmper,m)
print(len(topMFreq))
columns = []
for freq in topMFreq:
    columns.append(' '.join(freq))
columns += ['Class']
attackTrainFreqs = toFreq(columns,topMFreq,attack, 1)

benignTrainFreqs = toFreq(columns,topMFreq,[benign], 0)
totTrainingData = pd.concat([benignTrainFreqs,attackTrainFreqs], ignore_index = True)
totTrainingData.to_csv('training.csv', index = False)

attackValFreqs = toFreq(columns,topMFreq, attackVal, 1)

benignValFreqs = toFreq(columns,topMFreq, [benignVal], 0)
totTrainingData = pd.concat([benignTrainFreqs,attackTrainFreqs], ignore_index = True)
totTrainingData.to_csv('validation.csv', index = False)
#If yo want to put the benign and attavk training data together :
#totTrainingData = pd.concat([benignTrainFreqs,attackTrainFreqs], ignore_index = True)

