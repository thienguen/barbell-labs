import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix, accuracy_score, recall_score, f1_score, log_loss

# Step 1: Define the current directory and file path for the dataset
current_directory = os.path.dirname(os.path.realpath(__file__))
file_name = 'data.csv'
file_path = os.path.join(current_directory, file_name)

# Step 2: Read the dataset into a pandas DataFrame
data = pd.read_csv(file_path)

# Step 3: Preprocess the data by dropping columns with all NaN values
data = data.dropna(axis=1, how='all')
print(data)

# Step 4: Separate features (X) and target (y) variables
y = data['diagnosis']
X = data.drop('diagnosis', axis=1)

# Step 5: Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=83)

# Step 6: Standardize the features using StandardScaler
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Step 7: Initialize the Naive Bayes classifier
model = GaussianNB()

# Step 8: Train the Naive Bayes classifier on the training data
model.fit(X_train, y_train)

# Step 9: Make predictions on the training data
train_predictions = model.predict(X_train)

# Step 10: Evaluate the model's performance on the training data
for label in ['B', 'M']:
    indices = (y_train == label)
    y_train_binary = (y_train == label)
    train_predictions_binary = (train_predictions == label)
    tn, fp, fn, tp = confusion_matrix(y_train_binary, train_predictions_binary).ravel()
    specificity = tn / (tn + fp) if (tn + fp) != 0 else 0
    print(f"\nMetrics for class '{label}' on the Training Set:")
    print(f"Accuracy for '{label}': {accuracy_score(y_train[indices], train_predictions[indices])}")
    print(f"Sensitivity for '{label}': {recall_score(y_train[indices], train_predictions[indices], pos_label=label, zero_division='warn')}")
    print(f"Specificity for '{label}': {specificity}")
    print(f"F1 Score for '{label}': {f1_score(y_train[indices], train_predictions[indices], pos_label=label)}")

# Step 11: Make predictions on the testing data
y_pred = model.predict(X_test)
test_predictions = model.predict(X_test)

# Step 12: Evaluate the model's performance on the testing data
for label in ['B', 'M']:
    indices = (y_test == label)
    y_test_binary = (y_test == label)
    test_predictions_binary = (test_predictions == label)
    tn, fp, fn, tp = confusion_matrix(y_test_binary, test_predictions_binary).ravel()
    specificity = tn / (tn + fp) if (tn + fp) != 0 else 0
    print(f"\nMetrics for class '{label}' on the Test Set:")
    print(f"Accuracy for '{label}': {accuracy_score(y_test[indices], test_predictions[indices])}")
    print(f"Sensitivity for '{label}': {recall_score(y_test[indices], test_predictions[indices], pos_label=label, zero_division='warn')}")
    print(f"Specificity for '{label}': {specificity}")
    print(f"F1 Score for '{label}': {f1_score(y_test[indices], test_predictions[indices], pos_label=label)}")
    print(f"Log Loss for '{label}': {log_loss(y_test_binary, model.predict_proba(X_test)[:, model.classes_ == label])}")
