import csv
import os

from sklearn.naive_bayes import CategoricalNB
from sklearn.preprocessing import OrdinalEncoder
# os.environ['OPENBLAS_NUM_THREADS'] = '1'
# from submission_script import *
# from dataset_script import dataset

def read_csv_file(path):
    with open(path) as doc:
        csv_reader = csv.reader(doc, delimiter=",")
        dataset = list(csv_reader)[1:] 
        
    return dataset
if __name__ == '__main__':
    # Vashiot kod tuka
    
    dataset = read_csv_file('data.csv')

    encoder = OrdinalEncoder()
    encoder.fit([row[:-1] for row in dataset])
    
    train_set = dataset[:int(0.75 * len(dataset))]
    train_X = [row[:-1] for row in train_set]     
    train_Y = [row[-1] for row in train_set]
    

    test_set = dataset[int(0.75 * len(dataset)):]
    test_X = [row[:-1] for row in test_set]     
    test_Y = [row[-1] for row in test_set] 
     
    train_X = encoder.transform(train_X)    
    test_X = encoder.transform(test_X)   
    
    classifier = CategoricalNB()
    classifier.fit(train_X, train_Y) 

    train_accuracy = classifier.score(train_X, train_Y)

    test_accuracy = classifier.score(test_X, test_Y)

    new_sample = input()
    new_sample = new_sample.split(' ')
    new_sample = encoder.transform([new_sample])    

    predicted_class = classifier.predict(new_sample)[0]
    probabilities = classifier.predict_proba(new_sample)

    print(test_accuracy)
    print(predicted_class)
    print(probabilities)
    
    
    
    
    # Na kraj potrebno e da napravite submit na podatochnoto mnozestvo,
    # klasifikatorot i encoderot so povik na slednite funkcii
    
    # submit na trenirachkoto mnozestvo
    # submit_train_data(train_X, train_Y)
    
    # submit na testirachkoto mnozestvo
    # submit_test_data(test_X, test_Y)
    
    # submit na klasifikatorot
    # submit_classifier(classifier)
    
    # submit na encoderot
    # submit_encoder(encoder)
