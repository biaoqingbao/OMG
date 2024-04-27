#!/bin/bash


# compute umbrella
for i in $(seq 1 2 93) 
do
    /usr/local/gromacs/bin/gmx grompp -f umb.mdp -c ../prod/conf${i}.gro -r ../prod/conf${i}.gro -n index.ndx -o umb${i}.tpr -p system.top -maxwarn 2;
    nohup /usr/local/gromacs/bin/gmx mdrun -deffnm umb${i} -nt 1 -gpu_id 0 -v &
done



exit;
