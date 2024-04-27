#!/bin/bash

rm pullf-files.dat tpr-files.dat pullf-upp-files.dat pullf-dow-files.dat *upp_pullf.xvg *dow_pullf.xvg


# compute umbrella
touch tpr-files.dat
touch pullf-files.dat
for i in $(seq 1 2 89) 
do
    echo "umb${i}.tpr" >> tpr-files.dat
    echo "umb${i}_pullf.xvg" >> pullf-files.dat
done

/usr/local/gromacs/bin/gmx wham -it tpr-files.dat -if pullf-files.dat -o down-pot.xvg -hist down-hist.xvg -is coord-sel_down.dat  -unit kCal -e 10000
/usr/local/gromacs/bin/gmx wham -it tpr-files.dat -if pullf-files.dat -o upp-pot.xvg -hist upp-hist.xvg -is coord-sel_upp.dat  -unit kCal -e 10000
exit;
