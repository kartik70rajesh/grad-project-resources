from sklearn import datasets
from sklearn import svm
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split as tts
from sklearn.metrics import accuracy_score

train_news = pd.read_csv(train_filename)
test_news = pd.read_csv(test_filename)
valid_news = pd.read_csv(valid_filename)


#split the data into training and testing
train_feats, test_feats, train_labels, test_labels = tts(features, labels, test_size=0.2)


clf = RandomForestClassifier()



# print the details of the Classifier used
print("Using", clf)

# training
clf.fit(train_feats, train_labels)

# predictions
predictions = clf.predict(test_feats)
print("\nPredictions:" , predictions)

score = 0
for i in range(len(predictions)):
    if predictions[i] == test_labels[i]:
        score += 1
print ("Accuracy:", (score / len(predictions)) * 100, "%")

# or, just do this for accuracy
# print accuracy_score(test_labels, predictions)
