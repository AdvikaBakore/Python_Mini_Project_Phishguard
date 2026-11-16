
import pandas as pd
from sklearn.metrics import (accuracy_score,precision_score,recall_score,f1_score,confusion_matrix)

df = pd.read_csv("threshold_test_results.csv")
y_test = df["actual_label"]
probabilities = df["phishing_probability"]

thresholds = [0.30,0.40,0.50,0.60,0.70,0.80,0.90]

print("\n===== THRESHOLD ANALYSIS =====")
results = []

for threshold in thresholds:
    predictions = (probabilities >= threshold).astype(int)
    accuracy = accuracy_score(y_test, predictions)
    precision = precision_score(y_test, predictions, zero_division=0)
    recall = recall_score(y_test, predictions, zero_division=0)
    f1 = f1_score(y_test, predictions, zero_division=0)

    print(f"\nThreshold: {threshold}")
    print(f"Accuracy: {accuracy:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall: {recall:.4f}")
    print(f"F1 Score: {f1:.4f}")

    results.append({"Threshold": threshold,"Accuracy": accuracy,"Precision": precision,"Recall": recall,"F1 Score": f1})

results_df = pd.DataFrame(results)
results_df.to_csv("threshold_comparison.csv", index=False)
print("\nResults saved to threshold_comparison.csv")
