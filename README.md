# procedural_terrain
Minimal procedural terrain generation with 3D mesh export and visualization.

<img src="noises/fbm.png" width=256> <img src="noises/perlin.png" width=256>

## Features
- Procedurally generate heightmaps with fractal noise using FBM & Perlin
- Convert heightmaps to 3D mesh (OBJ format)
- Preview terrain in <b>Jupyter Notebook</b>
- Configurable via <code>config.yaml</code>

## Dependencies
- Numpy
- Matplotlib
- Noise
- Pyyaml

## Usage
1. Generate & export mesh:
    - ```bash
        python generate.py
        ```
    - This will produce an OBJ file in <code>meshes/</code> that can eventually be rendered in <b>Blender</b> or <b>Meshlab</b>

2. Visualize in <b>Jupyter Notebook</b>:
    - Open <code>visualization.ipynb</code> and run the cells. The notebook generates a procedural terrain and displays it in 3D using matplotlib.

## License
MIT License