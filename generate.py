import os
import yaml
from engine.noise import fbm
from engine.heightmap import normalize
from engine.mesh import heightmap_mesh, export_obj

with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

terrain_cfg = config["terrain"]
output_cfg = config["output"]

os.makedirs(output_cfg["mesh_dir"], exist_ok=True)

hm = fbm(
    terrain_cfg["width"],
    terrain_cfg["height"],
    scale=terrain_cfg["scale"],
    octaves=terrain_cfg.get("octaves", 4),
    seed=terrain_cfg.get("seed", None)
)
hm = normalize(hm)

vertices, faces = heightmap_mesh(
    hm,
    scale=1.0,
    height_scale=terrain_cfg.get("height_scale", 10)
)

output_path = os.path.join(output_cfg["mesh_dir"], output_cfg["mesh_name"])
export_obj(vertices, faces, output_path)
print(f"Terrain exported to: {output_path}")
