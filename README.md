# RTG code challenge 

The objective of this challenge is to give you a chance to demonstrate your abilities to tackle a common scenario using your technical coding skills. This will involve following instructions and asking questions where appropriate. It is very common to deal with situations that need clarifying in our work, so feel free to ask questions if something is unfamiliar or unclear. This can be especially important if you don't completely understand some terminology or a requirement, a quick well placed question can save you a lot of time.    

## Instructions
Your task will be to complete (or improve) some code and produce some output for a client. By the end of the task you should have a running script (`challenge_script.py`) and some values to show the client. There is some skeleton code to get you started, but make sure to read the instructions carefully and come back to them as needed.

You are to modify the code in the `challenge_script.py` file to make it work and comply to the client requirements below. We have identified the places where you will need to modify the code to make it work between these kind of symbols `>>>>>>` & `<<<<<<`. Feel free to modify outside these symbols if you want to improve the standard of the code in any way. 

A text file containing some short DNA sequences that are to be used as input has been provided by the client. Also provided by the client is another text file with the results of an algorithm that the client has already used to process the DNA sequences (these are where the 'true labels' come from). The goal here is processing the provided DNA sequences with another very simple algorithm within the script you will work on and see how close the results are to the previous algorithm. In reality, the provided results are random, it is very unlikely that what you get will match very well, so don't worry about the actual results you produce. This also mean that you can't really get the algorithm wrong either. The "algorithm" you will implement is just some very simple string matching and is not meant to trip you up, the quality of the implementation is whats important. Keep in mind we may want to use algorithms in other projects later, so aspects like readability and portability are valuable.      

It could be a good idea to make a branch to work on your solution to display some git competency. 

## Requirements 
1. Read in the DNA sequences and true labels from the input files (provided by the client in `./input_data`) and store them in two lists.

2. Predict the labels for each DNA sequence using a simple algorithm that classifies a sequence as 'positive' if it contains the subsequence 'ATG' and is longer than 20 nucleotide long, otherwise the label should be negative. The client has provided an algorithm from some previous work that they think might be useful. This should to be adapted to get the results we need. 


3. Create a confusion matrix that shows the number of true positive, false positive, true negative, and false negative classifications for the algorithm you implemented against the previous results (`true_labels`). Some previous work from the client also required a confusion matrix, so we can reference that code if we wanted to or feel free to implement your own way of doing this if that is more comfortable for you. 

4. Report the accuracy, precision, and recall of the classifier algorithm you implemented (see Definitions below). A simple print statement or writing the results to a file would suffice for this project.

5. Include some simple documentation so the client can run the script, understand what it is doing, and know what to expect. This can be in a new file and/or inline with the code.

## Definitions 
Here are the standard definitions we will use. 

### Outcomes:
- True positive (TP): item was correctly classified as positive
- False positive (FP): item was incorrectly classified as positive
- True Negative (TN): item was correctly classified as negative
- False Negative (FN): item was incorrectly classified as negative

### Metrics
- Accuracy: `(TP + TN) / (TP + TN + FP + FN)`
- Precision: `TP / (TP + FP)`
- Recall: `TP / (TP + FN)`
