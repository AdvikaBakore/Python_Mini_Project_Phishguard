import joblib
import pandas as pd
from feature_extraction import extract_features

model = joblib.load("phishing_model.pkl")

urls_to_test = [
    "https://www.google.com",
    "https://www.mitwpu.edu.in",
    "http://192.168.1.1-secure-login.verify-account.com/update",
    "https://paypa1-secure-login.com/account/confirm",
    "https://github.com",
]

for url in urls_to_test:
    feats = extract_features(url)
    # Match the exact column order used in training
    X = pd.DataFrame([feats])[
        ["url_length", "num_dots", "has_https", "has_ip", "num_subdirs",
         "num_params", "suspicious_words", "special_char_count",
         "digits_count", "entropy"]
    ]
    prediction = model.predict(X)[0]
    result = "PHISHING" if prediction == 1 else "LEGITIMATE"
    print(f"{url}  -->  {result}")