import numpy as np
from noise import pnoise2, snoise2

def _base(seed: int) -> int:
    if seed == 0:
        seed = np.random.randint(0, 100)
    np.random.seed(seed)
    return seed

def perlin(
    width: int,
    height: int,
    scale: float,
    seed: int
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
    octaves: int,
    persistence: float,
    lacunarity: float,
    seed: int
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
    seed: int
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
    octaves: int,
    persistence: float,
    lacunarity: float,
    seed: int
) -> np.ndarray:

    hm = fbm(width, height, scale, octaves, persistence, lacunarity, seed)
    return np.abs(hm)

def ridged(
    width: int,
    height: int,
    scale: float,
    octaves: int,
    persistence: float,
    lacunarity: float,
    seed: int
) -> np.ndarray:

    hm = fbm(width, height, scale, octaves, persistence, lacunarity, seed)
    return 1 - np.abs(hm)

def select(noise_type: str, c: dict) -> np.ndarray:
    if noise_type == "perlin":
        return perlin(
            c["terrain"]["width"],
            c["terrain"]["height"],
            c["noise"]["scale"],
            c["noise"]["seed"]
        )
    elif noise_type == "fbm":
        return fbm(
            c["terrain"]["width"],
            c["terrain"]["height"],
            c["noise"]["scale"],
            c["noise"]["octaves"],
            c["noise"]["persistance"],
            c["noise"]["lacunarity"],
            c["noise"]["seed"]
        )
    elif noise_type == "simplex":
        return simplex(
            c["terrain"]["width"],
            c["terrain"]["height"],
            c["noise"]["scale"],
            c["noise"]["seed"]
        )
    elif noise_type == "billow":
        return billow(
            c["terrain"]["width"],
            c["terrain"]["height"],
            c["noise"]["scale"],
            c["noise"]["octaves"],
            c["noise"]["persistance"],
            c["noise"]["lacunarity"],
            c["noise"]["seed"]
        )
    elif noise_type == "ridged":
        return ridged(
            c["terrain"]["width"],
            c["terrain"]["height"],
            c["noise"]["scale"],
            c["noise"]["octaves"],
            c["noise"]["persistance"],
            c["noise"]["lacunarity"],
            c["noise"]["seed"]
        )