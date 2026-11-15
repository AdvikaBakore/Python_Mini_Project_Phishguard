import pandas as pd

df = pd.read_csv("phishing_features.csv")

# Check correlation of each numeric feature with the label
df_numeric = df.drop(columns=["url", "tld"])
correlations = df_numeric.corr()["label"].sort_values(ascending=False)
print(correlations)