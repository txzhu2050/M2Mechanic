# M2Mechanic
## Public executable files and example cases of M2Mechanic (published paper at DATE 26) 

### M2Mechanic
M2Mechanic is an efficient warpage simulator for complex 2.5-D/3-D IC structures based on a novel meshing algorithm and a modified 2-D layerwise plate theory. It can also be used for obtaining strain/stress distributions. M2Mechanic can be coupled with external thermal simulators, or it can perform thermal simulation itself with an integrated thermal simulation module. The 2-D algorithm can only be used for warpage simulation under constant thermal loads for the moment.

Our simulator supports
1. Flexible 2.5-D/3-D/hybrid structures;
2. Detailed floorplan and power definations;
3. Heterogeneous and anistropic material properties.

Details can be found in our paper, which can be cited as:
```
@inproceedings{zhu2026efficient, 
        title={Efficient Warpage Simulation of Complex 2.5-D/3-D IC Structures with Novel Meshing Algorithm and Layerwise Plate Theory},
        author={Zhu, Tianxiang and Wang, Qipan and Lin, Yibo and Wang, Runsheng},
        booktitle={2026 Design, Automation \& Test in Europe Conference (DATE)},
        pages={1--7},
        year={2026}
    }
```

### Requirements
M2Mechanic is currently written in Python and built upon the open-sourced high performance C++ FEM backend, Dolfinx. For more information, please visit their website https://fenicsproject.org.

Recommended package version:
```
python 3.12.7
dolfinx 0.9.0
dolfinx_mpc 0.9.1
gmsh 4.13.1
petsc4py 3.23.0
numpy 1.26.4
scipy 1.15.2
pandas 2.2.2
```

### Usage
```
mpirun -np number_of_process python path/to/M2Mechanic.py -xml path/to/xml/file -config path/to/config/file --output_dir path/to/output/dir
```

Example:
```
cd cases/chiplet
mpirun -np 8 python ../../src/M2Mechanic.py -xml package.xml -config sim.config
```

The input files are:
```
.xml file: describe the 2.5-D/3-D IC structure; specify paths to the material file and the external temperature results
.config file: include configurations of the simulator.
```

For more details, please refer to the example cases, which cover various methods of use. The user's manual is also comming soon.

### Contact
```
txzhu@pku.edu.cn
```


