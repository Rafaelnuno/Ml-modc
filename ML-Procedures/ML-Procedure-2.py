import pandas as pd
import arff
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

train_data_path = "dataset/KDDTrain+.arff"
test_data_path = "dataset/KDDTest+.arff"

# Load ARFF files
train_data_arff = list(arff.load(train_data_path))
test_data_arff = list(arff.load(test_data_path))

# Convert ARFF data to pandas dataframes
train_data = pd.DataFrame(train_data_arff[0])
test_data = pd.DataFrame(test_data_arff[0])

# Split the data into features and labels
train_features = train_data.drop(columns=[train_data.columns[-1]])
train_labels = train_data[train_data.columns[-1]]
test_features = test_data.drop(columns=[test_data.columns[-1]])
test_labels = test_data[test_data.columns[-1]]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(train_features, train_labels, test_size=0.2, random_state=42)

# Create a decision tree classifier
classifier = DecisionTreeClassifier()

# Fit the classifier on the training data
classifier.fit(X_train, y_train)

# Make predictions on the test data
predictions = classifier.predict(X_test)

# Calculate the accuracy of the classifier
accuracy = accuracy_score(y_test, predictions)
print("Accuracy:", accuracy)
