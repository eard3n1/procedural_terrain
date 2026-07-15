# strata_forge
A minimal procedural terrain generation pipeline. Composites fractal noise into heightmaps, converts them into 3D meshes, and drops you into a walkable first-person <a href="https://www.ursinaengine.org/">Ursina</a> environment.

<img src="noises/fbm.png" width=256> <img src="noises/perlin.png" width=256>

## Features
- Noise presets: Perlin, Simplex, FBm, Billow, Ridged
- Heightmap to mesh conversion with OBJ export
- First-person mesh preview using Ursina Engine
- Jupyter notebook terrain analysis and visualization

## Requirements
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

    - The `noise` package may require a wheel build on some platforms:
      1. Install [Visual Studio Build Tools for C++](https://visualstudio.microsoft.com/visual-cpp-build-tools/)

      2. During setup, select **Desktop development with C++**
      
      3. Try noise installation again:
          - ```bash
            pip install noise
            ```
          - Wheel build should succeed.

2. Generate & export mesh:
   - ```bash
     python generate.py
     ```
    
    - Outputs an OBJ file to `meshes/`, ready to import into Blender or MeshLab.

3. Preview in first-person:
    - ```bash
      python render.py
      ```

    - Loads the generated mesh in a minimal Ursina environment for first-person visualization.

4. Visualization in notebook:

    Open `analysis.ipynb` for heightmap inspection and 3D terrain visualization.

    <img src="noises/billow.png" width=256> <img src="noises/ridged.png" width=256>

## License
MIT License
