# AI and ML for Cybersecurity – Midterm Exam

**Student:** Giorgi Ghvdeladze  
**Date:** January 2026  

This repository contains my solutions for the midterm exam (both tasks).

---

## 1. Finding the Correlation (10 points)

### What I did
- I opened the online graph at: `max.ge/aiml_midterm/47631_html`
- I manually collected the blue points by hovering the mouse over them
- I wrote down the (x, y) values
- I collected these 10 points:

(-9, 6), (-7.4, 5), (-5, 3), (-3, 4), (-1, 1),  
(1, 0), (3, -2), (5, -3), (7, -4), (9, -5)

### Method
I used **Python** with the **NumPy** library to calculate **Pearson correlation coefficient**.

### Result
**Pearson’s r ≈ -0.97**

This means there is a **very strong negative correlation**.  
As x increases, y decreases almost in a straight line.

### Code
Python code is here:  
[`finding the correlation/correlation.py`](./finding%20the%20correlation/correlation.py)

### Visualization
Scatter plot showing the data points and their relationship:

![Correlation Scatter Plot](finding%20the%20correlation/correlation_plot.png)

(Another version is saved as `Figure_1.png`)

---

## 2. Spam Email Detection (20 points)

### 1. Dataset
The provided CSV file is uploaded to the repository.

File name: `g_ghvdeladze_47631.csv`  
Link:  
[`spam email detection/g_ghvdeladze_47631.csv`](./spam%20email%20detection/g_ghvdeladze_47631.csv)

---

### 2. Model – Logistic Regression
- I used **70%** of the data for training
- I used **Logistic Regression** from `scikit-learn`
- The main code is here:  
[`spam email detection/spam_classifier.py`](./spam%20email%20detection/spam_classifier.py)

The code includes:
- Loading and preparing the data
- Splitting data into train and test sets
- Training the Logistic Regression model
- Printing model coefficients in the console

---

### 3. Testing the model
The model was tested on the remaining **30%** of the data.

Results from my run:
- Confusion Matrix
- Accuracy score

Confusion matrix image:  
[`spam email detection/confusion_matrix.png`](./spam%20email%20detection/confusion_matrix.png)

The code for accuracy and confusion matrix is also in `spam_classifier.py`.

---

### 4. Predicting a new email
The program can:
- Take a new email text
- Extract the same features as the dataset
- Predict whether the email is **spam** or **legitimate**

This part is implemented at the bottom of `spam_classifier.py`.

---

### 5. Example of SPAM email

**Spam email example:**

Subject: WIN $1,000,000 RIGHT NOW!!!  

Dear friend,  
You are the lucky winner of our big lottery!  
Click here to claim your prize: http://get-money-now.com/claim  
Send us your bank details fast before offer ends!  

Best regards,  
Lottery Team  

**Why spam?**  
It contains common spam words (win, prize, claim, money), fake promises, urgency, and a suspicious link.

---

### 6. Example of LEGITIMATE email

**Legitimate email example:**

Subject: Meeting reminder – Project update tomorrow  

Hi team,  
Just a reminder about our project status meeting tomorrow at 11:00 in room 305.  
Please bring your latest progress report.  

Best,  
Giorgi  

**Why legitimate?**  
Normal work-related email, no suspicious words, no money offers, and no strange links.

---

### 7. Visualizations

#### Visualization 1 – Class Distribution

![Class Distribution](spam%20email%20detection/class_distribution.png)

**Explanation:**  
This graph shows how many spam and legitimate emails are in the dataset.  
It helps to see if the data is balanced or not.

Code is in `spam_classifier.py`.

---

#### Visualization 2 – Confusion Matrix Heatmap

![Confusion Matrix Heatmap](spam%20email%20detection/confusion_matrix.png)

**Explanation:**  
This visualization shows correct and incorrect predictions.  
Values on the diagonal represent correct classifications.

Code is also in `spam_classifier.py`.

---

