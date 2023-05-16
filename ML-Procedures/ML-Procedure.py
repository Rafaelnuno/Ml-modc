from sklearn.datasets import load_arff
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

train_data_path = "path/to/nsl-kdd-dataset/KDDTrain+.arff"
test_data_path = "path/to/nsl-kdd-dataset/KDDTest+.arff"

train_data, train_meta = load_arff(train_data_path)
test_data, test_meta = load_arff(test_data_path)

