fosforos = [1,0,1,0,0,1,1,0,-1,1,0,0,1]

# f_quemado = -1
# f_prendido = 1
# f_nuevo = 0

def propagar(fosforos):
    for i in range(1, len(fosforos)):
        if fosforos[i-1] == 1 and fosforos[i] == 0:
            fosforos[i] = 1
    
    fosforos = fosforos[::-1]
    
    for i in range(1, len(fosforos)):
        if fosforos[i-1] == 1 and fosforos[i] == 0:
            fosforos[i] = 1
    
    return fosforos[::-1]


print(propagar(fosforos))

print(propagar([ 0, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 0]))
# [ 0, 0, 0,-1, 1, 1, 1, 1,-1, 1, 1, 1, 1]
print(propagar([ 0, 0, 0, 1, 0, 0]))
# [ 1, 1, 1, 1, 1, 1]