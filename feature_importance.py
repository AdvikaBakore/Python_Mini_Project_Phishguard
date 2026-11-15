import joblib
import pandas as pd
import matplotlib.pyplot as plt

model=joblib.load("phishing_model.pkl")
features= ['url_length','num_dots','has_https','has_ip','num_subdirs',
           'num_params','suspicious_words','special_char_count','digits_count','entropy']
importance=model.feature_importances_
if len(features) != len(importance):
    raise ValueError("Feature names do not match model features")

importance_df=pd.DataFrame({"Feature": features, 'Importance': importance})
importance_df=importance_df.sort_values(by="Importance",ascending=False)

print("\n===== FEATURE IMPORTANCE =====")
print(importance_df.to_string(index=False))

importance_df.to_csv("feature_importance_results.csv", index=False)

plt.figure(figsize=(10, 6))
plt.barh(importance_df["Feature"],importance_df["Importance"])

plt.xlabel("Importance Score")
plt.ylabel("Features")
plt.title("Random Forest Feature Importance")
plt.gca().invert_yaxis()
plt.tight_layout()

plt.savefig("feature_importance_graph.png")
plt.show()