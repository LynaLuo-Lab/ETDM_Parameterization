#!/bin/bash
#SBATCH -J psi4QM
#SBATCH --partition=defq
#SBATCH --get-user-env
#SBATCH --nodes=1
#SBATCH --tasks-per-node=4
##SBATCH --gres=gpu:1
#SBATCH --time=08:00:00

eval "$(command conda 'shell.bash' 'hook' 2> /dev/null)"
conda init bash
source activate ffpenv
which python

scriptName=$1
logFileName=`echo $1 | sed "s:.py:.out:g"`
#logFileName=psi4.log
echo "Running $scriptName. Saving result to $logFileName"
python $scriptName &> $logFileName
#/home/lyna/anaconda3/envs/ffpenv/bin/psi4/ $scriptName &> $logFileName

echo "Done"
