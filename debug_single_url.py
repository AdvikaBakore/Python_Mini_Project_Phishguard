import joblib
import pandas as pd
from feature_extraction import extract_features

model = joblib.load("phishing_model.pkl")

url = "http://192.168.1.1-secure-login.verify-account.com/update"
feats = extract_features(url)

print("Extracted features:")
for k, v in feats.items():
    print(f"  {k}: {v}")

X = pd.DataFrame([feats])[
    ["url_length", "num_dots", "has_https", "has_ip", "num_subdirs",
     "num_params", "suspicious_words", "special_char_count",
     "digits_count", "entropy"]
]

prediction = model.predict(X)[0]
probability = model.predict_proba(X)[0]

print("\nPrediction:", "PHISHING" if prediction == 1 else "LEGITIMATE")
print("Probability [legitimate, phishing]:", probability)