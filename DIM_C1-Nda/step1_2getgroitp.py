#直接用  用automartini 格式  1upp 2 upp
with open("equ.gro", "r") as f:
    # Read the contents of the second text file into a list of lines
    equ = f.readlines()
    
with open('upp.gro', "w") as f:
    upp = equ
    uppsit = []
    for i in [2]:
        n1 = 1
        moleculetype1 = 'UPP'
        beads1 = upp[i][12:15]
        beads_n1 = i-1
        x1 = '{0:.3f}'.format((float(upp[i][22:28])-float(upp[i+1][22:28]))*5/8)
        y1 = '{0:.3f}'.format((float(upp[i][30:36])-float(upp[i+1][30:36]))*5/8)
        z1 = '{0:.3f}'.format((float(upp[i][38:44])-float(upp[i+1][38:44]))*5/8)
        columns1=[n1,moleculetype1,beads1,beads_n1,x1,y1,z1]
        # = ' 1UPP'+'    '+beads+'    1'+'   '+uppx+'   '+uppy+'  '+uppz
        uppsite1 = f'{int(columns1[0]):5d}{columns1[1]:4s}   {columns1[2]:3s}{int(columns1[3]):5d}  {float(columns1[4]):6.3f}  {float(columns1[5]):6.3f}  {float(columns1[6]):6.3f}\n'
        #uppsite1 = '    2UPP'+'    '+beads+'    2'+'   '+'0.000'+'   '+'0.000'+'   '+'0.000'+'\n'
        
        n2 = 2
        moleculetype2 = 'UPP'
        beads2 = upp[i+1][12:15]
        beads_n2 = i
        x2 = '{0:.3f}'.format((float(upp[i][22:28])-float(upp[i+1][22:28]))*(-3/8))
        y2 = '{0:.3f}'.format((float(upp[i][30:36])-float(upp[i+1][30:36]))*(-3/8))
        z2 = '{0:.3f}'.format((float(upp[i][38:44])-float(upp[i+1][38:44]))*(-3/8))
        columns2=[n2,moleculetype2,beads2,beads_n2,x2,y2,z2]
        # = ' 1UPP'+'    '+beads+'    1'+'   '+uppx+'   '+uppy+'  '+uppz
        uppsite2 = f'{int(columns2[0]):5d}{columns2[1]:4s}   {columns2[2]:3s}{int(columns2[3]):5d}  {float(columns2[4]):6.3f}  {float(columns2[5]):6.3f}  {float(columns2[6]):6.3f}\n'

        
        #uppsite1 =    1UPP    C01    1  -0.032  -0.075   0.102
        #uppsite1 = 6673ION     CL21783   6.071   8.052   0.172
        uppsit.append(uppsite1)
        uppsit.append(uppsite2)
    opening="""UPP gro from https://doi.org/10.1038/s41597-020-0391-0
    2
"""
    
    f.write(opening)
    for i in uppsit:
        f.write(i)
        
    ending="""  10.00000  10.00000  10.00000"""
    f.write(ending)
    
    
    
    
    
with open('dow.gro', "w") as f:
    dow = equ
    dowsit = []
    for i in [2]:
        n1 = 1
        moleculetype1 = 'DOW'
        beads1 = dow[i][12:15]
        beads_n1 = i-1
        x1 = '{0:.3f}'.format((float(dow[i][22:28])-float(dow[i+1][22:28]))*5/8)
        y1 = '{0:.3f}'.format((float(dow[i][30:36])-float(dow[i+1][30:36]))*5/8)
        z1 = '{0:.3f}'.format((float(dow[i][38:44])-float(dow[i+1][38:44]))*5/8)
        columns1=[n1,moleculetype1,beads1,beads_n1,x1,y1,z1]
        # = ' 1dow'+'    '+beads+'    1'+'   '+dowx+'   '+dowy+'  '+dowz
        dowsite1 = f'{int(columns1[0]):5d}{columns1[1]:4s}   {columns1[2]:3s}{int(columns1[3]):5d}  {float(columns1[4]):6.3f}  {float(columns1[5]):6.3f}  {float(columns1[6]):6.3f}\n'
        #dowsite1 = '    2dow'+'    '+beads+'    2'+'   '+'0.000'+'   '+'0.000'+'   '+'0.000'+'\n'
        
        n2 = 2
        moleculetype2 = 'DOW'
        beads2 = dow[i+1][12:15]
        beads_n2 = i
        x2 = '{0:.3f}'.format((float(dow[i][22:28])-float(dow[i+1][22:28]))*(-3/8))
        y2 = '{0:.3f}'.format((float(dow[i][30:36])-float(dow[i+1][30:36]))*(-3/8))
        z2 = '{0:.3f}'.format((float(dow[i][38:44])-float(dow[i+1][38:44]))*(-3/8))
        columns2=[n2,moleculetype2,beads2,beads_n2,x2,y2,z2]
        # = ' 1dow'+'    '+beads+'    1'+'   '+dowx+'   '+dowy+'  '+dowz
        dowsite2 = f'{int(columns2[0]):5d}{columns2[1]:4s}   {columns2[2]:3s}{int(columns2[3]):5d}  {float(columns2[4]):6.3f}  {float(columns2[5]):6.3f}  {float(columns2[6]):6.3f}\n'

        
        #dowsite1 =    1dow    C01    1  -0.032  -0.075   0.102
        #dowsite1 = 6673ION     CL21783   6.071   8.052   0.172
        dowsit.append(dowsite1)
        dowsit.append(dowsite2)
    opening="""DOW gro from https://doi.org/10.1038/s41597-020-0391-0
    2
"""
    
    f.write(opening)
    for i in dowsit:
        f.write(i)
        
    ending="""  10.00000  10.00000  10.00000"""
    f.write(ending)
    
    
#直接用get itp from paper 
with open("mol3.itp", "r") as f:
    # Read the contents of the second text file into a list of lines
    itp = f.readlines()
    
with open('upp.itp', "w") as f:
    for i in itp:
        f.write(i)
    
    
with open('dow.itp', "w") as f:
    for i in itp:
        f.write(i)

