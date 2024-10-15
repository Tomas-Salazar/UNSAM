# Hipoteca


# def ejercicio_107():
#     """
#     Ejercicio 1.7: La hipoteca de David
#     David solicitó un crédito a 30 años para comprar una vivienda, con una tasa fija nominal anual del 5%. 
#     Pidió $500000 al banco y acordó un pago mensual fijo de $2684,11.
#     El siguiente es un programa que calcula el monto total que pagará David a lo largo de los años;
#     Copiá este código y correlo. Deberías obtener 966279.6 como respuesta.
#     """
#     saldo = 500000.0
#     tasa = 0.05
#     pago_mensual = 2684.11
#     total_pagado = 0.0
    
#     while saldo > 0:
#         saldo = saldo * (1+tasa/12) - pago_mensual
#         total_pagado = total_pagado + pago_mensual
        
#     print('Ejercicio 1.7:')
#     print('Total pagado', round(total_pagado, 2), '\n\n')
# # ejercicio_107()


# def ejercicio_108():
#     """
#     Ejercicio 1.8: Adelantos
#     Supongamos que David adelanta pagos extra de $1000/mes durante los primeros 12 meses de la hipoteca.
    
#     Modificá el programa para incorporar estos pagos extra y para que imprima el monto total pagado
#     junto con la cantidad de meses requeridos.
    
#     Cuando lo corras, este nuevo programa debería dar un pago total de 929965.62 en 342 meses.
    
#     Aclaración: aunque puede parecer sencillo, este ejercicio requiere que agregues una variable mes 
#     y que prestes bastante atención a cuándo la incrementás, con qué valor entra al ciclo y con qué valor sale del ciclo. 
#     Una posiblidad es inicializar mes en 0 y otra es inicializarla en 1. 
#     En el primer caso es probable que la variable salga del ciclo contando la cantidad de pagos que se hicieron.
#     En el segundo, ¡es probable que salga contando la cantidad de pagos más uno!
#     """
#     saldo = 500000.0
#     tasa = 0.05
#     pago_mensual = 2684.11
#     total_pagado = 0.0
#     mes = 0
    
#     while saldo > 0:
#         mes += 1
#         if mes <= 12:
#             saldo = saldo * (1+tasa/12) - pago_mensual - 1000
#             total_pagado = total_pagado + pago_mensual + 1000
#         else:
#             saldo = saldo * (1+tasa/12) - pago_mensual
#             total_pagado = total_pagado + pago_mensual
            
#     print('Ejercicio 1.8:')
#     print('Total pagado', round(total_pagado, 2))
#     print(mes, '\n\n')
# # ejercicio_108()


# def ejercicio_109():
#     """
#     Ejercicio 1.9: Calculadora de adelantos
#     ¿Cuánto pagaría David si agrega $1000 por mes durante cuatro años,
#     comenzando en el sexto año de la hipoteca (es decir, luego de 5 años)?
    
#     Modificá tu programa de forma que la información sobre pagos extras sea incorporada de manera versátil.
#     Agregá las siguientes variables antes del ciclo, para definir el comienzo, fin y monto de los pagos extras:
    
#     pago_extra_mes_comienzo = 61
#     pago_extra_mes_fin = 108
#     pago_extra = 1000
#     Hacé que el programa tenga en cuenta estas variables para calcular el total a pagar apropiadamente.
#     """
#     saldo = 500000.0
#     tasa = 0.05
#     pago_mensual = 2684.11
#     total_pagado = 0.0
#     mes = 0
#     pago_extra_mes_comienzo = 61
#     pago_extra_mes_fin = 108
#     pago_extra = 1000
    
#     while saldo > 0:
#         mes += 1
#         if mes >= pago_extra_mes_comienzo and mes <=pago_extra_mes_fin:
#             saldo = saldo * (1+tasa/12) - pago_mensual - pago_extra
#             total_pagado = total_pagado + pago_mensual + pago_extra
#         else:
#             saldo = saldo * (1+tasa/12) - pago_mensual
#             total_pagado = total_pagado + pago_mensual
            
#     print('Ejercicio 1.9:')
#     print('Total pagado', round(total_pagado, 2))
#     print(mes, '\n\n')
# # ejercicio_109()


# def ejercicio_110():
#     """
#     Ejercicio 1.10: Tablas
#     Modicá tu programa para que imprima una tabla mostrando el mes, el total pagado hasta el momento y el saldo restante.
#     La salida debería verse aproximadamente así:
    
#     1 2684.11 499399.22
#     2 5368.22 498795.94
#     3 8052.33 498190.15
#     4 10736.44 497581.83
#     5 13420.55 496970.98
#     ...
#     308 874705.88 3478.83
#     309 877389.99 809.21
#     310 880074.1 -1871.53
#     Total pagado:  880074.1
#     Meses:  310
#     """
#     saldo = 500000.0
#     tasa = 0.05
#     pago_mensual = 2684.11
#     total_pagado = 0.0
#     mes = 0
#     pago_extra_mes_comienzo = 61
#     pago_extra_mes_fin = 108
#     pago_extra = 1000
    
#     print('Ejercicio 1.10:')
#     while saldo > 0:
#         mes += 1
#         if mes >= pago_extra_mes_comienzo and mes <=pago_extra_mes_fin:
#             saldo = saldo * (1+tasa/12) - pago_mensual - pago_extra
#             total_pagado = total_pagado + pago_mensual + pago_extra
#             print(mes, round(total_pagado, 2), round(saldo, 2))
#         else:
#             saldo = saldo * (1+tasa/12) - pago_mensual
#             total_pagado = total_pagado + pago_mensual
#         print(mes, round(total_pagado, 2), round(saldo, 2))
        
#     print('Total pagado: ', round(total_pagado, 2))
#     print('Meses: ', mes, '\n\n')
# # ejercicio_110()


# def ejercicio_111():
#     """
#     Ejercicio 1.11: Hipoteca ajustado
#     Ya que estamos, corregí el código anterior de forma que el pago del último mes se ajuste a lo adeudado.
#     """
#     saldo = 500000.0
#     tasa = 0.05
#     pago_mensual = 2684.11
#     total_pagado = 0.0
#     mes = 0
#     pago_extra_mes_comienzo = 61
#     pago_extra_mes_fin = 108
#     pago_extra = 1000
    
#     print('Ejercicio 1.11:')
#     while saldo > 0:
#         mes += 1
#         if mes >= pago_extra_mes_comienzo and mes <=pago_extra_mes_fin:
#                 saldo = saldo * (1+tasa/12) - pago_mensual - pago_extra
#                 total_pagado = total_pagado + pago_mensual + pago_extra
#                 print(mes, round(total_pagado, 2), round(saldo, 2))
#         else:
#             saldo = saldo * (1+tasa/12) - pago_mensual
#             total_pagado = total_pagado + pago_mensual
#         print(mes, round(total_pagado, 2), round(saldo, 2))
        
#         if (saldo * (1+tasa/12)) < pago_mensual:     # Se modifica saldo -> (saldo * (1+tasa/12))
#             total_pagado += (saldo * (1+tasa/12))    # Se modifica saldo -> (saldo * (1+tasa/12))
#             saldo = 0
#             print(mes, round(total_pagado, 2), round(saldo, 2))
            
#     print('Total pagado: ', round(total_pagado, 2))
#     print('Meses: ', mes, '\n\n')
# ejercicio_111()

saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
mes = 0
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pago_extra = 1000
print('Ejercicio 1.11:')
while saldo > 0:
    mes += 1
    if mes >= pago_extra_mes_comienzo and mes <=pago_extra_mes_fin:
            saldo = saldo * (1+tasa/12) - pago_mensual - pago_extra
            total_pagado = total_pagado + pago_mensual + pago_extra
            print(mes, round(total_pagado, 2), round(saldo, 2))
    else:
        saldo = saldo * (1+tasa/12) - pago_mensual
        total_pagado = total_pagado + pago_mensual
    print(mes, round(total_pagado, 2), round(saldo, 2))
    if (saldo * (1+tasa/12)) < pago_mensual:     # Se modifica saldo -> (saldo * (1+tasa/12))
        total_pagado += (saldo * (1+tasa/12))    # Se modifica saldo -> (saldo * (1+tasa/12))
        saldo = 0
        print(mes, round(total_pagado, 2), round(saldo, 2))
print('Total pagado: ', round(total_pagado, 2))
print('Meses: ', mes, '\n\n')