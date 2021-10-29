# DDM

import numpy as np
from river.drift import DDM
np.random.seed(12345)

ddm = DDM()

# Simulate a data stream as a normal distribution of 1's and 0's
data_stream = np.random.randint(2, size=2000)
# Change the data distribution from index 999 to 1500, simulating an
# increase in error rate (1 indicates error)
data_stream[1000:1200] = [np.random.binomial(1, .8) for _ in range(200)]

# Update drift detector and verify if change is detected
for i, val in enumerate(data_stream):
    in_drift, in_warning = ddm.update(val)
    if in_drift:
        print(f"Change detected at index {i}, input value: {val}")
# Change detected at index 1157, input value: 1
