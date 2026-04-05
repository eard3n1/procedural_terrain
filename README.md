# procedural_terrain
Minimal procedural terrain generation with 3D mesh export, render & visualization.

<img src="noises/fbm.png" width=256> <img src="noises/perlin.png" width=256>

## Features
- Procedural heightmap generation using fractal noise
- Convert heightmaps to 3D mesh (OBJ format)
- Render the mesh using **Ursina Engine**
- Static visualization / analysis
- Configurable via yaml

## Dependencies
- Python 3.10+
- Numpy
- Matplotlib
- Noise
- Pyyaml
- Ursina

## Usage
1. Install requirements:
    - ```bash
        pip install -r requirements.txt
        ```
    - Noise might require wheel setup.
2. Generate & export mesh:
    - ```bash
        python generate.py
        ```
    - This will produce an OBJ file in <code>meshes/</code> that can eventually be rendered in **Blender** or **Meshlab**.

3. Render using generated mesh:
    - ```bash
        python render.py
        ```
    - This will render the mesh in a first person 3D environment to have a simple look.

4. Visualization in notebook:
    - Open <code>analysis.ipynb</code>. The notebook generates an illustration of the terrain in a simple 3D graph:
    
    <img src="noises/billow.png" width=256> <img src="noises/ridged.png" width=256>

## License
MIT License