#!/bin/bash


# compute umbrella
for i in $(seq 1 2 41) 
do
    gmx grompp -f umb.mdp -c ../prod/conf${i}.gro -r ../prod/conf${i}.gro -n index.ndx -o umb${i}.tpr -p system.top -maxwarn 2
    nohup gmx mdrun -deffnm umb${i} -nt 1 -gpu_id 0 -v &
done

for j in $(seq 41 2 93)
do
    gmx grompp -f umb.mdp -c ../prod/conf${j}.gro -r ../prod/conf${j}.gro -n index.ndx -o umb${j}.tpr -p system.top -maxwarn 2
    nohup gmx mdrun -deffnm umb${j} -nt 1 -gpu_id 1 -v &
done


exit;
