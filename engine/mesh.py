import numpy as np

def heightmap_mesh(hm: np.ndarray, scale: float = 1.0, height_scale: float = 1.0) -> tuple[np.ndarray, np.ndarray]:
    h, w = hm.shape
    vertices = np.zeros((h * w, 3), dtype=np.float32)

    for y in range(h):
        for x in range(w):
            idx = y * w + x
            vertices[idx] = [x * scale, hm[y, x] * height_scale, y * scale]

    faces = []
    for y in range(h - 1):
        for x in range(w - 1):
            i = y * w + x
            faces.append([i, i + 1, i + w])
            faces.append([i + 1, i + w + 1, i + w])
    faces = np.array(faces, dtype=np.int32)
    return vertices, faces

def normalize(hm: np.ndarray, min_val: float = 0.0, max_val: float = 1.0) -> np.ndarray:
    hm_min, hm_max = hm.min(), hm.max()

    if hm_max - hm_min == 0:
        return np.full_like(hm, min_val)
    
    norm = (hm - hm_min) / (hm_max - hm_min)
    return norm * (max_val - min_val) + min_val

def export_obj(vertices: np.ndarray, faces: np.ndarray, path: str) -> None:
    with open(path, 'w') as f:
        for v in vertices:
            f.write(f"v {v[0]} {v[1]} {v[2]}\n")
        for face in faces:
            f.write(f"f {face[0] + 1} {face[1] + 1} {face[2] + 1}\n")
