from src.data_loader import DataLoader
from src.preprocessor import Preprocessor
from src.autoencoder_model import AutoencoderIDS
from src.evaluator import ModelEvaluator

# Load data
df = DataLoader("data/Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX").load()

# Preprocess
X = df.drop("Label", axis=1)
y = df["Label"]
preproc = Preprocessor()
X_proc = preproc.fit_transform(X)

# Train only on normal traffic
X_train = X_proc[y == 0]
X_test = X_proc[y == 1]

model = AutoencoderIDS(input_dim=X_train.shape[1])
model.train(X_train)

# Predict & evaluate
mse_normal = model.reconstruction_error(X_train, model.reconstruct(X_train))
mse_attack = model.reconstruction_error(X_test, model.reconstruct(X_test))

evaluator = ModelEvaluator()
threshold = evaluator.find_threshold(mse_normal)
conf_matrix, report = evaluator.evaluate(mse_normal, mse_attack)

print("Threshold:", threshold)
print(conf_matrix)
print(report)

# Save the model
model.save("models/autoencoder_model.keras", include_optimizer=False)
