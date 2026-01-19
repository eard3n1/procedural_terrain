import numpy as np
from noise import pnoise2

def perlin(width: int, height: int, scale: float, seed: int | None = None) -> np.ndarray:
    if seed is not None:
        np.random.seed(seed)
        base = np.random.randint(0, 100)
    else:
        base = 0

    hm = np.zeros((height, width), dtype=np.float32)
    for y in range(height):
        for x in range(width):
            hm[y, x] = pnoise2(x / scale, y / scale, octaves=1, base=base)
    return hm

def fbm(width: int, height: int, scale: float,
        octaves: int = 4, persistence: float = 0.5,
        lacunarity: float = 2.0, seed: int | None = None) -> np.ndarray:
    if seed is not None:
        np.random.seed(seed)
        base = np.random.randint(0, 100)
    else:
        base = 0

    hm = np.zeros((height, width), dtype=np.float32)
    for y in range(height):
        for x in range(width):
            hm[y, x] = pnoise2(
                x / scale, y / scale,
                octaves=octaves, persistence=persistence,
                lacunarity=lacunarity, base=base
            )
    return hm
