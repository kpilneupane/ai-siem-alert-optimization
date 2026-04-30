import pandas as pd

def load_data(path):
    df = pd.read_csv(path)

    # basic cleaning
    df = df.dropna(subset=["text", "label"])
    df["text"] = df["text"].str.strip()

    return df["text"].tolist(), df["label"].tolist()
