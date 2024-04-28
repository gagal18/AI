import csv
import os

from sklearn.naive_bayes import GaussianNB
os.environ['OPENBLAS_NUM_THREADS'] = '1'
# from submission_script import *
# from dataset_script import dataset


def read_csv_file(path):
    dataset = None
    with open(path) as doc:
        csv_reader = csv.reader(doc, delimiter=",")
        dataset = list(csv_reader)[1:] 

    return dataset

def map_dataset(dataset):
    dataset_mp = []
    for row in dataset:
        int_list = list(map(float, row))
        dataset_mp.append(int_list)
    return dataset_mp


if __name__ == '__main__':
    # Vashiot kod tuka
    
    
    dataset = read_csv_file('data.csv')
    dataset = map_dataset(dataset)
    train_set = dataset[:int(0.85 * len(dataset))]
    train_X = [row[:-1] for row in train_set]     
    train_Y = [row[-1] for row in train_set]
    

    test_set = dataset[int(0.85 * len(dataset)):]
    test_X = [row[:-1] for row in test_set]     
    test_Y = [row[-1] for row in test_set] 
     
    
    classifier = GaussianNB()
    classifier.fit(train_X, train_Y) 

    test_accuracy = classifier.score(test_X, test_Y)

    new_sample = input()
    new_sample = [float(el) for el in new_sample.split(' ')]
    predicted_class = classifier.predict([new_sample])[0]
    probabilities = classifier.predict_proba([new_sample])
    print(test_accuracy)
    print(int(predicted_class))
    print(probabilities)
    
    
    
    
    # Na kraj potrebno e da napravite submit na podatochnoto mnozestvo,
    # klasifikatorot i encoderot so povik na slednite funkcii
    
    # submit na trenirachkoto mnozestvo
    # submit_train_data(train_X, train_Y)
    
    # submit na testirachkoto mnozestvo
    # submit_test_data(test_X, test_Y)
    
    # submit na klasifikatorot
    # submit_classifier(classifier)
    
    # povtoren import na kraj / ne ja otstranuvajte ovaa linija
