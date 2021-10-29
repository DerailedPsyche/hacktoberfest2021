# ADWIN

import numpy as np
from river.drift import ADWIN
np.random.seed(12345)

adwin = ADWIN()

# Simulate a data stream composed by two data distributions
data_stream = np.concatenate((np.random.randint(2, size=1000),
                              np.random.randint(4, high=8, size=1000)))

# Update drift detector and verify if change is detected
for i, val in enumerate(data_stream):
    in_drift, in_warning = adwin.update(val)
    if in_drift:
        print(f"Change detected at index {i}, input value: {val}")
