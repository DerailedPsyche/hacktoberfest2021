# pageHinkley

import numpy as np
from river.drift import PageHinkley
np.random.seed(12345)

ph = PageHinkley()

# Simulate a data stream composed by two data distributions
data_stream = np.concatenate((np.random.randint(3, size=1000),
                               np.random.randint(4, high=16, size=1000)))

# Update drift detector and verify if change is detected
for i, val in enumerate(data_stream):
    in_drift, in_warning = ph.update(val)
    if in_drift:
        print(f"Change detected at index {i}, input value: {val}")
# Change detected at index 1009, input value: 5
