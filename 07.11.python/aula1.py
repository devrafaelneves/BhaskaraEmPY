import math

def calcula_delta(a,b,c):
    return (b**2) - 4*a*c


def calcula_x1(a,b,c,delta):
    return (-1*b+math.sqrt(delta))/(2*a)


def calcula_x2(a,b,c,delta):
    return (-1*b-math.sqrt(delta))/(2*a)



a = float(input("digita a"))
b = float (input('digite o valor b '))
c = float(input('digite o valor c '))

delta = calcula_delta(a,b,c)
x1 = calcula_x1(a,b,c,delta)
x2 = calcula_x2(a,b,c,delta)
print(delta)
print(x1)
print(x2)




# def raiz_quadrada(a):
#     return math.sqrt(a)


# def potencia (a,b):
#     return a**b
   


# def somar (a,b):
#     return a+b

#     def subtrair(a,b):
#             return a-b

#             def mult (a,b):
#              a*b

#     def div(a,b):
#             return a/b
           
           
           
#             print (mult (10,20))
#             print(div (10,20))
#             print(somar(10,20))
#             print(subtrair(30,20))
#             print(potencia(10,20))
#             print (raiz_quadrada(9))

# a= float (input('digite o valor a '))
# b= float (input('digite o valor b '))
# print (a+b)


# a = 10
# b = 20 
# c = a + b 
# print (c)

