import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score

# ===============================
# Load dataset (same folder)
# ===============================
df = pd.read_csv("g_ghvdeladze_47631.csv")

# ===============================
# Automatically detect features and class
# (last column is class)
# ===============================
X = df.iloc[:, :-1]
y = df.iloc[:, -1]

print("Feature columns:")
print(list(X.columns))
print("\nClass column:")
print(y.name)

# ===============================
# Train / Test split (70% / 30%)
# ===============================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# ===============================
# Train Logistic Regression model
# ===============================
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# ===============================
# Print model coefficients
# ===============================
print("\nModel coefficients:")
for feature, coef in zip(X.columns, model.coef_[0]):
    print(f"{feature}: {coef}")

# ===============================
# Model evaluation
# ===============================
y_pred = model.predict(X_test)

cm = confusion_matrix(y_test, y_pred)
accuracy = accuracy_score(y_test, y_pred)

print("\nConfusion Matrix:")
print(cm)

print("\nAccuracy:", accuracy)

# ===============================
# Visualization 1: Class Distribution
# ===============================
plt.figure()
y.value_counts().plot(kind="bar")
plt.title("Spam vs Legitimate Email Distribution")
plt.xlabel("Email Class")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("class_distribution.png")
plt.close()

# ===============================
# Visualization 2: Confusion Matrix Heatmap
# ===============================
plt.figure()
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
plt.title("Confusion Matrix Heatmap")
plt.xlabel("Predicted Class")
plt.ylabel("Actual Class")
plt.tight_layout()
plt.savefig("confusion_matrix.png")
plt.close()

print("\nGraphs saved in current folder:")
print("- class_distribution.png")
print("- confusion_matrix.png")
