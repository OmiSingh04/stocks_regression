from sklearn.datasets import load_iris
import numpy as np
from sklearn import tree
iris = load_iris()
print (iris.feature_names)
print (iris.target_names)
print (iris.data[0])
#here target means labels
#now writing the classifier
#we will divide the data into two sets, one for learning and one for testing

iris = load_iris()
test_idx = [0,50,100]
# we are going to be extracting these three examples, one being each type of flower.

#training data
train_target = np.delete(iris.target, test_idx)
train_features = np.delete(iris.data, test_idx, axis = 0)

#testing data
test_target = iris.target[test_idx]
test_data = iris.data[test_idx]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(train_features, train_target)
print(test_target)
print(clf.predict(test_data))