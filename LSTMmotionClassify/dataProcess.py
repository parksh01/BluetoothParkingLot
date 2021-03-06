import csv
import numpy as np

# takes array of labels as input, and generates dictionary for converting into integer, or vice versa.
def label(labels):
    label2num = {}
    num2label = {}
    n = 0
    for i in labels:
        label2num[i] = n
        num2label[n] = i
        n = n + 1
    return label2num, num2label

def load_testcases(path, sliceSize, label2num):
    # First, read file and store in array
    num_classes = len(label2num)
    f = open(path, 'r')
    print("Now reading : " + path)
    X_test = []
    y_test = []
    rdr = csv.reader(f)
    linecount = 0
    for line in rdr:
        if linecount == 0:
            linecount = linecount + 1
        else:
            temp = []
            for i in range(num_classes):
                temp.append(float(line[i].strip()))
            X_test.append(temp)
            y_test.append(oneHotEncode(label2num[line[num_classes]], num_classes))
            linecount = linecount + 1
    f.close()
    # then slice it.
    slicedData = sliceData(X_test, sliceSize)
    slicedLabel = []
    for i in range(0, linecount - sliceSize):
        slicedLabel.append(y_test[i + int(sliceSize/2)])
    return np.array(slicedData).reshape(-1, sliceSize, num_classes), np.array(slicedLabel).reshape(-1, num_classes)

# Do one hot encoding with given category number.
def oneHotEncode(whichCategory, howMany):
    encoded = []
    for i in range(howMany):
        if i == whichCategory:
            encoded.append(1)
        else:
            encoded.append(0)
    return encoded

# read csv file and returns array.
def read_csv(path):
    f = open(path, 'r')
    print("Now reading : " + path)
    rows = []
    rdr = csv.reader(f)
    linecount = 0
    for line in rdr:
        if linecount == 0:
            linecount = linecount + 1
        else:
            temp = []
            for i in range(6):
                temp.append(float(line[i].strip()))
            rows.append(temp)
            linecount = linecount + 1
    f.close()
    return rows

# sliceSize = 100, sliceNum = 100 will be suitable.
def sliceData(data, sliceSize):
    rows = len(data)
    startingPoints = range(0, rows - sliceSize)
    slicedData = []
    for i in startingPoints:
        slicedData.append(data[i:i+sliceSize])
    return slicedData

# path : array of paths of testcases
# category : category number of each testcase files
# sliceSize : slice dataset by this size (100 will be suitable)
# test_split : split testcases and training dataset
def load_data(path, category, sliceSize, test_split):
    X_train = []
    y_train = []
    X_test = []
    y_test = []
    for i in range(len(path)):
        slicedData = sliceData(read_csv(path[i]), sliceSize)
        testCases = int(len(slicedData) * test_split)
        X_train = X_train + slicedData[testCases:]
        y_train = y_train + (oneHotEncode(category[i], len(set(category))) * (len(slicedData) - testCases))
        X_test = X_test + slicedData[:testCases]
        y_test = y_test + (oneHotEncode(category[i], len(set(category))) * testCases)
    return (X_train, y_train), (X_test, y_test)
