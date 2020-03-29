# CSE2431_Project1
Project 1: Malware detection

Authors:	Quinton Hiler
		Andrew Cantor

Description:
A machine learning malware detector in python and C.  With the detector created using a SVM algorithm in python and grabing the system calls using C.

# Compile

The command will compile the C portion of this project:
	
	gcc -o ptrace_malware ptrace_malware.c

# Runs

1. Entire detector
Once the code has been compiled to binary file 'ptrace_malware', it can be run using the following command:
	
	./ptrace_malware potential_malware potential_malware_args

2. SVM model, this is needed to run the detector if the needed files are missing. (The files needed to run the entire detector should already be provided, this is here for completeness sake)
Assuming the correct modules are installed (see header of python files) and the working directory is the same as the file, to get the training and validation data is parsed for the SVM machine run 'input_training_val.py' using:

	python input_training_val.py

That command will create two files 'training.csv' and 'validation.csv', these are used by the SVM model.  To run the SVM model in 'SVM_Model.py' use:

	python SVM_Model.py

That will produce the SVM model file, that is the saved algorithm for future use so that the model does not need to be trained every time it is used.  This will allow the detector to run properly.
