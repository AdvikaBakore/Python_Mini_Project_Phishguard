# PhishGuard - Intelligent Phishing URL Detection System

First Year Python Mini Project, MIT World Peace University, Pune (AY 2026-27).

PhishGuard is a small Flask web app. You paste a URL and it tells you whether the
link looks like **phishing** or **legitimate**, with a risk score and the reasons.

## How it works
1. `feature_extraction.py` turns a URL into 10 numbers (length, dots, HTTPS, IP address,
   path depth, parameters, suspicious words, special characters, digits, entropy).
2. A Random Forest model (scikit-learn), trained on a Kaggle dataset of 160,064 URLs,
   gives a phishing probability.
3. `app.py` combines that with domain-only scoring and a 0.60 threshold, and shows the
   result on a web page (`templates/index.html`).

## Files
| File | Purpose |
|---|---|
| `app.py` | Flask web app |
| `templates/index.html` | The web page |
| `feature_extraction.py` | Measures the 10 features of a URL |
| `retrain.py` | Trains and saves the model (adds realistic legitimate URLs with paths) |
| `check_urls.py` | Prints full / domain / final scores for sample URLs |
| `accuracy_test.py` | Tests 20 URLs and prints the accuracy |
| `phishing_model.pkl` | The trained model |
| `feature_importance.py` | Ranks the 10 URL features by importance |
| `feature_importance_results.csv` | Stores the feature importance scores |
| `feature_importance_graph.png` | Visual representation of feature importance |
| `threshold_analysis.py` | Compares model performance at different classification thresholds |
| `threshold_comparison.csv` | Stores the performance metrics for each threshold |
| `threshold_test_results.csv` | Stores test results for threshold analysis |
## How to run
```bash
python -m venv venv
venv\Scripts\activate          # Windows  (Mac/Linux: source venv/bin/activate)
pip install flask scikit-learn pandas joblib
python app.py
```
Open (http://127.0.0.1:5000/) in your browser.

To retrain the model, place `phishing_features.csv` (Kaggle: "Phishing URL Detection
Dataset (100K+ URLs)") in the folder and run `python retrain.py`. Restart the app afterwards.

## Results
- On 20 hand-chosen URLs (10 legitimate, 10 phishing-style): 20/20 correct.
- Real sites such as hotstar.com, wikipedia.org and amazon.in are no longer flagged.

## Model Analysis

### 1. Feature Importance Analysis

We used `feature_importance.py` to identify which URL features are most important for the Random Forest model.

The top three features were:

| Feature | Importance |
|---|---:|
| has_https | 19.32% |
| url_length | 14.30% |
| entropy | 12.42% |

The least important feature was `suspicious_words`, with a score of 0.53%.

The results are saved in `feature_importance_results.csv`, and the graph is saved as `feature_importance_graph.png`.

### 2. Threshold Analysis

We used `threshold_analysis.py` to compare six thresholds from 0.30 to 0.80.

The results at a threshold of 0.60 were:

- Accuracy: 97.13%
- Precision: 99.42%
- Recall: 97.39%
- F1-score: 98.39%

We selected 0.60 because it provides high precision while maintaining good recall. This helps reduce false alarms while still detecting most phishing URLs.
# PhishGuard - Intelligent Phishing URL Detection System

First Year Python Mini Project, MIT World Peace University, Pune (AY 2026-27).

PhishGuard is a small Flask web app. You paste a URL and it tells you whether the
link looks like **phishing** or **legitimate**, with a risk score and the reasons.

## How it works
1. `feature_extraction.py` turns a URL into 10 numbers (length, dots, HTTPS, IP address,
   path depth, parameters, suspicious words, special characters, digits, entropy).
2. A Random Forest model (scikit-learn), trained on a Kaggle dataset of 160,064 URLs,
   gives a phishing probability.
3. `app.py` combines that with domain-only scoring and a 0.60 threshold, and shows the
   result on a web page (`templates/index.html`).

## Files
| File | Purpose |
|---|---|
| `app.py` | Flask web app |
| `templates/index.html` | The web page |
| `feature_extraction.py` | Measures the 10 features of a URL |
| `retrain.py` | Trains and saves the model (adds realistic legitimate URLs with paths) |
| `check_urls.py` | Prints full / domain / final scores for sample URLs |
| `accuracy_test.py` | Tests 20 URLs and prints the accuracy |
| `phishing_model.pkl` | The trained model |
| `feature_importance.py` | Ranks the 10 URL features by importance |
| `feature_importance_results.csv` | Stores the feature importance scores |
| `feature_importance_graph.png` | Visual representation of feature importance |
| `threshold_analysis.py` | Compares model performance at different classification thresholds |
| `threshold_comparison.csv` | Stores the performance metrics for each threshold|
| `threshold_test_results.csv` | Stores test results for threshold analysis |
## How to run
```bash
python -m venv venv
venv\Scripts\activate          # Windows  (Mac/Linux: source venv/bin/activate)
pip install flask scikit-learn pandas joblib
python app.py
```
Open (http://127.0.0.1:5000/) in your browser.

To retrain the model, place `phishing_features.csv` (Kaggle: "Phishing URL Detection
Dataset (100K+ URLs)") in the folder and run `python retrain.py`. Restart the app afterwards.

## Results
- On 20 hand-chosen URLs (10 legitimate, 10 phishing-style): 20/20 correct.
- Real sites such as hotstar.com, wikipedia.org and amazon.in are no longer flagged.

## Model Analysis

### 1. Feature Importance Analysis

We used `feature_importance.py` to identify which URL features are most important for the Random Forest model.

The top three features were:

| Feature | Importance |
|---|---:|
| has_https | 19.32% |
| url_length | 14.30% |
| entropy | 12.42% |

The least important feature was `suspicious_words`, with an score of 0.53%.

The results are saved in `feature_importance_results.csv`, and the graph is saved as `feature_importance_graph.png`.

### 2. Threshold Analysis

We used `threshold_analysis.py` to compare six thresholds from 0.30 to 0.80.

The results at a threshold of 0.60 were:

- Accuracy: 97.13%
- Precision: 99.42%
- Recall: 97.39%
- F1-score: 98.39%

We selected 0.60 because it provides high precision (99.42%) while maintaining good recall (97.39%), helping reduce false alarms while still detecting most phishing URLs.

The comparison results are saved in `threshold_comparison.csv`.

### 3. Conclusion

Feature importance analysis helped us understand which URL features influence the model's predictions. Threshold analysis helped us understand how changing the threshold affects the model's performance.

## Future Scope
- Add a WHOIS domain-age feature, since brand-new domains are a classic phishing sign.
- Train on a much larger list of real, popular websites to reduce false alarms.
- Analyse the page content too (login forms, logos, hidden links).
- Build a browser extension that warns users before they click a link.
- Deploy the Flask app online so anyone can use it.
- Add a feedback button and retrain regularly with new phishing URLs.
The comparison results are saved in `threshold_comparison.csv`.

## Team
**MIT-WPU Pune - Team of 4**
1. Advika Bakore
2. Asmita Dalvi
3. Sradha Saiju
4. Tanvi Rathod
