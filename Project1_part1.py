# import pandas as pd
# import numpy as np
import os
# from sklearn.svm import SVC
# import matplotlib.pyplot as plt
file = 1
type = 0
seqFreq = []
numberSeqFreq = []
filetype = ('Adduser_', 'Hydra_FTP_', 'Hydra_SSH_', 'Java_Meterpreter_', 'Meterpeter_', 'Web_Shell_')
while(type  < 6):
    while(file < 8):
        filenum = ''.join([filetype[type], str(file)])
        directory = '\\'.join(['ADFA-LD', 'ADFA-LD', 'Attack_Data_Master',filenum])
        listing = os.listdir(directory)
        l = 0
        while(l < len(listing)):
            print(listing)
            f = open('\\'.join([directory,listing[l]]),'r')
            sequence = f.read()
            f.close()
            calls = sequence.split()
            print(calls)
            gram = 2
            n = gram
            while (len(calls) >= n ):
                k = 0
                seq = []
                while(k < gram):
                    seq.append(calls[(n+k-gram)])
                    k += 1

                print(seq)
                k = 0
                passval = 0
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
                print(seqFreq)
                n += 1
            l +=1
        file +=1
    type +=1
