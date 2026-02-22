from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import yaml
import os

with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

terrain = config["terrain"]
output = config["output"]
noise = config["noise"]
mesh = os.path.join(output["mesh_dir"], output["mesh_name"])

width, height = int(terrain["width"]), int(terrain["height"])
height_scale = int(noise["height_scale"])

if not os.path.exists(mesh):
    raise FileNotFoundError("obj file not found, run generate.py first.")

app = Ursina()

terrain = Entity(
    model=mesh,
    collider="mesh",
    double_sided=True
)

Sky()

player = FirstPersonController(
    position=(width / -2, height_scale * 2, height / 2),
    gravity=0.5,
    jump_height=4,
    speed=10
)

if __name__ == "__main__":
    window.fullscreen = True
    app.run()
