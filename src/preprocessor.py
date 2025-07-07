from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import VarianceThreshold
import numpy as np
class Preprocessor:
    def __init__(self):
        self.scaler = StandardScaler()
        self.selector = VarianceThreshold()

    def fit_transform(self, X):
        corr = X.corr().abs()
        upper = corr.where(np.triu(np.ones(corr.shape), k=1).astype(bool))
        self.to_drop = [col for col in upper.columns if any(upper[col] > 0.95)]
        X = X.drop(columns=self.to_drop)

        X_scaled = self.scaler.fit_transform(X)
        X_final = self.selector.fit_transform(X_scaled)
        return X_final

    def transform(self, X):
        X = X.drop(columns=self.to_drop)
        X_scaled = self.scaler.transform(X)
        return self.selector.transform(X_scaled)
