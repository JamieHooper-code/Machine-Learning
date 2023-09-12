import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Load the heart disease dataset
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/heart-disease/processed.cleveland.data"
column_names = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal', 'target']
data = pd.read_csv(url, names=column_names, na_values="?")

# Preprocessing data for decision trees:
# 1. Handling Missing Values: Ensure that the dataset does not contain any missing values. You can use methods like imputation to fill missing values.
data = data.dropna()

# 2. Encoding Categorical Variables: Convert necessary columns to one-hot encoded columns.
categorical_columns = ['cp', 'restecg', 'slope', 'thal']
data = pd.get_dummies(data, columns=categorical_columns)

# Convert the target column to a binary categorical variable (0 or 1)
data['target'] = data['target'].apply(lambda x: 1 if x > 0 else 0)

# 3. Feature Scaling: Although decision trees do not require feature scaling, it might be necessary if you plan to use other algorithms alongside.
# (Not necessary for this dataset)

# 4. Feature Selection: You might consider performing feature selection to remove irrelevant features, although decision trees can handle irrelevant features quite well.
# (Not necessary for this dataset)

X = data.drop('target', axis=1)
y = data['target']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a decision tree instance
clf = DecisionTreeClassifier(random_state=42)

# Fit the model to the training data to find effective alphas
clf.fit(X_train, y_train)

# Predict the labels of the test set using the original model
y_pred_original = clf.predict(X_test)

# Calculate the accuracy of the original model
accuracy_original = accuracy_score(y_test, y_pred_original)
print(f"Original Model Test Accuracy: {accuracy_original}")

# Get the effective alphas and their corresponding impurities
path = clf.cost_complexity_pruning_path(X_train, y_train)
ccp_alphas, impurities = path.ccp_alphas, path.impurities

# Set up grid of hyperparameters for cost complexity pruning
param_grid = {
    'ccp_alpha': ccp_alphas,
    'max_depth': [None, 2, 4, 6, 8, 10],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
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
print(f"Pruned Model Test Accuracy: {accuracy}")
