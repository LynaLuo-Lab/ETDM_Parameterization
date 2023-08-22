#!/bin/bash

for f in  *wat*.py;
 do echo sbatch Run_qm_script.slurm.bash $f; done
