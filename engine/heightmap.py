import numpy as np

def normalize(hm: np.ndarray, min_val: float = 0.0, max_val: float = 1.0) -> np.ndarray:
    hm_min, hm_max = hm.min(), hm.max()

    if hm_max - hm_min == 0:
        return np.full_like(hm, min_val)
    
    norm = (hm - hm_min) / (hm_max - hm_min)
    return norm * (max_val - min_val) + min_val

def tile(hm: np.ndarray, tile_x: int, tile_y: int) -> np.ndarray:
    return np.tile(hm, (tile_y, tile_x))

def extract_patch(hm: np.ndarray, x: int, y: int, size: int) -> np.ndarray:
    return hm[y:y+size, x:x+size]