dim_c1-nda#!/bin/bash
source /usr/local/gromacs-2022.4/bin/GMXRC
rm pullf-files.dat tpr-files.dat pullf-upp-files.dat pullf-dow-files.dat *upp_pullf.xvg *dow_pullf.xvg


# compute umbrella
touch tpr-files.dat
touch pullf-files.dat
for i in $(seq 1 2 82) 
do
    echo "umb${i}.tpr" >> tpr-files.dat
    echo "umb${i}_pullf.xvg" >> pullf-files.dat
done

gmx wham -it tpr-files.dat -if pullf-files.dat -o c1-nda-down-pot.xvg -hist c1-nda-down-hist.xvg -is coord-sel_down.dat  -unit kCal -e 10000
gmx wham -it tpr-files.dat -if pullf-files.dat -o c1-nda-upp-pot.xvg -hist c1-nda-upp-hist.xvg -is coord-sel_upp.dat  -unit kCal -e 10000
exit;
