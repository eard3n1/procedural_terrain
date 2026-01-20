import os
import yaml
from engine.noise import perlin, fbm
from engine.heightmap import normalize
from engine.mesh import heightmap_mesh, export_obj

with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

terrain = config["terrain"]
noise_cfg = config["noise"]
output = config["output"]

os.makedirs(output["mesh_dir"], exist_ok=True)

if noise_cfg["type"] == "perlin":
    hm = perlin(
        terrain["width"],
        terrain["height"],
        scale=noise_cfg["scale"],
        seed=noise_cfg.get("seed")
    )

elif noise_cfg["type"] == "fbm":
    hm = fbm(
        terrain["width"],
        terrain["height"],
        scale=noise_cfg["scale"],
        octaves=noise_cfg.get("octaves", 4),
        seed=noise_cfg.get("seed")
    )

else:
    raise ValueError(f"Unknown noise type: {noise_cfg["type"]}")

hm = normalize(hm)

vertices, faces = heightmap_mesh(
    hm,
    height_scale=noise_cfg["height_scale"]
)

output_path = os.path.join(output["mesh_dir"], output["mesh_name"])
export_obj(vertices, faces, output_path)

print(f"Terrain generated using: {noise_cfg["type"]} noise")
print(f"Exported to: {output_path}")
