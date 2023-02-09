with open('proxy.txt', 'r') as file:
    filteredproxies = open('filteredproxy.txt', 'w')
    for i in file.readlines():
        i = i[0:i.find(' ')]
        filteredproxies.write(str(i) + '\n')
        
