import pandas as pd

df = pd.read_csv("/var/log/dnsdist/queries.csv")
df["time"] = pd.to_datetime(df["timestamp"], unit="s")
df["qname"] = df["qname"].str.rstrip(".")
print(df.tail(10))
print("\nTotal queries:", len(df))
print(df["rcode"].value_counts())
