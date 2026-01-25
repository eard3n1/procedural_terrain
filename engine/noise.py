import numpy as np
from noise import pnoise2, snoise2


def _base(seed: int | None) -> int:
    if seed is None:
        return 0
    np.random.seed(seed)
    return np.random.randint(0, 100)

def perlin(
    width: int,
    height: int,
    scale: float,
    seed: int | None = None
) -> np.ndarray:
    
    base = _base(seed)
    hm = np.zeros((height, width), dtype=np.float32)

    for y in range(height):
        for x in range(width):
            hm[y, x] = pnoise2(x / scale, y / scale, base=base)
    return hm

def fbm(
    width: int,
    height: int,
    scale: float,
    octaves: int = 4,
    persistence: float = 0.5,
    lacunarity: float = 2.0,
    seed: int | None = None
) -> np.ndarray:

    base = _base(seed)
    hm = np.zeros((height, width), dtype=np.float32)

    for y in range(height):
        for x in range(width):
            hm[y, x] = pnoise2(
                x / scale,
                y / scale,
                octaves=octaves,
                persistence=persistence,
                lacunarity=lacunarity,
                base=base
            )
    return hm

def simplex(
    width: int,
    height: int,
    scale: float,
    seed: int | None = None
) -> np.ndarray:

    base = _base(seed)
    hm = np.zeros((height, width), dtype=np.float32)

    for y in range(height):
        for x in range(width):
            hm[y, x] = snoise2(x / scale, y / scale, base=base)
    return hm

def billow(
    width: int,
    height: int,
    scale: float,
    octaves: int = 4,
    seed: int | None = None
) -> np.ndarray:

    hm = fbm(width, height, scale, octaves, seed=seed)
    return np.abs(hm)

def ridged(
    width: int,
    height: int,
    scale: float,
    octaves: int = 4,
    seed: int | None = None
) -> np.ndarray:

    hm = fbm(width, height, scale, octaves, seed=seed)
    return 1.0 - np.abs(hm)
