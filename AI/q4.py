import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

data = pd.read_csv("q2,4.csv")

X = data[['Graduation Percentage', 'Experience', 'Written Score', 'Interview Score']]
y = data['Selection']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
knn_classifier = KNeighborsClassifier()
nb_classifier = GaussianNB()
dt_classifier = DecisionTreeClassifier()

classifiers = {
    "KNN Classifier": knn_classifier,
    "Naive Bayes Classifier": nb_classifier,
    "Decision Tree Classifier": dt_classifier
}

results = {}
for clf_name, clf in classifiers.items():
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    results[clf_name] = {
        "Accuracy": accuracy
    }

results_df = pd.DataFrame(results)
print(results_df)

results_df.to_csv("q4.csv")

sample = pd.DataFrame({
    'Graduation Percentage': [90],
    'Experience': [5],
    'Written Score': [8],
    'Interview Score': [10]
})

predictions = {}
for clf_name, clf in classifiers.items():
    prediction = clf.predict(sample)
    predictions[clf_name] = prediction

print("Predictions for one sample:")
print(predictions)
