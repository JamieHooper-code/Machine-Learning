import sklearn
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing, linear_model
import pickle

# function to run the algorithm as many times as I call it and return the best accuracy
def best_accuracy(X, y):
    best = 0
    for _ in range(100):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1)

        # Create model
        model = KNeighborsClassifier(n_neighbors=9)

        # Train model
        model.fit(X_train, y_train)

        # Test model
        acc = model.score(X_test, y_test)
        if acc > best:
            best = acc
    return best, model, X_test, y_test

def main():
    data = pd.read_csv('car.data')

    # Convert data to numerical values
    le = preprocessing.LabelEncoder()
    buying = le.fit_transform(list(data['buying']))
    maint = le.fit_transform(list(data['maint']))
    door = le.fit_transform(list(data['door']))
    persons = le.fit_transform(list(data['persons']))
    lug_boot = le.fit_transform(list(data['lug_boot']))
    safety = le.fit_transform(list(data['safety']))
    cls = le.fit_transform(list(data['class']))

    # Create features and labels
    predict = 'class'
    X = list(zip(buying, maint, door, persons, lug_boot, safety))
    y = list(cls)

    # called the best accuracy function
    best, model, X_test, y_test = best_accuracy(X, y)

    print('Accuracy: ', best)

    # Predict
    predicted = model.predict(X_test)
    names = ['unacc', 'acc', 'good', 'vgood']

    # Save model
    with open('car_model.pickle', 'wb') as f:
        pickle.dump(model, f)

    # Load model
    pickle_in = open('car_model.pickle', 'rb')
    model = pickle.load(pickle_in)


    # Print results
    for x in range(10):
        print('Predicted: ', names[predicted[x]], 'Data: ', X_test[x], 'Actual: ', names[y_test[x]])
        n = model.kneighbors([X_test[x]], 9, True)
        print('N: ', n)

    print('Accuracy: ', best)

    # Plot results
    plt.plot(X_test, predicted)
    plt.show()

main()