import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, classification_report

data = pd.read_csv("q2,4.csv")

X = data.iloc[:,:-1].values
y = data.iloc[:,-1:].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = GaussianNB()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

classification_metrics = classification_report(y_test, y_pred, output_dict=True)


print("Accuracy:", accuracy)


unseen_data = pd.DataFrame({
    'Graduation Percentage': [90, 75],
    'Experience': [5, 8],
    'Written Score': [8, 7],
    'Interview Score': [10, 6]
})

predictions_unseen = model.predict(unseen_data)
print("Predictions for unseen data:", predictions_unseen)

classification_metrics_df = pd.DataFrame(classification_metrics).transpose()
classification_metrics_df.to_csv('q2.csv')
