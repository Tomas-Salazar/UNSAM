fosforos = [1,0,1,0,0,1,1,0,-1,1,0,0,1]

f_quemado = -1
f_prendido = 1
f_nuevo = 0

i = 0
for fosforo in fosforos:
    if fosforo == -1:
        break
    else:
        i += 1

vector = [1] * len(fosforos[:i])
print(vector)

# i = 0
# for fosforo in fosforos:
#     if fosforo == -1:
#         break
#     elif fosforo == 0:
#         if fosforos[i-1] or fosforos[i+1] == 1:
#             fosforo = 0
#             i += 1
#     else:
#         i += 1
#         pass

# vector = [1] * len(fosforos[:i])
# print(vector)