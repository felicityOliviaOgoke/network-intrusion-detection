from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.models import load_model
import numpy as np
class AutoencoderIDS:
    def __init__(self, input_dim):

        self.model = Sequential([
            Input(shape=(input_dim,)),
            Dense(64, activation='relu'),
            Dense(32, activation='relu'),
            Dense(64, activation='relu'),
            Dense(input_dim, activation='linear')
        ])
        self.model.compile(optimizer='adam', loss='mse')

    def train(self, X_train):
        early_stop = EarlyStopping(monitor='val_loss', patience=3, restore_best_weights=True)
        self.model.fit(X_train, X_train,
                       epochs=20, batch_size=256, validation_split=0.1,
                       callbacks=[early_stop], verbose=1)

    def save(self, path):
        self.model.save(path)

    def load(self, path):
        self.model = load_model(path)

    def reconstruct(self, X):
        return self.model.predict(X)

    def reconstruction_error(self, X, X_recon):
        return np.mean(np.square(X - X_recon), axis=1)
