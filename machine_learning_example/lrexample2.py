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

# PROCESS DATA
X = np.array(data.drop([label], 1))  # Features
y = np.array(data[label])  # Labels

# SPLIT DATA INTO TRAINING AND TESTING SETS
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.1)

# PICK MODEL AND TRAIN
linear = linear_model.LinearRegression()
linear.fit(x_train, y_train)

# TEST MODEL
acc = linear.score(x_test, y_test)

# PRINT RESULTS
print("Accuracy:", acc)

# PREDICT
predictions = linear.predict(x_test)

# SAVE MODEL
with open("best_student_model.pickle", "wb") as f:
    pickle.dump(linear, f)
    print("Model saved")

