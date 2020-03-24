# import pandas as pd
# import numpy as np
import os
# from sklearn.svm import SVC
# import matplotlib.pyplot as plt

def inputDataAttacks(startnum, endnumfile):
    typeCalls = 'Attack_Data_Master'
    startnumfile = startnum
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
        while(startnumfile <= endnumfile):
            print(''.join([files, str(startnumfile)]))
            directory2 = '\\'.join([directory, ''.join([files, str(startnumfile)])])
            #   Folder in type ex. 1, 2, 3
            folder = []
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
                file.append([seqFreq, numberSeqFreq])
            folder.append(file)
            file = []
            startnumfile += 1
            attacks.append(folder)

    print(attacks[0][0][0])
    return attacks

def inputDataBenign(typeCalls):
    seqFreq = []
    numberSeqFreq = []
    benign = []
    txtfile = []
    directory = '\\'.join(['ADFA-LD', 'ADFA-LD', typeCalls])
    filetype = os.listdir(directory)
    # Types of Attacks
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
        txtfile = []
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
    return benign

def

inputDataAttacks(1,7)
inputDataBenign('Training_Data_Master')
