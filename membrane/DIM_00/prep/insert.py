#直接用insertfomat
with open("start.gro", "r") as f:
    # Read the contents of the second text file into a list of lines
    start = f.readlines()
    new=start[1].replace('21785',"21787")
    
    
with open("upp.gro", "r") as f:
    # Read the contents of the second text file into a list of lines
    upp = f.readlines()
    uppsit = []
    for i in [2,3]:

        
        n1 = 6672+i
        moleculetype1 = 'UPP'
        beads1 = upp[i][12:15]
        beads_n1 = 21782+i
        uppx = '{0:.3f}'.format(float(upp[i][22:28])+4.791)
        uppy = '{0:.3f}'.format(float(upp[i][30:36])+4.791)
        uppz = '{0:.3f}'.format(float(upp[i][38:44])+10.364)
        columns1=[n1,moleculetype1,beads1,beads_n1,uppx,uppy,uppz]
        # = ' 1dow'+'    '+beads+'    1'+'   '+dowx+'   '+dowy+'  '+dowz
        uppsite = f'{int(columns1[0]):5d}{columns1[1]:4s}   {columns1[2]:3s}{int(columns1[3]):5d}  {float(columns1[4]):6.3f}  {float(columns1[5]):6.3f}  {float(columns1[6]):6.3f}\n'
        #dowsite1 = '    2dow'+'    '+beads+'    2'+'   '+'0.000'+'   '+'0.000'+'   '+'0.000'+'\n'
        uppsit.append(uppsite)
        
        
        
        
        
        
        
        
        
with open("dow.gro", "r") as f:
    # Read the contents of the second text file into a list of lines
    dow = f.readlines()
    dowsit = []
    for i in [2,3]:

        n1 = 6674+i
        moleculetype1 = 'DOW'
        beads1 = dow[i][12:15]
        beads_n1 = 21784+i
        dowx = '{0:.3f}'.format(float(dow[i][22:28])+4.791)
        dowy = '{0:.3f}'.format(float(dow[i][30:36])+4.791)
        dowz = '{0:.3f}'.format(float(dow[i][38:44])+1.093)
        columns1=[n1,moleculetype1,beads1,beads_n1,dowx,dowy,dowz]
        # = ' 1dow'+'    '+beads+'    1'+'   '+dowx+'   '+dowy+'  '+dowz
        dowsite = f'{int(columns1[0]):5d}{columns1[1]:4s}   {columns1[2]:3s}{int(columns1[3]):5d}  {float(columns1[4]):6.3f}  {float(columns1[5]):6.3f}  {float(columns1[6]):6.3f}\n'
        #dowsite1 = '    2dow'+'    '+beads+'    2'+'   '+'0.000'+'   '+'0.000'+'   '+'0.000'+'\n'
        dowsit.append(dowsite)
    
    
    
    
    
    
    
        
with open('start.gro', "w") as f:
    f.write(start[0])
    f.write(new)
    for i in range(2,21785):
        f.write(start[i])
    for i in uppsit:
        f.write(i)
    for i in dowsit:
        f.write(i)
    f.write(start[-1])
