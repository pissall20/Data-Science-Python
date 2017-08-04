import numpy as np

# Returns if the value is outside the IQR range
def is_outlier(value, p25, p75):
    lower = p25 - 1.5 * (p75 - p25)
    upper = p75 + 1.5 * (p75 - p25)
    if value <= lower or value >= upper:
        return True
    elif value >= lower or value <= upper:
        return False

# Returns if there is an outlier in boolean, dependent on is_outlier
def check_outlier(values):
    p25 = np.percentile(values, 25)
    p75 = np.percentile(values, 75)
    for value in values:
        if is_outlier(value, p25, p75):
            return True
        else:
            return False

# Returns the indices of outliers present
def get_indices_of_outliers(values):
    """Get outlier indices (if any)
    """
    p25 = np.percentile(values, 25)
    p75 = np.percentile(values, 75)

    indices_of_outliers = []
    for i in range(len(values)):
        if is_outlier(values[i], p25, p75):
            indices_of_outliers.append(i)
        else:
            pass
    return indices_of_outliers