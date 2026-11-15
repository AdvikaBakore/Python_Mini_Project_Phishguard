import joblib
import pandas as pd
from urllib.parse import urlparse
from feature_extraction import extract_features

ORDER = ["url_length", "num_dots", "has_https", "has_ip", "num_subdirs",
         "num_params", "suspicious_words", "special_char_count",
         "digits_count", "entropy"]

model = joblib.load("phishing_model.pkl")


def score(u):
    f = extract_features(u)
    return model.predict_proba(pd.DataFrame([f])[ORDER])[0][1], f


urls = [
    "https://hotstar.com",
    "https://www.hotstar.com/in",
    "https://www.hotstar.com/in/onboarding/profile",
    "https://en.wikipedia.org/wiki/Python_(programming_language)",
    "https://www.amazon.in/gp/cart/view.html",
    "https://paypa1-secure-login.com/account/confirm",
    "http://192.168.1.1-secure-login.verify-account.com/update",
]

print("FULL = whole URL | DOMAIN = domain only | FINAL = our combined score")
for u in urls:
    p = urlparse(u)
    full, f_full = score(u)
    dom, f_dom = score(p.scheme + "://" + p.netloc)
    kw = f_full["suspicious_words"] - f_dom["suspicious_words"]
    final = dom if kw == 0 else max(full, dom)
    print(f"FULL {round(full*100):>3}%  DOMAIN {round(dom*100):>3}%  FINAL {round(final*100):>3}%  {u}")