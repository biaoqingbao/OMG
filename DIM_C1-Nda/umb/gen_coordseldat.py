f1 = open('coord-sel_upp.dat', 'w')
for i in range(45):
    f1.write('1 0\n')

f1.close()

f1 = open('coord-sel_down.dat', 'w')
for i in range(45):
    f1.write('0 1\n')

f1.close()
