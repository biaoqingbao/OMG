#/bin/bash
#MINIMIZE EQUILIBRATE

/usr/local/gromacs/bin/gmx grompp -f 6.0.mdp -c start.gro -p system.top -n -o 6.0.tpr -maxwarn 2;
/usr/local/gromacs/bin/gmx mdrun -deffnm 6.0 -v -nt 4 -gpu_id 0; 

/usr/local/gromacs/bin/gmx grompp -f 6.1.mdp -c 6.0.gro -p system.top -n -o 6.1.tpr -maxwarn 2;
/usr/local/gromacs/bin/gmx mdrun -deffnm 6.1 -v -nt 4 -gpu_id 0; 

/usr/local/gromacs/bin/gmx grompp -f 6.2.mdp -c 6.1.gro -r 6.0.gro -p system.top -n -o 6.2.tpr -maxwarn 3;
/usr/local/gromacs/bin/gmx mdrun -deffnm 6.2 -v -nt 4 -gpu_id 0; 

/usr/local/gromacs/bin/gmx grompp -f 6.3.mdp -c 6.2.gro -r 6.0.gro -p system.top -n -o 6.3.tpr -maxwarn 3;
/usr/local/gromacs/bin/gmx mdrun -deffnm 6.3 -v -nt 4 -gpu_id 0; 

/usr/local/gromacs/bin/gmx grompp -f 6.4.mdp -c 6.3.gro -r 6.0.gro -p system.top -n -o 6.4.tpr -maxwarn 3;
/usr/local/gromacs/bin/gmx mdrun -deffnm 6.4 -v -nt 4 -gpu_id 0; 

/usr/local/gromacs/bin/gmx grompp -f 6.5.mdp -c 6.4.gro -r 6.0.gro -p system.top -n -o 6.5.tpr -maxwarn 3;
/usr/local/gromacs/bin/gmx mdrun -deffnm 6.5 -v -nt 4 -gpu_id 0;

/usr/local/gromacs/bin/gmx grompp -f 6.6.mdp -c 6.5.gro -r 6.5.gro -p system.top -n -o 6.6.tpr -maxwarn 3;
/usr/local/gromacs/bin/gmx mdrun -deffnm 6.6 -v -nt 4 -gpu_id 0; 

cp 6.6.gro ../umb/;
cp 6.6.gro ../prod/;
cp 6.0.gro ../umb/;
cp 6.0.gro ../prod/;
cp upp.itp ../prod/;
cp upp.itp ../umb/;
cp dow.itp ../prod/;
cp dow.itp ../umb/;
cp system.top ../prod/;
cp system.top ../umb/;
rm step*;
