import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

data = pd.read_csv("Student_data.csv")

x = data[["StudyHours","Attendance","PreviousMarks","Assignments"]]

y = data["Result"]

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2)

model = DecisionTreeClassifier()

model.fit(x_train, y_train)

accuracy = model.score(x_test, y_test)

print("Model Accuracy :", accuracy * 100, "%")

print("\nStudent Pass/Fail Prediction\n")

study_hours = float(input("Enter study hours : "))
attendance = float(input("Enter attendance percentage : "))
previous_marks = float(input("Enter previous marks : "))
assignments = int(input("Assignment completed (1 yes / 0 no) : "))

student = pd.DataFrame([[study_hours,attendance,previous_marks,assignments]],
columns=["StudyHours","Attendance","PreviousMarks","Assignments"])

result = model.predict(student)

print("\nPrediction :", result[0])