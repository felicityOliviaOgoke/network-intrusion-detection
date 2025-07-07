import numpy as np
import numpy as np
from sklearn.metrics import classification_report, confusion_matrix
class ModelEvaluator:
    def __init__(self, threshold=None):
        self.threshold = threshold

    def find_threshold(self, mse_normal, percentile=95):
        self.threshold = np.percentile(mse_normal, percentile)
        return self.threshold

    def evaluate(self, mse_normal, mse_attack):
        y_pred = np.concatenate([(mse_normal > self.threshold).astype(int),
                                 (mse_attack > self.threshold).astype(int)])
        y_true = np.concatenate([np.zeros_like(mse_normal), np.ones_like(mse_attack)])
        return confusion_matrix(y_true, y_pred), classification_report(y_true, y_pred, target_names=["Normal", "Attack"])
