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
Open http://127.0.0.1:5000/ in your browser.

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

We used `threshold_analysis.py` to compare six thresholds from 0.30 to 0.90.

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
 PhishGuard - Intelligent Phishing URL Detection System

First Year Python Programming Mini Project, MIT World Peace University, Pune (AY 2026-27).

PhishGuard is a small web app built with Flask. You paste a link, and it shows a **risk score**, a risk level (**Safe**, **Suspicious** or **Dangerous**) and the **reasons** behind the result, so you can check a link before you click it.

**Team:** Advika Bakore, Asmita Dalvi, Sradha Saiju, Tanvi Rathod

## Why this project
Phishing links pretend to be banks, shops or delivery services to steal passwords and money. Many checkers only know links that were already reported. PhishGuard measures the link itself, so it can give a risk score even for a link it has never seen before.

## Features
**Application, model and new features by: Advika Bakore**

- **Risk score and three levels:** Safe (green), Suspicious (orange) and Dangerous (red), with a risk bar.
- **"Why" list:** the result is explained in plain words (for example: suspicious words, no HTTPS, IP address, very long link).
- **Look-alike detection:** warns about fake names such as `paypa1.com` or `g00gle.com` that copy a trusted site.
- **Short-link warning:** warns about links like `bit.ly` that hide the real destination.
- **Safety tip:** one line of advice that matches the risk level.
- **Recent checks:** the last 5 links are shown while the app is running. They are kept only in memory and are never saved to a file.

## How it works
1. `feature_extraction.py` turns a URL into 10 numbers: length, dots, HTTPS, IP address, path depth, parameters, suspicious words, special characters, digits and entropy (randomness).
2. A Random Forest model (scikit-learn), trained on a Kaggle dataset of 160,064 URLs, gives a phishing probability.
3. `app.py` scores the domain on its own (the path only counts if it adds suspicious words), applies a trusted-sites list, the look-alike and short-link checks, and a threshold of 0.60.
4. The result is shown on the web page `templates/index.html`.

## Technology stack
Python, Flask, scikit-learn (Random Forest), pandas, joblib, HTML and CSS.

## Files
| File | Purpose |
|---|---|
| `app.py` | Flask web app, scoring rules and the new checks |
| `templates/index.html` | The web page |
| `feature_extraction.py` | Measures the 10 features of a URL |
| `retrain.py` | Trains and saves the model (adds realistic legitimate URLs with paths) |
| `check_urls.py` | Prints full, domain and final scores for sample URLs |
| `accuracy_test.py` | Tests 30 URLs and prints the accuracy |
| `test_results.txt` | Saved output of the accuracy test |
| `feature_importance.py` | Shows which features the model relies on |
| `threshold_analysis.py` | Shows how the threshold changes the results |
| `phishing_model.pkl` | The trained model |

## How to run
```bash
python -m venv venv
venv\Scripts\activate          # Windows  (Mac/Linux: source venv/bin/activate)
pip install flask scikit-learn pandas joblib
python app.py
```
Open http://127.0.0.1:5000/ in your browser.

To retrain the model, place `phishing_features.csv` (Kaggle: "Phishing URL Detection Dataset (100K+ URLs)") in the folder and run `python retrain.py`. Restart the app afterwards.

## Testing
**Tested by: Asmita Dalvi**

PhishGuard was tested in two ways.

### 1. Automatic accuracy test
`accuracy_test.py` checks 30 URLs that we chose ourselves: 15 real websites and 15 phishing-style links.

| Group | Number of URLs | Correct |
|---|---|---|
| Real websites | 15 | 15 |
| Phishing-style URLs | 15 | 15 |
| **Total** | **30** | **30 (100%)** |

To run it: `python accuracy_test.py`. The full output is saved in `test_results.txt`.

### 2. Manual test of the new features
We typed links into the web page and checked what it showed.

| URL typed | Expected | Result |
|---|---|---|
| www.hotstar.com/in | Safe (trusted list) | Safe, 5% |
| github.com/pallets/flask | Safe | Safe |
| paypa1.com | Dangerous, look-alike warning | Dangerous, 85% |
| g00gle.com | Dangerous, look-alike warning | Dangerous, 85% |
| amazom.in | Dangerous, look-alike warning | Dangerous, 85% |
| bit.ly/abc123 | Suspicious, short-link warning | Suspicious, 40% |
| http://paypa1-secure-login.com/account/confirm | Dangerous | Dangerous |

### What the testing shows, and what it does not
- The app behaves correctly on these examples.
- The test set is small. The real websites are mostly well known, and the phishing links are obvious look-alikes, so results on other links may be different.
- The look-alike check only compares with the sites on our trusted list, so it cannot catch a fake of a site that is not on the list.
- A short link is marked Suspicious, not Dangerous, because short links are not always bad.

## Model Analysis
**Analysis by: Sradha Saiju**

This section explains how the model makes its decisions and how the threshold affects the results.

### 1. Which features does the model rely on most?
`feature_importance.py` ranks the 10 features by how much the Random Forest uses them.

| Feature | Importance |
|---|---|
| suspicious_words | 38.5% |
| has_https | 32.8% |
| entropy | 11.5% |
| special_char_count | 7.0% |
| url_length | 5.9% |
| num_dots | 2.2% |
| num_subdirs | 2.1% |
| num_params | 0.0% |
| has_ip | 0.0% |
| digits_count | 0.0% |

- The model relies mostly on suspicious words and on whether the link uses HTTPS.
- The three features at 0% are not used by the model. The app still shows an IP warning on the page.
- The training data has very few real websites, so the model may have learned that "no HTTPS" means phishing. We treat this as a limit.

### 2. How does the threshold change the results?
A risk at or above the threshold is shown as phishing. `threshold_analysis.py` tries thresholds from 0.30 to 0.90 on our 30 test URLs.

| Threshold | Real sites wrongly flagged | Phishing missed | Accuracy |
|---|---|---|---|
| 0.30 | 0 | 0 | 100% |
| 0.40 | 0 | 0 | 100% |
| 0.50 | 0 | 0 | 100% |
| **0.60 (we use this)** | 0 | 0 | 100% |
| 0.70 | 0 | 0 | 100% |
| 0.80 | 0 | 4 | 87% |
| 0.90 | 0 | 13 | 57% |

- From 0.30 to 0.70 the results are the same on our test, so 0.60 is a safe middle value.
- Above 0.80 the model starts to miss phishing links.
- A lower threshold catches more phishing but could wrongly flag real sites on a bigger test.

## Responsible use
- PhishGuard gives a **risk score to help a person decide**. It is not a final judgement, and it can be wrong in both directions.
- It only reads the link text that the user pastes. The recent checks list stays in memory and is not saved.
- We report our results honestly, including the limits below.

## SDG mapping
- **SDG 16 (Peace, Justice and Strong Institutions):** helps people avoid online fraud.
- **SDG 9 (Industry, Innovation and Infrastructure):** a digital safety tool.
- **SDG 8 (Decent Work and Economic Growth):** fraud causes real money loss for people and small businesses.

## Future scope
- Check how old a website is (new sites are riskier).
- Train on many more real websites to make it more reliable.
- Read the page content as well as the link.
- Make it a browser add-on that warns you automatically.
- Put it online so anyone can use it.

## Documentation
**Documentation (this README, the project report and the presentations) by: Tanvi Rathod**

## Team
Team of 4, MIT-WPU Pune.

| Member | Role |
|---|---|
| Advika Bakore | Application code, model training and new features |
| Asmita Dalvi | Testing |
| Sradha Saiju | Model analysis |
| Tanvi Rathod | Documentation and presentations |

**MIT-WPU Pune - Team of 4**
1. Advika Bakore
2. Asmita Dalvi
3. Sradha Saiju
4. Tanvi Rathod
