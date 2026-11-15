import re
import math
from urllib.parse import urlparse


def calculate_entropy(s):
    if not s:
        return 0
    prob = [s.count(c) / len(s) for c in set(s)]
    return -sum(p * math.log2(p) for p in prob)


def extract_features(url):
    url = url.strip()
    url = re.sub(r"^(\w+://)www\.", r"\1", url)  # ignore a leading www.

    parsed = urlparse(url)
    domain = parsed.netloc
    path = parsed.path

    features = {}
    features["url_length"] = len(url)
    features["num_dots"] = url.count(".")
    features["has_https"] = 1 if parsed.scheme == "https" else 0
    features["has_ip"] = 1 if re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", domain) else 0
    features["num_subdirs"] = path.count("/")
    features["num_params"] = url.count("=")

    suspicious = ["login", "verify", "secure", "account", "update", "bank", "confirm", "signin"]
    features["suspicious_words"] = sum(word in url.lower() for word in suspicious)

    features["special_char_count"] = len(re.findall(r"[^a-zA-Z0-9]", url))
    features["digits_count"] = sum(c.isdigit() for c in url)
    features["entropy"] = calculate_entropy(url)

    return features
