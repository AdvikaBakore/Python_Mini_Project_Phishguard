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

## Limitations
- Only 820 legitimate domains in the dataset, so unknown real sites can be misjudged.
- Augmented URL paths are synthetic; the test set is small.
- Looks at URL text only (no page content, domain age or blacklists).
- The threshold trades false alarms against missed phishing.

## Team
Team of 4 - MIT-WPU Pune. (Asmita Dalvi,Sradha Saiju,Tanvi Rathod,Advika Bakore)