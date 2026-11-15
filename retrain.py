import os
import random
import shutil
from urllib.parse import urlparse
import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from feature_extraction import extract_features

ORDER = ["url_length", "num_dots", "has_https", "has_ip", "num_subdirs",
         "num_params", "suspicious_words", "special_char_count",
         "digits_count", "entropy"]

random.seed(42)


def add_scheme(u):
    u = str(u).strip()
    return u if "://" in u else "https://" + u


# 1. Load original dataset: keep only url + label (we recalculate features ourselves)
df = pd.read_csv("phishing_features.csv")[["url", "label"]]
df["url"] = df["url"].apply(add_scheme)
df["source"] = "original"
print("Original dataset rows:", len(df))

# 2. Build realistic legitimate URLs WITH paths on the dataset's own legitimate domains
SEGMENTS = ["en", "us", "uk", "hi", "about", "products", "product", "help", "support",
            "docs", "blog", "news", "category", "categories", "item", "store", "shop",
            "watch", "video", "videos", "play", "settings", "pricing", "contact",
            "careers", "faq", "features", "tv", "movies", "shows", "series", "sports",
            "articles", "article", "wiki", "page", "view", "details", "home", "explore",
            "search", "download", "apps", "services", "learn", "courses", "community",
            "events", "topics", "collections", "overview", "welcome", "getting-started",
            "tutorials", "documentation", "international", "entertainment", "membership",
            "subscription", "notifications", "preferences", "downloads", "publications"]
WORDS = ["best", "new", "how", "guide", "latest", "review", "tips", "learn", "python",
         "music", "travel", "health", "sports", "movies", "recipes", "phones", "laptops",
         "budget", "season", "episode", "trailer", "college", "science", "design"]
ENDINGS = ["", "", "", ".html", ".php", ".aspx"]
QUERIES = ["", "", "", "?id={n}", "?q=python+tutorial&page=2", "?ref=home",
           "?lang=en", "?v=abc{n}XYZ", "?page={n}"]

CONSONANTS = "bcdfghjklmnprstvwz"
VOWELS = "aeiou"


def random_word():
    """Pronounceable made-up word, 3 to 14 letters, so path words have many different lengths."""
    length = random.randint(3, 14)
    return "".join(
        random.choice(CONSONANTS if i % 2 == 0 else VOWELS) for i in range(length)
    )


def make_path():
    parts = []
    for _ in range(random.randint(1, 4)):
        kind = random.random()
        if kind < 0.40:
            parts.append(random.choice(SEGMENTS))
        elif kind < 0.55:
            parts.append(str(random.randint(1, 99999)))
        elif kind < 0.75:
            parts.append("-".join(random.sample(WORDS, random.randint(2, 3))))
        else:
            parts.append(random_word())
    return "/" + "/".join(parts) + random.choice(ENDINGS)


legit_urls = df[df["label"] == 0]["url"]
domains = set()
for u in legit_urls:
    netloc = urlparse(u).netloc
    if netloc and "hotstar" not in netloc.lower():
        domains.add(netloc)
print("Legitimate domains found:", len(domains))

PER_DOMAIN = 20
synthetic = []
for d in sorted(domains):
    for _ in range(PER_DOMAIN):
        host = d
        # half of the time use the www. version (many real sites do)
        if not host.startswith("www.") and random.random() < 0.5:
            host = "www." + host
        q = random.choice(QUERIES).format(n=random.randint(1, 9999))
        synthetic.append("https://" + host + make_path() + q)
syn_df = pd.DataFrame({"url": synthetic, "label": 0, "source": "synthetic"})
print("Synthetic legitimate URLs with paths:", len(syn_df))
print("Examples:", synthetic[:3])
df = pd.concat([df, syn_df], ignore_index=True)

# 3. Optional: our own hand-collected legitimate URLs
if os.path.exists("my_legit_urls.txt"):
    with open("my_legit_urls.txt", encoding="utf-8") as f:
        own = [line.strip() for line in f if line.strip()]
    own_df = pd.DataFrame({"url": own, "label": 0, "source": "own"})
    df = pd.concat([df, own_df], ignore_index=True)
    print("Own legitimate URLs added:", len(own))

# 4. Keep hotstar out of training so it stays a fair test
df = df[~df["url"].astype(str).str.contains("hotstar.com", case=False)].reset_index(drop=True)

# 5. Recalculate features with OUR function (same code the web page uses)
feats = pd.DataFrame([extract_features(u) for u in df["url"]])
X = feats[ORDER]
y = df["label"]

# Evidence for the report: how many '/' does each group have on average?
check = feats.assign(label=df["label"], source=df["source"])
print("\nAverage num_subdirs (number of / in the path):")
print(check.groupby(["source", "label"])["num_subdirs"].mean().round(2))
print("\nTraining rows per class:")
print(y.value_counts())

# 6. Train / test split and train
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
model = RandomForestClassifier(class_weight="balanced", random_state=42)
model.fit(X_train, y_train)

# 7. Evaluate
preds = model.predict(X_test)
print(classification_report(y_test, preds, target_names=["legitimate", "phishing"]))
print("Confusion matrix:\n", confusion_matrix(y_test, preds))

# 8. Back up the old model, then save the new one
if os.path.exists("phishing_model.pkl") and not os.path.exists("phishing_model_v1.pkl"):
    shutil.copy("phishing_model.pkl", "phishing_model_v1.pkl")
joblib.dump(model, "phishing_model.pkl")
print("Saved new phishing_model.pkl")