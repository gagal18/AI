import os
os.environ['OPENBLAS_NUM_THREADS'] = '1'
from submission_script import *
from dataset_script import dataset
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
    
    
    x = int(input())
    estimators = int(input())
    characteristic = input()
    print()
    dataset = remove_column(dataset, x)
    
    train_set = dataset[:int(0.85 * len(dataset))]
    train_X = [row[:-1] for row in train_set]     
    train_Y = [row[-1] for row in train_set]
    
    test_set = dataset[int(0.85 * len(dataset)):]
    test_X = [row[:-1] for row in test_set]     
    test_Y = [row[-1] for row in test_set]   
    
    forestClassifier = RandomForestClassifier(n_estimators=estimators, criterion=characteristic, random_state=0)
    forestClassifier.fit(train_X, train_Y)
    

    # new_sample = encoder.transform([new_sample])  
    
    accuracy = classifier_accuracy(forestClassifier, test_X, test_Y)
    
    
    new_sample = input()
    new_sample = [float(el) for el in new_sample.split(' ')]
    del new_sample[x]
    
    print(f'Accuracy: {accuracy}')
    print(forestClassifier.predict([new_sample])[0])
    print(forestClassifier.predict_proba([new_sample]))
    
    
    
    
    # Na kraj potrebno e da napravite submit na podatochnoto mnozestvo
    # i klasifikatorot so povik na slednite funkcii
    
    # submit na trenirachkoto mnozestvo
    submit_train_data(train_X, train_Y)
    
    # submit na testirachkoto mnozestvo
    submit_test_data(test_X, test_Y)
    
    # submit na klasifikatorot
    submit_classifier(forestClassifier)
