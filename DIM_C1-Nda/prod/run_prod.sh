#!/bin/bash
#GENERATE CONFORMATIONS


gmx grompp -f prod.mdp -c 6.6.gro -r 6.0.gro -p system.top -n -o prod.tpr -maxwarn 3
gmx mdrun -deffnm prod -nt 4 -gpu_id 0 -v
gmx trjconv -f prod.xtc -n index.ndx -s prod.tpr -pbc whole -o prod_pbc.xtc
#select 0 system
./get_distances.sh


#CHECK YOUR RESULTS 
#download to local computer and check the trajectory of both beads:
#vmd 6.6.gro prod_pbc.xtc
