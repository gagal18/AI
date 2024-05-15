import os
os.environ['OPENBLAS_NUM_THREADS'] = '1'
# from submission_script import *
# from dataset_script import dataset
import csv
from sklearn.ensemble import RandomForestClassifier
# Ova e primerok od podatochnoto mnozestvo, za treniranje/evaluacija koristete ja
# importiranata promenliva dataset
dataset_sample = [[180.0, 23.6, 25.2, 27.9, 25.4, 14.0, 'Roach'],
                  [12.2, 11.5, 12.2, 13.4, 15.6, 10.4, 'Smelt'],
                  [135.0, 20.0, 22.0, 23.5, 25.0, 15.0, 'Perch'],
                  [1600.0, 56.0, 60.0, 64.0, 15.0, 9.6, 'Pike'],
                  [120.0, 20.0, 22.0, 23.5, 26.0, 14.5, 'Perch']]

def write_csv(filename, dataset):
    with open(filename, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        csvwriter.writerows(dataset)

def read_csv_file(path):
    with open(path) as doc:
        csv_reader = csv.reader(doc, delimiter=",")
        dataset = list(csv_reader)[1:] 
        return dataset

def remove_column(dataset, idx):
    for row in dataset:
        del row[idx]
    return dataset

def map_dataset(dataset):
    dataset_mp = []
    for row in dataset:
        int_list = list(map(float, row))
        dataset_mp.append(int_list)
    return dataset_mp


def classifier_accuracy(classifier, test_X, test_Y):
    acc = 0
    for i in range(len(test_X)):
        actual_class = test_Y[i]
        predicted_class = classifier.predict([test_X[i]])[0]
        if actual_class == predicted_class:
            acc += 1

    accuracy = acc / len(test_X)
    return accuracy

if __name__ == '__main__':
    # Vashiot kod tuka
    col_index = int(input())
    
    train_X = [dataset[i][:-1] for i in range(0, int(len(dataset) * 0.85))]
    train_Y = [dataset[i][-1] for i in range(0, int(len(dataset) * 0.85))]
    train_X = [list(row[i] for i in range(0, len(row)) if i != col_index) for row in train_X]

    test_X = [dataset[i][:-1] for i in range(int(len(dataset) * 0.85), len(dataset))]
    test_Y = [dataset[i][-1] for i in range(int(len(dataset) * 0.85), len(dataset))]
    test_X = [list(row[i] for i in range(0, len(row)) if i != col_index) for row in test_X] 
    
    forestClassifier = RandomForestClassifier(n_estimators=int(input()), criterion=input(), random_state=0)
    forestClassifier.fit(train_X, train_Y)
    

    # new_sample = encoder.transform([new_sample])  
    
    accuracy = classifier_accuracy(forestClassifier, test_X, test_Y)
    
    
    new_sample = input()
    new_sample = [float(el) for el in new_sample.split(' ')]
    del new_sample[col_index]
    
    print(f'Accuracy: {accuracy}')
    predicted_class = forestClassifier.predict([new_sample])[0]
    probabilities = forestClassifier.predict_proba([new_sample])
    print(predicted_class)
    print(probabilities[0])
    
    
    
    
    # Na kraj potrebno e da napravite submit na podatochnoto mnozestvo
    # i klasifikatorot so povik na slednite funkcii
    
    # submit na trenirachkoto mnozestvo
    # submit_train_data(train_X, train_Y)
    
    # submit na testirachkoto mnozestvo
    # submit_test_data(test_X, test_Y)
    
    # submit na klasifikatorot
    # submit_classifier(forestClassifier)
