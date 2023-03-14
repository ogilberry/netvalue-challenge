# Import necessary libraries
import sys
import numpy as np
from pathlib import Path


# Set input path
INPUT_DIR = Path('input_data')
POSITIVE = 'positive'
NEGATIVE = 'negative'
INVALID = 'invalid'
SEQUENCES = 'sequences.txt'
TRUE_LABELS = 'true_labels.txt'

def get_list_from_file(filename):
    try:
        with open(INPUT_DIR/filename, 'r') as f:
            result = f.read().splitlines()
        return result
    except FileNotFoundError:
        print (f'Could not find file {filename}')
        sys.exit(1)
    except Exception as e:
        print (f'Error trying to open file {filename}: {repr(e)}')
        sys.exit(1)

# Read in the DNA sequences input txt file
#>>>>>>
sequences = get_list_from_file(SEQUENCES)
true_labels = get_list_from_file(TRUE_LABELS)

# Warn/inform the user if the two input files are of different lengths 
if (len(sequences) != len(true_labels)):
    print(f'Warning: {SEQUENCES} contains {len(sequences)} lines, but {TRUE_LABELS} '
    + f'contains {len(true_labels)} lines. Only the first {min(len(sequences), len(true_labels))} '
    + 'lines will be checked. ')
    
# Inform the user if either input file is empty, then exit before reporting results
if len(sequences) == 0:
    print (f'{SEQUENCES} contains no data. Aborting')
    sys.exit(1)
if len(true_labels) == 0:
    print (f'{TRUE_LABELS} contains no data. Aborting')
    sys.exit(1)
#<<<<<<
 
# Define a function to predict the label for a given DNA sequence
def predict_label(sequence):
#>>>>>>
    valid_nucleotides = ['G', 'C', 'A', 'T', 'U']
    target_matches = ['ATG']
    min_length = 21
    # not a performative algorithm (O(kn) without validation), but easily modifiable
    if not all(n in valid_nucleotides for n in sequence):
        return INVALID
    
    if len(sequence) >= min_length and all(match in sequence for match in target_matches):
        return POSITIVE

    return NEGATIVE
#<<<<<<


# Predict the labels for each DNA sequence using the predict_label function
#<<<<<<
predicted_labels = [predict_label(l) for l in sequences]
#>>>>>>

# Create a confusion matrix to summarize the performance of the predictions
#>>>>>>
confusion_matrix = np.zeros((2, 2)) 
invalid_sequence_lines = []
invalid_true_lines = []
line = 1
# Count the outcomes and update the matrix
for true, predicted in zip(true_labels, predicted_labels):
    # first check if both the sequence and then the true label inputs are valid
    if predicted == INVALID:
        invalid_sequence_lines.append(line)
    elif true != POSITIVE and true != NEGATIVE:
        invalid_true_lines.append(line)
    # now both inputs have been validated, compare the predictions and increment confusion_matrix
    elif true == POSITIVE and predicted == POSITIVE: 
        confusion_matrix[0, 0] += 1
    elif true == POSITIVE and predicted == NEGATIVE:
        confusion_matrix[1, 0] += 1
    elif true == NEGATIVE and predicted == NEGATIVE:
        confusion_matrix[1, 1] += 1
    elif true == NEGATIVE and predicted == POSITIVE:
        confusion_matrix[0, 1] += 1
    else:
        print(f'Unknown label(s): {true}, {predicted}')
    line += 1
#<<<<<<

# From the definitions 
TP_count = confusion_matrix[0, 0]
FP_count = confusion_matrix[0, 1]
TN_count = confusion_matrix[1, 1]
FN_count = confusion_matrix[1, 0]
total_count = TP_count + FP_count + TN_count + FN_count

# Calculate accuracy, precision, and recall
#>>>>>
accuracy = (TP_count + TN_count) / (max(1, total_count))
precision = (TP_count) / (max(1, TP_count + FP_count))
recall = (TP_count) / (max(1, TP_count + FN_count))
#<<<<<

if len(invalid_sequence_lines) > 0:
    print(f'Warning: {SEQUENCES} contains invalid input on lines: {invalid_sequence_lines}')
if len(invalid_true_lines) > 0:
    print(f'Warning: {TRUE_LABELS} contains invalid input on lines: {invalid_true_lines}')

print ('Prediction Algorithm Results')
print ('Accuracy: ' + '{:.1%}'.format(accuracy))
print ('Precision: ' + '{:.1%}'.format(precision))
print ('Recall: ' + '{:.1%}'.format(recall))

