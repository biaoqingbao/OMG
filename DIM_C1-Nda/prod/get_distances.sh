#!/bin/bash

#################################################
# get_distances.sh
#
#   Script iteratively calls gmx distance and
#   assembles a series of COM distance values
#   indexed by frame number, for use in
#   preparing umbrella sampling windows.
#
# Written by: Justin A. Lemkul, Ph.D.
#    Contact: jalemkul@vt.edu
#
#################################################
gmx trjconv -s prod.tpr -f prod.xtc -o conf.gro -sep
#select 0 system
# compute distances
for (( i=0; i<93; i++ ))
do
    gmx distance -s prod.tpr -f conf${i}.gro -n index.ndx -select 'com of group "UPP" plus com of group "MEMBRANE"' -oxyz dist_upp${i}.xvg 
done

# compile summary
touch summary_distances_upp.dat
for (( i=0; i<93; i++ ))
do
    d=`tail -n 1 dist_upp${i}.xvg | awk '{print $4}'`
    echo "${i} ${d}" >> summary_distances_upp.dat
    rm dist_upp${i}.xvg
done

# compute distances
for (( j=0; j<93; j++ ))
do
    gmx distance -s prod.tpr -f conf${j}.gro -n index.ndx -select 'com of group "DOW" plus com of group "MEMBRANE"' -oxyz dist_dow${j}.xvg
done

# compile summary
touch summary_distances_dow.dat
for (( j=0; j<93; j++ ))
do
    k=`tail -n 1 dist_dow${j}.xvg | awk '{print $4}'`
    echo "${j} ${k}" >> summary_distances_dow.dat
    rm dist_dow${j}.xvg
done


exit;
