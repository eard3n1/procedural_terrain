from pathlib import Path

from engine.noise import select
from engine.mesh import normalize, heightmap_mesh, export_obj
from engine.config import load_config


config = load_config("config.yaml")

noise = config["noise"]
output = config["output"]

hm = select(noise["type"], config)
hm = normalize(hm)

vertices, faces = heightmap_mesh(hm, noise["height_scale"])
output_path = Path(output["mesh_dir"]) / output["mesh_name"]

if __name__ == "__main__":
    output_path.parent.mkdir(parents=True, exist_ok=True)
    export_obj(vertices, faces, output_path)

    print(f"Terrain generated | noise: {noise['type'].capitalize()} | seed: {noise['seed'] if noise['seed'] else 'RANDOM'}")
    print(f"Exported to: {output_path}")