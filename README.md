# Student Pass/Fail Prediction model Using AI

## Project Overview

This project is a simple Machine Learning based system that predicts whether a student will Pass or Fail based on:

- Study Hours
- Attendance Percentage
- Previous Marks
- Assignment Completion

The project uses the Decision Tree Classification algorithm from Scikit-learn.


# Technologies Used

- Python
- Pandas
- Scikit-learn


# Files Used

| File Name | Description |
|---|---|
| student_pass_fail_prediction.py | Main Python program |
| student_data.csv | Dataset file |
| README.md | Project documentation |


# Dataset Information

The dataset contains student academic details.


### Dataset Columns

| Column Name | Description |
|---|---|
| StudyHours | Daily study hours |
| Attendance | Attendance percentage |
| PreviousMarks | Previous exam marks |
| Assignments | Assignment status (1 = Yes, 0 = No) |
| Result | Pass or Fail |


## Decision Tree Classifier

The Decision Tree algorithm learns patterns from student data and predicts whether a student may pass or fail.


# Features

- Reads dataset from CSV file
- Splits data into training and testing sets
- Trains Machine Learning model
- Predicts student result
- Shows model accuracy
- Takes user input dynamically


# How to Run the Project

```bash
python3 student_pass_fail_prediction.py
```


# Example Input

```text
Enter study hours : 5
Enter attendance percentage : 80
Enter previous marks : 65
Assignment completed (1 yes / 0 no) : 1
```


# Example Output

```text
Model Accuracy : 100.0 %

Prediction : Pass
```


# Project Workflow

```text
Load Dataset
      ↓
Split Dataset
      ↓
Train Model
      ↓
Check Accuracy
      ↓
Take User Input
      ↓
Predict Pass/Fail
```


# Future Improvements

- Add graphical user interface (GUI)
- Add larger dataset
- Create web application using Flask
- Improve prediction accuracy
- Store student records



# Conclusion

This project demonstrates the basic implementation of Machine Learning classification using Python and Scikit-learn. It predicts student performance based on academic details and helps understand supervised learning concepts.


# Author

Sarth Patel
