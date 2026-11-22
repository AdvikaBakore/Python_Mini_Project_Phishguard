# Tests PhishGuard on 30 URLs we chose ourselves (15 legitimate, 15 phishing-style).
# Run:  python accuracy_test.py
from app import final_risk, is_trusted, THRESHOLD

TESTS = [  # (url, correct answer: 0 = legitimate, 1 = phishing)
    ("https://www.google.com/search?q=python", 0),
    ("https://github.com/pallets/flask", 0),
    ("https://www.wikipedia.org", 0),
    ("https://www.amazon.in/gp/cart/view.html", 0),
    ("https://www.flipkart.com/mobiles/pr?sid=tyy", 0),
    ("https://www.youtube.com/watch?v=abc123", 0),
    ("https://www.mitwpu.edu.in/admissions", 0),
    ("https://www.irctc.co.in/nget/train-search", 0),
    ("https://stackoverflow.com/questions/tagged/python", 0),
    ("https://www.linkedin.com/in/someone", 0),
    ("http://paypa1-secure-login.com/account/confirm", 1),
    ("http://192.168.1.1-secure-login.verify-account.com/update", 1),
    ("http://sbi-netbanking-verify.com/login/update-account", 1),
    ("http://amaz0n-account-verify.net/signin?id=84721", 1),
    ("http://secure-login.google-account-confirm.xyz/verify", 1),
    ("http://hdfc-bank-update-kyc.info/login.php?user=1234", 1),
    ("http://netflix-billing-update.com/account/confirm-payment", 1),
    ("http://45.77.12.9/login/verify/account.php", 1),
    ("http://icici-secure-signin.top/bank/confirm", 1),
    ("http://apple-id-locked-verify.com/signin/update", 1),
    # ---- 10 new URLs ----
    ("https://www.microsoft.com/en-in", 0),
    ("https://www.nytimes.com/section/world", 0),
    ("https://www.bbc.com/news", 0),
    ("https://www.swiggy.com/restaurants", 0),
    ("https://docs.python.org/3/tutorial", 0),
    ("http://netflix-account-suspended.com/login/verify", 1),
    ("http://secure-sbi-kyc-update.xyz/login?id=9921", 1),
    ("http://paytm-wallet-verify.top/confirm/account", 1),
    ("http://123.45.67.89/bank/signin.php", 1),
    ("http://amazon-prize-winner-claim.info/verify/account", 1),
]

correct = 0
print(f"{'RESULT':<8}{'RISK':>6}  URL")
for url, truth in TESTS:
    risk = final_risk(url)[0]
    if is_trusted(url):
        risk = min(risk, 0.05)
    pred = 1 if risk >= THRESHOLD else 0
    ok = pred == truth
    correct += ok
    print(f"{'OK' if ok else 'WRONG':<8}{round(risk*100):>5}%  {url}")
print(f"\nAccuracy: {correct}/{len(TESTS)} = {correct/len(TESTS)*100:.0f}%")