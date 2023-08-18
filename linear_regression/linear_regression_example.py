# IMPORT DEPENDENCIES
import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.model_selection import train_test_split
import pickle
import matplotlib.pyplot as pyplot
from matplotlib import style


# IMPORT DATA
data = pd.read_csv("student-mat.csv", sep=";")
data = data[["G1", "G2", "G3", "studytime", "failures", "absences"]]


# CHOOSE LABEL
label = "G3"


# PRINT DATA
print(data.head())
print("\n")
print(data.shape)
print("\n")


input("Press enter to continue...")
print("\n")


# PROCESS DATA
X = np.array(data.drop([label], 1))  # Features
y = np.array(data[label])  # Labels


print("Features: \n", X[:5, :])
print("Labels: \n", y[:5])


input("Press enter to continue...")
print("\n")


# SPLIT DATA INTO TRAINING AND TESTING SETS
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.1)


# PICK MODEL AND TRAIN
linear = linear_model.LinearRegression()
linear.fit(x_train, y_train)


# TEST MODEL
acc = linear.score(x_test, y_test)


# PRINT RESULTS
print("Best accuracy:", acc)
print("Coefficients: ", linear.coef_)
print("Intercept: ", linear.intercept_)


# PREDICT
predictions = linear.predict(x_test)


input("Press enter to continue...")
print("\n")

# PRINT PREDICTIONS
for x in range(3):
    print(f"""
PREDICTED VALUES: {predictions[x]}
INPUT DATA: {x_test[x]}
ACTUAL VALUE: {y_test[x]}
    """)

input("Press enter to continue...")
print("\n")

# PREDICT NEW DATA
new_data = np.array([12, 10, 2, 0, 0])
new_data = new_data.reshape(1, -1)
prediction = linear.predict(new_data)
print("New data: ", new_data)
print("Prediction: ", prediction)



input("Press enter to continue...")
print("\n")


# SAVE MODEL
with open("best_student_model.pickle", "wb") as f:
    pickle.dump(linear, f)
    print("Model saved")

# LOAD MODEL
pickle_in = open("best_student_model.pickle", "rb")
best_linear = pickle.load(pickle_in)
print("Model loaded")


# PLOT DATA
p = "G1"
style.use("ggplot")
pyplot.scatter(data[p], data["G3"])
pyplot.xlabel(p)
pyplot.ylabel("Final Grade")
pyplot.show()

