# PhishGuard - Intelligent Phishing URL Detection System

**First Year Python Programming Mini Project, MIT World Peace University, Pune (AY 2026-27).**

PhishGuard is a small web app built with Flask. You paste a link, and it shows a risk score, a risk level (Safe, Suspicious or Dangerous) and the reasons behind the result, so you can check a link before you click it.

**Team:** Advika Bakore, Asmita Dalvi, Sradha Saiju, Tanvi Rathod

## Why this project

Phishing links pretend to be banks, shops or delivery services to steal passwords and money. Many checkers only know links that were already reported. PhishGuard measures the link itself, so it can give a risk score even for a link it has never seen before.

## Features

**Application, model and new features by: Advika Bakore**

- Risk score and three levels: Safe (green), Suspicious (orange) and Dangerous (red), with a risk bar.
- "Why" list: the result is explained in plain words (for example: suspicious words, no HTTPS, IP address, very long link).
- Look-alike detection: warns about fake names such as `paypa1.com` or `g00gle.com` that copy a trusted site.
- Short-link warning: warns about links like `bit.ly` that hide the real destination.
- Safety tip: one line of advice that matches the risk level.
- Recent checks: the last 5 links are shown while the app is running. They are kept only in memory and are never saved to a file.

## How it works

- `feature_extraction.py` turns a URL into 10 numbers: length, dots, HTTPS, IP address, path depth, parameters, suspicious words, special characters, digits and entropy (randomness).
- A Random Forest model (scikit-learn), trained on a Kaggle dataset of 160,064 URLs, gives a phishing probability.
- `app.py` scores the domain on its own (the path only counts if it adds suspicious words), applies a trusted-sites list, the look-alike and short-link checks, and a threshold of 0.60.
- The result is shown on the web page `templates/index.html`.

## Technology stack

- Python
- Flask
- scikit-learn (Random Forest)
- pandas
- joblib
- HTML and CSS

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
|---|---:|---:|
| Real websites | 15 | 15 |
| Phishing-style URLs | 15 | 15 |
| **Total** | **30** | **30 (100%)** |

To run it: `python accuracy_test.py`. The full output is saved in `test_results.txt`.

### 2. Manual
