Markdown# AI and ML for Cybersecurity – Midterm Exam  
**Student:** Giorgi Ghvdeladze  
**Date:** January 2026  

This repository contains my solutions for both parts of the midterm exam.

## 1. Finding the Correlation (10 points)

### What I did
- I opened the online graph at: `max.ge/aiml_midterm/47631_html`  
- I manually collected the blue data points by hovering the mouse over them and writing down the (x, y) coordinates.  
- I got these 10 points:
(-9, 6), (-7.4, 5), (-5, 3), (-3, 4), (-1, 1),
(1, 0), (3, -2), (5, -3), (7, -4), (9, -5)
text### Method
I used Python and NumPy library to calculate **Pearson's correlation coefficient**.

### Result
**Pearson's r ≈ -0.97**  
This is a **very strong negative correlation**.  
When x goes up, y goes down almost in a straight line.

### Code
See file: [`finding the correlation/correlation.py`](./finding%20the%20correlation/correlation.py)

### Visualization
Here is the scatter plot that shows the points and the strong negative relationship:

![Correlation Scatter Plot](finding%20the%20correlation/correlation_plot.png)

(You can also see another version: `Figure_1.png`)

---

## 2. Spam Email Detection (20 points)

### 1. Data file
I uploaded the given CSV file to the repository.  
File name: `g_ghvdeladze_47631.csv`  
Link: [`spam email detection/g_ghvdeladze_47631.csv`](./spam%20email%20detection/g_ghvdeladze_47631.csv)

### 2. Model – Logistic Regression
- I used 70% of data for training  
- I used **Logistic Regression** from scikit-learn  
- Code is here: [`spam email detection/spam_classifier.py`](./spam%20email%20detection/spam_classifier.py)

In the code you can find:
- How I load and prepare the data
- How I split data (train/test)
- How I train Logistic Regression model
- The **coefficients** of the model (printed in console)

### 3. Validation on test data
I tested the model on the remaining 30% of data.  
Results (from my run):

- **Confusion Matrix**  
- **Accuracy**: (you should write your real number here, for example: 0.935 or 93.5%)

See file: [`spam email detection/confusion_matrix.png`](./spam%20email%20detection/confusion_matrix.png)

Code for confusion matrix and accuracy is also in `spam_classifier.py`

### 4. How to check new email text
The program can:
- Take any email text
- Extract the same features as in the CSV file
- Predict if it is spam or legitimate  
(You can see this part at the bottom of `spam_classifier.py`)

### 5. Email that should be classified as SPAM
**My spam email example:**
Subject: WIN $1,000,000 RIGHT NOW!!!
Dear friend,
You are the lucky winner of our big lottery!
Click here to claim your prize: http://get-money-now.com/claim
Send us your bank details fast before offer ends!
Best regards,
Lottery Team
text**Why spam?**  
It has typical spam words (win, prize, claim, money, click here, urgent), fake offer, and link to suspicious website.

### 6. Email that should be classified as LEGITIMATE
**My legitimate email example:**
Subject: Meeting reminder – Project update tomorrow
Hi team,
Just a quick reminder that we have our project status meeting tomorrow at 11:00 in room 305.
Please bring your latest progress report.
See you there!
Best,
Giorgi
text**Why legitimate?**  
Normal work email, no suspicious words, no money/prize, no links to strange sites, just regular office communication.

### 7. Two Visualizations

**Visualization 1 – Class Distribution**  
Shows how many spam and legitimate emails are in the dataset.

![Class Distribution](spam%20email%20detection/class_distribution.png)

**What it shows:**  
The graph helps us see if we have more spam or more legitimate emails.  
If the classes are very unbalanced, it can make the model harder to train well.

**Code:** You can find it in `spam_classifier.py` (matplotlib/seaborn part)

**Visualization 2 – Confusion Matrix Heatmap**

![Confusion Matrix Heatmap](spam%20email%20detection/confusion_matrix.png)

**What it shows:**  
This picture shows how many predictions were correct and wrong.  
The numbers on the diagonal (top-left and bottom-right) are correct predictions.

**Code:** Also in `spam_classifier.py`

---

Good luck with evaluation!  
Repository will stay public until grades are out.