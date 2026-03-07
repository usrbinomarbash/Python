from sklearn.datasets import fetch_openml
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
import seaborn as sns
import random

# 1️⃣ Load data
X, y = fetch_openml("mnist_784", version=1, return_X_y=True)
y = y.astype(int)

# 2️⃣ Normalize
X = X / 255.0

# 3️⃣ Visualize one digit
plt.imshow(X.iloc[0].values.reshape(28,28), cmap="gray")
plt.title(f"Label: {y.iloc[0]}")
plt.axis("off")
plt.show()

# 4️⃣ Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 5️⃣ Train Logistic Regression model
model = LogisticRegression(max_iter=3000, n_jobs=-1)
model.fit(X_train, y_train)

# 6️⃣ Predict
y_pred = model.predict(X_test)

# 7️⃣ Accuracy
print("Accuracy:", accuracy_score(y_test, y_pred))

# 8️⃣ Confusion matrix
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(8,6))
sns.heatmap(cm, cmap="Blues")
plt.xlabel("Predicted")
plt.ylabel("True")
plt.title("Confusion Matrix")
plt.show()

# 9️⃣ Show random digit
idx = random.randint(0, len(X)-1)
plt.imshow(X.iloc[idx].values.reshape(28,28), cmap="gray")
plt.title(f"Label: {y.iloc[idx]}")
plt.axis("off")
plt.show()

