import arff
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

with open("dataset/KDDTrain+.arff") as train_file:
    train_data = arff.load(train_file)
with open("dataset/KDDTest+.arff") as test_file:
    test_data = arff.load(test_file)

train_features = [row[:-1] for row in train_data['data']]
train_labels = [row[-1] for row in train_data['data']]

test_features = [row[:-1] for row in test_data['data']]
test_labels = [row[-1] for row in test_data['data']]

clf = DecisionTreeClassifier()

clf.fit(train_features, train_labels)

predictions = clf.predict(test_features)

accuracy = accuracy_score(test_labels, predictions)
print("Accuracy:", accuracy)