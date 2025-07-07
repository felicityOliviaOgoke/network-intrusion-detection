# Autoencoder IDS

A lightweight Intrusion Detection System (IDS) built using an unsupervised deep learning approach. This system is designed to detect malicious network activity by modeling normal (benign) traffic patterns using an autoencoder, and flagging deviations as potential intrusions.

---

## Why Autoencoders?

Autoencoders are neural networks trained to reconstruct their input data. When trained exclusively on **benign traffic**, the model becomes highly specialized in recreating normal behavior. When **malicious traffic** is introduced, the reconstruction error increases significantly, allowing for **anomaly detection without labeled attack data**. This makes autoencoders particularly valuable for:
- Zero-day attacks
- Unsupervised learning scenarios
- Reducing labeling cost and bias

---

## Dataset: CIC-IDS2017

The [CIC-IDS2017 dataset](https://www.unb.ca/cic/datasets/ids-2017.html) is a benchmark dataset for evaluating intrusion detection systems. It includes realistic traffic data covering various attack types and benign behavior.

This project uses the following subset: Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX

To use it:
1. Download the `.csv` or converted `.pcap_ISCX` file from CIC's site.
2. Place it in the `data/` directory (you can change the path in `main.py` as needed).

---

## Features

- Trains autoencoder using only benign samples
- Cleans and preprocesses features (drops non-informative, scales, filters)
- Uses reconstruction error as anomaly score
- Detects attacks with a learned threshold
- Outputs a full classification report and confusion matrix

---

## Results
**Performance Analysis**
The model demonstrates high effectiveness in detecting both normal and attack traffic:

Normal Traffic
Precision: 0.99 — the model almost never falsely labels attacks as normal
Recall: 0.95 — slightly underdetects some normal traffic as attacks

Attack Traffic
Precision: 0.96 — very few false positives
Recall: 0.99 — almost all attacks were correctly detected

Overall Accuracy: 97%
Balanced performance across classes with strong macro and weighted averages, indicating that neither class dominates the learning process or skews the evaluation.

This balance makes the system practical for real-world intrusion detection, where minimizing false negatives (missed attacks) and false positives (over-alerting) are both critical.


![download](https://github.com/user-attachments/assets/954e46a8-3ca9-4d24-ab97-00052a16418d)







