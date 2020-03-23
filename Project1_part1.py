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
        listing = os.listdir(path)
        for infile in listin
        f = open(os.path.join(path,infile),'r')
        f = open( + filetype[type] + file + , 'r')
        sequence = f.read()
        calls = sequence.split()
        one = calls[0]
        two = calls[1]
        three = calls[2]
        n = 3
        while(len(calls) > n ){
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
