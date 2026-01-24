from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import yaml
import os

with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

output_cfg = config["output"]
mesh_path = os.path.join(output_cfg["mesh_dir"], output_cfg["mesh_name"])

if not os.path.exists(mesh_path):
    raise FileNotFoundError("obj file not found, run generate.py first.")

app = Ursina()

terrain = Entity(
    model=mesh_path,
    collider="mesh",
    double_sided=True
)

Sky()

player = FirstPersonController(
    position=(0, 30, 0),
    gravity=0.5
)

def update():
    if player.y < -50:
        player.position = (0, 30, 0)

app.run()
