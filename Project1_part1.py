# import pandas as pd
# import numpy as np
import os
# from sklearn.svm import SVC
# import matplotlib.pyplot as plt
file = 1
type = 0
numtype =  6
numfile =  7
seqFreq = []
numberSeqFreq = []
attacks = []
filetype = ('Adduser_', 'Hydra_FTP_', 'Hydra_SSH_', 'Java_Meterpreter_', 'Meterpreter_', 'Web_Shell_')
# Types of Attacks
while(type  < numtype):
    print(filetype[type])
    file = 1
    # Folder in type ex. 1, 2, 3
    folder = []
    while(file <= numfile):
        filenum = ''.join([filetype[type], str(file)])
        print(filenum)
        directory = '\\'.join(['ADFA-LD', 'ADFA-LD', 'Attack_Data_Master',filenum])
        listing = os.listdir(directory)
        l = 0
        # Text Doc in folder... About 10
        while(l < len(listing)):
            print(listing[l])
            f = open('\\'.join([directory,listing[l]]),'r')
            sequence = f.read()
            f.close()
            calls = sequence.split()
            print(len(calls))
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
            l += 1
            folder.append([seqFreq, numberSeqFreq])
        file += 1
    attacks.append(folder)
    print(attacks)
    type += 1
