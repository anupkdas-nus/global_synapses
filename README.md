# global_synapses
global synapse simulator

How to use the scripts: 
1. There are two different folders in the repository and they are from PyNN. 
2. The PyNN-distpackages is the folder that shall be in the python distpackages. This means that when we install PyNN the PyNN folder would be located in the distpackages, here is where we place the PyNN implementation(The distpackages fodler in repo).
3. The script test.py was used to test the functionality of the PyNN-Carlsim interface incrementatlly after each functionality was implemented. 
4. The PyNN-distpackages contains various packages(supported simulators) including carlsim(small letters for consistency with others) this is where the implementation of the interface is done. Currently this supports a few basic functionalities such as creating a group, connection betwen group of neurons and setting CUBA or COBA mode(I think it supports a few more but I cannot recollect). 
5. This carlsim package also contains carlsim python library(generated by SWIG) carlsim.py and the library itself is carlsim.so. These can be used without any dependecy on other files. just import carlsim to use the library. 
6. The function names are the same as the C++ counterpart and it uses the same arguments as well with a slight change in type of the argument depeding on pointer or array etc(can be easily found out).
7. To use this scripts isntall PyNn and place the carlsim package in the PyNN folder. It also contains the carlsim python library so making a test script to test your extended functionality will be easy. 
