#-------------------------------------------#

# Universidad del Valle de Guatemala
# Departamento de Computación
# Organizador de Computadoras y Assembler

# Javier Alejandro Ramírez Heredia-21600  
# Mario Andres Cristales Cardona-21631
# 24/01/2022
   
# Ejercicio 5

#-------------------------------------------#
from pickle import TRUE


def main():

    estado = True


    while estado:
        menu()
        opcion = int(input("¡Bienvenido!, Que opcion del menu quieres elegir:   "))
        
        if opcion == 1:
            calculadoraCA2()
            input()
        elif opcion== 2:

           Respuesta = input('¿Desea salir del Programa:  ')
           if Respuesta == "si":
               print ("FeliZ Dia =)")
               
               estado = False  
           
           else:
               main()

        else:

            print('Ingrese una opcion correcta del menu')

            print(main())
        
def menu():

        print('''
             ------------------------------------------------------
             -    ___   _                       _                 -
             -   | _ ) (_)  _ _    __ _   _ _  (_)  ___   ___     -
             -   | _ \ | | | ' \  / _` | | '_| | | / _ \ (_-<     -
             -   |___/ |_| |_||_| \__,_| |_|   |_| \___/ /__/     -
             ------------------------------------------------------
             ------------------------------------------------------
             -  (1) Ingresar un Numero Binario                    -
             -  (2) Salir                                         -
             ------------------------------------------------------          
            ''')


 
def Com_A_2(lista):
    print("------------------------------------------------------")
    print("lista ingresada: ")
    print("".join(lista))

    for i in range(len(lista)):

        num = int(lista[i])
        if num == 1 :
            lista[i] = '0'
        elif num == 0:
            lista[i] = '1'
    
    newLista="".join(lista)
    
    a = newLista
    b = "1"
    max_len = max(len(a), len(b))
    a = a.zfill(max_len)
    b = b.zfill(max_len)

    resultado = ''

    carry = 0

    for i in range(max_len - 1, -1, -1):
        r = carry
        r += 1 if a[i] == '1' else 0
        r += 1 if b[i] == '1' else 0
        resultado = ('1' if r % 2 == 1 else '0') + resultado

        carry = 0 if r < 2 else 1

    if carry != 0:
        resultado = '1' + resultado
        
    print("------------------------------------------------------")
    print("el complemento a 2 del número ingresado es: ")

    print(resultado.zfill(max_len))
    
def bin_a_dec(binario):
    pos = 0
    decimal = 0
    binario = binario[::-1]
    for digito in binario:
        multiplicar = 2**pos
        decimal += int(digito) * multiplicar
        pos += 1
    return decimal


Estado = True

def calculadoraCA2():
    contador = 0
    numBin = input("Ingrese un numero binario de 8 bits:")
    listB = list(numBin)
    if int(len(listB) == 8):
        try :
            for i in range(len(listB)):

                num = int(listB[i])
                if num == 1 or num == 0 :
                    print("correcto")

                elif num != 1 or num != 0:
                    print("el dígito: ",num,
                  " no es 1 o 0, ingrese el dato de nuevo")
                    contador = contador +1

            if contador == 0 :
                Estado = False
        except Exception as e :
            print("error en el ciclo for", e)
    else:
        print("los bits ingresados no coinciden con la cantidad requerida (7)")

    print("------------------------------------------------------")
    print("el numero ingresado en decimales es:",bin_a_dec(numBin))
    print( Com_A_2(listB))
    


if __name__ == '__main__':
    main()















    

      
