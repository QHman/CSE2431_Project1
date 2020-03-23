import pandas as pd
import numpy as np
import os
from sklearn.svm import SVC
import matplotlib.pyplot as plt
%matplotlib inline
file = 1
type = 0
seqFreq = np.array[]
numberSeqFreq = np.array[]
filetype = ("Adduser_", "Hydra_FTP_", "Hydra_SSH_", "Java_Meterpreter_", "Meterpeter_", "Web_Shell_")
while(type  < 6){
    while(file < 8){
        directory = os.join('ADFA-LD\\ADFA-LD\\Attack_Data_Master\\',filetype[type], file, '\\')
        listing = os.listdir(directory);
        l = 0
        while(l < len(listing)){
            f = open(os.join(directory,'\\',infile),'r')
            sequence = f.read()
            f.close()
            calls = sequence.split()
            print(calls)
            gram = 2
            n = gram
            while(len(calls) >= n ){
                k = 0
                seq = []
                while(k < gram){
                    seq.append(cals[(n+k-grams)])
                    k ++
                }
                k = 0
                pass = 0
                while(k < seqFreq && pass == 0){
                    if(seqFreq[k] == seq){
                    numberSeqFreq[k] ++
                    pass = 1
                    }
                    k ++
                }
                if (pass == 0){
                    seqFreq.append(seq)
                    numberSeqFreq.append(1)
                }

                n ++
            }


            l++
        }

    file ++
    }
    type ++
}
