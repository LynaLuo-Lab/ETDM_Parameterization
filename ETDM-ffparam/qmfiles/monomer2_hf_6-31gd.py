#!/usr/bin/env python
import psi4,os,importlib
import numpy as np
mem="1000mb"
cpu=4
psi4.set_num_threads(cpu)
psi4.set_memory(mem)

psi4.core.set_output_file(os.path.dirname(os.path.abspath(__file__))+'/'+'.'.join(os.path.basename(__file__).split('.')[:-1])+'.out', False)




opttheory="hf"
optbasis="6-31g*"
options={'scf_type': 'df', 'g_convergence':'gau','freeze_core':'true'}
psi4.set_options(options)


psi4_xyz="""
0 1
h    	-4.899844	-2.655921	0.763734
o    	-4.605126	-3.566454	0.746336
h    	-3.670451	-3.512402	0.547106

"""
mol=psi4.geometry(psi4_xyz)
mol.update_geometry() # This update is required for psi4 to load the molecule
E=psi4.energy(opttheory+"/"+optbasis)
psi4.core.print_out('INTERACTION MONOMER ENERGY is : '+str(E) )