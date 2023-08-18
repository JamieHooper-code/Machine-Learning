import sklearn
from sklearn import svm, datasets, metrics
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from matplotlib import style
import pickle


# svm algorithm function to run the algorithm as many times as I call it and return the best accuracy
def svm(X, y):
    best = 0
    for _ in range(1):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1)

        # Create model
        model = SVC(kernel='linear')

        # Train model
        model.fit(X_train, y_train)

        y_predicted = model.predict(X_test)

        # Test model
        acc = metrics.accuracy_score(y_test, y_predicted)
        if acc > best:
            best = acc
    return best, model, X_test, y_test, y_predicted

def main():
    cancer = datasets.load_breast_cancer()

    # Create features and labels
    X = cancer.data
    y = cancer.target

    # called the best accuracy function
    best, model, X_test, y_test, y_predicted = svm(X, y)

    print('Accuracy: ', best)

    # Predict
    names = cancer.target_names

    # Save model
    with open('cancer_model.pickle', 'wb') as f:
        pickle.dump(model, f)

    # Load model
    pickle_in = open('cancer_model.pickle', 'rb')
    model = pickle.load(pickle_in)

    #     print results
    for x in range(len(y_predicted)):
        print('Predicted: ', names[y_predicted[x]], 'Data: ', X_test[x], 'Actual: ', names[y_test[x]])
    print('Accuracy: ', best)

    print(cancer)
    # graph result
    p = 'area1'
    style.use('ggplot')
    plt.scatter(cancer[p], cancer['target'])
    plt.xlabel(p)
    plt.ylabel('Tumor Size')
    plt.show()



main()