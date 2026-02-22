import os
import yaml
from engine.noise import perlin, simplex, fbm, billow, ridged
from engine.mesh import normalize
from engine.mesh import heightmap_mesh, export_obj

with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

terrain = config["terrain"]
noise = config["noise"]
output = config["output"]

os.makedirs(output["mesh_dir"], exist_ok=True)

if noise["type"] == "perlin":
    hm = perlin(
        terrain["width"],
        terrain["height"],
        scale=noise["scale"],
        seed=noise.get("seed")
    )

elif noise["type"] == "fbm":
    hm = fbm(
        terrain["width"],
        terrain["height"],
        scale=noise["scale"],
        octaves=noise.get("octaves", 4),
        persistence=noise.get("persistence", 0.5),
        lacunarity=noise.get("lacunarity", 2.0),
        seed=noise.get("seed")
    )

elif noise["type"] == "simplex":
    hm = simplex(
        terrain["width"],
        terrain["height"],
        scale=noise["scale"],
        seed=noise.get("seed")
    )

elif noise["type"] == "billow":
    hm = billow(
        terrain["width"],
        terrain["height"],
        scale=noise["scale"],
        octaves=noise.get("octaves", 4),
        seed=noise.get("seed")
    )

elif noise["type"] == "ridged":
    hm = ridged(
        terrain["width"],
        terrain["height"],
        scale=noise["scale"],
        octaves=noise.get("octaves", 4),
        seed=noise.get("seed")
    )

else: raise ValueError(f"Unknown noise type: {noise['type']}")

hm = normalize(hm)
vertices, faces = heightmap_mesh(hm, height_scale=noise["height_scale"])
output_path = os.path.join(output["mesh_dir"], output["mesh_name"])

if __name__ == "__main__":
    export_obj(vertices, faces, output_path)
    print(f"Terrain generated using: {noise['type'].upper()} noise")
    print(f"Exported to: {output_path}")