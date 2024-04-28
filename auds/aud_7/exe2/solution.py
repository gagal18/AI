import csv
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import OrdinalEncoder

def read_csv_file(path):
    dataset = None
    with open(path) as doc:
        csv_reader = csv.reader(doc, delimiter=",")
        dataset = list(csv_reader)[1:] 
    dataset_int = []
    # Mapping in ints so no encoder will be needed since all data will be given as numbers
    for row in dataset:
        int_list = list(map(int, row))
        dataset_int.append(int_list)
    return dataset_int

if __name__ == "__main__":
    dataset = read_csv_file('medical_data.csv')
    # print(dataset)
    
    train_set = dataset[:int(0.7 * len(dataset))]
    train_in = [row[:-1] for row in train_set]     
    train_out = [row[-1] for row in train_set]
    

    test_set = dataset[int(0.7 * len(dataset)):]
    test_in = [row[:-1] for row in test_set]     
    test_out = [row[-1] for row in test_set] 
    
    
    classifier = GaussianNB()
    
    classifier.fit(train_in, train_out)
    
    # Calculate accuracy on the training set
    train_accuracy = classifier.score(train_in, train_out)
    print(f'Training set accuracy: {train_accuracy}')


    new_sample = input()
    new_sample = [int(el) for el in new_sample.split(',')]

    predicted_class = classifier.predict([new_sample])[0]
    probabilities = classifier.predict_proba([new_sample])

    print(f'Nov primerok: {new_sample}')
    print(f'Predvidena klasa: {predicted_class}')
    print(f'Verojatnosti za pripadnost vo klasite: {probabilities}')

    print()