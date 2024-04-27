with open("start_jia_1.gro", "r") as f:
    # Read the contents of the second text file into a list of lines
    lines2 = f.readlines()
lines3 = lines2[2:-1]

lines = []
for i in lines3:
    if i[5:9] != 'ION ':
        lines.append(i[5:9])
    elif i[12:15] == ' CL':
        lines.append('CL  ')
    elif i[12:15] == ' NA':
        lines.append('NA  ')

lst = lines
prev_elem = lst[0]
count = 1
grolist = []
for elem in lst[1:]:
    if elem == prev_elem:
        count += 1
    else:
        grolist.append(prev_elem+' ' + str(count))
        prev_elem = elem
        count = 1
grolist.append(prev_elem+' ' + str(count))  # 最后一行


toplist = []
for i in grolist:
    if i[0:5] == "DPCE ":
        dpce = int(i[5:])//9
        toplist.append('DPCE '+str(dpce))
    if i[0:5] == "CHOL ":
        chol = int(i[5:])//8
        toplist.append('CHOL '+str(chol))
    if i[0:5] == "BCN  ":
        bcn = int(i[5:])//6
        toplist.append('BCN '+str(bcn))
    if i[0:5] == "PW   ":
        pw = int(i[5:])//3
        toplist.append('PW '+str(pw))
    if i[0:5] == "UPP  ":
        upp = int(i[5:])//2
        toplist.append('UPP '+str(upp))
    if i[0:5] == "DOW  ":
        dow = int(i[5:])//2
        toplist.append('DOW '+str(dow))
    if i[0:5] == "NA   ":
        na = int(i[5:])//1
        toplist.append('NA '+str(na))
    if i[0:5] == "CL   ":
        cl = int(i[5:])//1
        toplist.append('CL '+str(cl))

with open('toplist.top', "w") as f:
    opening = """#include "martini_v2.2P.itp"
#include "martini_v2.0_lipids_all_201506.itp"
#include "martini_v2.0_ions.itp"
#include "CHOL.itp"
; Then ITP of specific molecule
#include "upp.itp"
#include "dow.itp"

[ system ]
; name
Martini system

[ molecules ]
; name        number"""
    f.write(opening + "\n")
    for i in toplist:
        f.write(i+"\n")
