spaceindex = 0
with open('proxy.txt', 'r') as file:
    filteredproxies = open('filteredproxy.txt', 'w')
    for i in file.readlines():
        spaceindex = i.find(' ')
        i = i[0:spaceindex]
        filteredproxies.write(str(i) + '\n')