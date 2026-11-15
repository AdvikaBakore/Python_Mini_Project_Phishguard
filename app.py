import joblib
import pandas as pd
from urllib.parse import urlparse
from flask import Flask, render_template, request
from feature_extraction import extract_features

app = Flask(__name__)
model = joblib.load("phishing_model.pkl")

FEATURE_ORDER = ["url_length", "num_dots", "has_https", "has_ip", "num_subdirs",
                 "num_params", "suspicious_words", "special_char_count",
                 "digits_count", "entropy"]

THRESHOLD = 0.60  # risk at or above this is shown as phishing

# Well-known sites. If the domain is exactly one of these (or a subdomain of it),
# we trust it. "irctc.co.in.evil.com" does NOT match, because it ends with .com
TRUSTED_DOMAINS = [
    "google.com", "youtube.com", "gmail.com", "microsoft.com", "live.com",
    "apple.com", "amazon.com", "amazon.in", "flipkart.com", "wikipedia.org",
    "github.com", "stackoverflow.com", "linkedin.com", "facebook.com",
    "instagram.com", "whatsapp.com", "twitter.com", "x.com", "netflix.com",
    "hotstar.com", "irctc.co.in", "npci.org.in", "paypal.com", "python.org",
    "kaggle.com", "mitwpu.edu.in", "sbi.co.in", "hdfcbank.com", "icicibank.com",
]
# Only schools and government bodies can register these endings
TRUSTED_SUFFIXES = (".gov.in", ".edu.in", ".ac.in", ".gov", ".edu")


def is_trusted(url):
    host = urlparse(url).netloc.lower().split(":")[0]
    if host.startswith("www."):
        host = host[4:]
    if host.endswith(TRUSTED_SUFFIXES):
        return True
    return any(host == d or host.endswith("." + d) for d in TRUSTED_DOMAINS)


def model_score(url):
    """Return (phishing probability, features) for one URL."""
    features = extract_features(url)
    X = pd.DataFrame([features])[FEATURE_ORDER]
    return model.predict_proba(X)[0][1], features


def final_risk(url):
    """Score the domain on its own. Only let the path raise the score
    if the path itself contains suspicious words."""
    p = urlparse(url)
    domain_url = p.scheme + "://" + p.netloc
    full_prob, full_f = model_score(url)
    dom_prob, dom_f = model_score(domain_url)
    path_keywords = full_f["suspicious_words"] - dom_f["suspicious_words"]
    if path_keywords == 0:
        return dom_prob, full_f
    return max(full_prob, dom_prob), full_f


def build_signals(f):
    """Turn features into a list of (ok, text) lines for the result box."""
    signals = []
    if f["has_ip"]:
        signals.append((False, "Domain contains an IP address"))
    else:
        signals.append((True, "No IP address in the domain"))
    if f["suspicious_words"] > 0:
        signals.append((False, "Contains suspicious words (login, verify, secure, ...)"))
    else:
        signals.append((True, "No suspicious keywords"))
    if f["url_length"] > 75:
        signals.append((False, "Very long URL"))
    else:
        signals.append((True, "URL length is normal"))
    if f["num_dots"] >= 4:
        signals.append((False, "Many dots / subdomains"))
    if f["has_https"]:
        signals.append((True, "Uses HTTPS"))
    else:
        signals.append((False, "Does not use HTTPS"))
    return signals


@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        url = request.form.get("url", "").strip()
        if url:
            if "://" not in url:
                url = "https://" + url
            phishing_prob, features = final_risk(url)
            trusted = is_trusted(url)
            if trusted:
                phishing_prob = min(phishing_prob, 0.05)
            is_phishing = phishing_prob >= THRESHOLD
            signals = build_signals(features)
            if trusted:
                signals.insert(0, (True, "Domain is on our trusted list"))
            result = {
                "url": url,
                "is_phishing": is_phishing,
                "risk": round(phishing_prob * 100),
                "signals": signals,
            }
    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)