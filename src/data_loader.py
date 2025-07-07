import pandas as pd
import numpy as np
class DataLoader:
    def __init__(self, filepath):
        self.filepath = filepath

    def load(self):

        df = pd.read_csv(self.filepath, low_memory=False)
        df.columns = df.columns.str.strip()
        df.replace(['Infinity', 'NaN', np.inf, -np.inf], np.nan, inplace=True)
        df.dropna(inplace=True)
        df['Label'] = df['Label'].apply(lambda x: 0 if x == 'BENIGN' else 1)
        df.drop(columns=['Flow ID', 'Source IP', 'Destination IP', 'Timestamp'], errors='ignore', inplace=True)
        return df
