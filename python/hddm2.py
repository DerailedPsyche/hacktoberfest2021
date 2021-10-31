# HHDM_A
import numpy as np
from river.drift import HDDM_A
np.random.seed(12345)

hddm_a = HDDM_A()

# Simulate a data stream as a normal distribution of 1's and 0's
data_stream = np.random.randint(2, size=2000)
# Change the data distribution from index 999 to 1500, simulating an
# increase in error rate (1 indicates error)
data_stream[999:1500] = 1

# Update drift detector and verify if change is detected
for i, val in enumerate(data_stream):
    in_drift, in_warning = hddm_a.update(val)
    if in_drift:
        print(f"Change detected at index {i}, input value: {val}")
# Change detected at index 1013, input value: 1
