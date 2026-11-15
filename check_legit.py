import pandas as pd

df = pd.read_csv("phishing_features.csv")
legit = df[df["label"] == 0]
phish = df[df["label"] == 1]

print(legit["url"].head(20))
print("Average num_subdirs - legitimate:", legit["num_subdirs"].mean())
print("Average num_subdirs - phishing:", phish["num_subdirs"].mean())