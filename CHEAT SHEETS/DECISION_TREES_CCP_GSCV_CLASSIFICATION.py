# DECISION TREES WITH COST COMPLEXITY PRUNING (CCP) - GRID SEARCH CV - IRIS DATASET - CLASSIFICATION PROBLEM - SCIKIT-LEARN - PYTHON

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score

# Load dataset
iris = load_iris()
X, y = iris.data, iris.target

# Preprocessing data for decision trees:
# 1. Handling Missing Values: Ensure that the dataset does not contain any missing values. You can use methods like imputation to fill missing values.
# 2. Encoding Categorical Variables: If the dataset contains categorical variables, encode them using techniques such as one-hot encoding or label encoding.
# 3. Feature Scaling: Although decision trees do not require feature scaling, it might be necessary if you plan to use other algorithms alongside.
# 4. Feature Selection: You might consider performing feature selection to remove irrelevant features, although decision trees can handle irrelevant features quite well.

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a decision tree instance
clf = DecisionTreeClassifier(random_state=42)

# Fit the model to the training data to find effective alphas
clf.fit(X_train, y_train)

# Get the effective alphas and their corresponding impurities
path = clf.cost_complexity_pruning_path(X_train, y_train)
ccp_alphas, impurities = path.ccp_alphas, path.impurities

# Set up grid of hyperparameters for cost complexity pruning
param_grid = {
    'ccp_alpha': ccp_alphas,
    'max_depth': [None, 2, 4, 6, 8, 10]
}

# Set up cross-validation grid search
grid_search = GridSearchCV(clf, param_grid, cv=5, scoring='accuracy')

# Fit the model to the training data
grid_search.fit(X_train, y_train)

# Get the best parameters from the grid search
best_params = grid_search.best_params_

# Train a new classifier using the best parameters found
best_clf = DecisionTreeClassifier(ccp_alpha=best_params['ccp_alpha'], max_depth=best_params['max_depth'], random_state=42)
best_clf.fit(X_train, y_train)

# Predict the labels of the test set
y_pred = best_clf.predict(X_test)

# Calculate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)

print(f"The best parameters are {best_params} with a score of {grid_search.best_score_}")
print(f"Test Accuracy: {accuracy}")
