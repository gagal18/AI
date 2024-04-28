import csv
from sklearn.naive_bayes import CategoricalNB
from sklearn.preprocessing import OrdinalEncoder

def read_csv_file(path):
    with open(path) as doc:
        csv_reader = csv.reader(doc, delimiter=",")
        dataset = list(csv_reader)[1:] 
        
    return dataset

if __name__ == "__main__":
    dataset = read_csv_file('car.csv')
    # print(dataset)
    
    encoder = OrdinalEncoder()
    encoder.fit([row[:-1] for row in dataset])
    
    train_set = dataset[:int(0.7 * len(dataset))]
    train_in = [row[:-1] for row in train_set]     
    train_out = [row[-1] for row in train_set]
    

    test_set = dataset[int(0.7 * len(dataset)):]
    test_in = [row[:-1] for row in test_set]     
    test_out = [row[-1] for row in test_set] 
     
    train_in_encoder = encoder.transform(train_in)    
    test_in_encoder = encoder.transform(test_in)   
    
    classifier = CategoricalNB()
    classifier.fit(train_in_encoder, train_out) 
    
    # Calculate accuracy on the training set
    train_accuracy = classifier.score(train_in_encoder, train_out)
    print(f'Training set accuracy: {train_accuracy}')
    
    # Calculate accuracy on the testing set
    test_accuracy = classifier.score(test_in_encoder, test_out)
    print(f'Testing set accuracy: {test_accuracy}')
    
    new_sample = input("Enter a new sample (comma-separated): ")
    new_sample = new_sample.split(',')
    new_sample_encoder = encoder.transform([new_sample])    
    
    predicted_class = classifier.predict(new_sample_encoder)[0]
    probabilities = classifier.predict_proba(new_sample_encoder)
    
    print(f'New sample: {new_sample_encoder}')
    print(f'Predicted class: {predicted_class}')
    print(f'Probabilities for each class: {probabilities}')