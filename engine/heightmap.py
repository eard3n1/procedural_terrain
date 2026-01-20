import numpy as np

def normalize(hm: np.ndarray, min_val: float = 0.0, max_val: float = 1.0) -> np.ndarray:
    hm_min, hm_max = hm.min(), hm.max()

    if hm_max - hm_min == 0:
        return np.full_like(hm, min_val)
    
    norm = (hm - hm_min) / (hm_max - hm_min)
    return norm * (max_val - min_val) + min_val