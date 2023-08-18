import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.model_selection import train_test_split
import pickle

data = pd.read_csv("student-mat.csv", sep=";")
data = data[["G1", "G2", "G3", "studytime", "failures", "absences"]]

predict = "G3"

X = np.array(data.drop([predict], 1))  # Features
y = np.array(data[predict])  # Labels

best_acc = 0
best_linear = None

for _ in range(1000):
    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.1)

    linear = linear_model.LinearRegression()
    linear.fit(x_train, y_train)

    predictions = linear.predict(x_test)
    rounded_predictions = np.round(predictions)  # Round the predictions

    acc = np.mean(rounded_predictions == y_test)  # Calculate accuracy with rounded predictions

    if acc > best_acc:
        best_acc = acc
        best_linear = linear

print("Best accuracy:", best_acc)

with open("best_student_model.pickle", "wb") as f:
    pickle.dump(best_linear, f)

pickle_in = open("best_student_model.pickle", "rb")
best_linear = pickle.load(pickle_in)

print("Co: \n", best_linear.coef_)
print("Intercept: \n", best_linear.intercept_)

for x in range(10):
    print(rounded_predictions[x], x_test[x], y_test[x])
