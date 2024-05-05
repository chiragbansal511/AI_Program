import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.preprocessing import StandardScaler


test = pd.read_csv("q1.csv")


test["test_score(out of 10)"] = test["test_score(out of 10)"].fillna(test["test_score(out of 10)"].mean())


X = test[["experience", "test_score(out of 10)", "interview_score(out of 10)"]]
y = test[["salary"]]


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.01)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

knn = KNeighborsRegressor(n_neighbors=5)



knn.fit(X_train_scaled, y_train)

candidates = [
    {'experience': 5, 'test_score(out of 10)': 8, 'interview_score(out of 10)':10},
    {'experience': 8, 'test_score(out of 10)': 7, 'interview_score(out of 10)': 6}
]

for candidate in candidates:
    candidate_data = scaler.transform([[candidate['experience'], candidate['test_score(out of 10)'], candidate['interview_score(out of 10)']]])
    predicted_salary = knn.predict(candidate_data)
    print("Predicted salary for candidate with " + str(candidate['experience']) + " years of experience, " +
          str(candidate['test_score(out of 10)']) + " written score, and " + str(candidate['interview_score(out of 10)']) +
          " interview score: $" + str(predicted_salary[0]))
