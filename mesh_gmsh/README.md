
mesh produced with GMSH script .geo , rearranged extrusion with .py script, finally converted to OGS format with the aid of a modification of FEniCS tool to convert meshes.

Original tool  available here https://github.com/FEniCS/dolfin/blob/master/site-packages/dolfin_utils/meshconvert/meshconvert.py

To create the gmsh mesh, simply download the .geo and run
>> gmsh 0_mesh.geo -3 0_mesh.msh
then download in the same folder the python script and  execute it
