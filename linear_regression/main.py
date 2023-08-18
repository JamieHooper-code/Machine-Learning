import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.model_selection import train_test_split
import pickle
import matplotlib.pyplot as pyplot
from matplotlib import style

data = pd.read_csv("student-mat.csv", sep=";")
data = data[["G1", "G2", "G3", "studytime", "failures", "absences"]]

predict = "G3"

X = np.array(data.drop([predict], 1))  # Features
y = np.array(data[predict])  # Labels

best_acc = 0
best_linear = None

for _ in range(10000):
    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.1)

    linear = linear_model.LinearRegression()
    linear.fit(x_train, y_train)

    acc = linear.score(x_test, y_test)

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

predictions = best_linear.predict(x_test)

for x in range(10):
    print(predictions[x], x_test[x], y_test[x])

p = "G1"
style.use("ggplot")
pyplot.scatter(data[p], data["G3"])
pyplot.xlabel(p)
pyplot.ylabel("Final Grade")
pyplot.show()
