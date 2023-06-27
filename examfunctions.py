import os
import numpy
import msvcrt
import time
import random

matriculados = numpy.empty([10,7], object)
mt = matriculados

grey = ("\033[30m")
green = ("\033[32m")
red = ("\033[31m")
yellow = ("\033[33m")
close = ("\033[0m")

def cleanscreen():
    os.system('cls')

def presskey():
    msvcrt.getch()

def waittime(seconds):
    time.sleep(seconds)

def selection(option):
    if option>=1 and option<=3:
        if option == 1:
            print("""REGISTRAR ALUMNO\n________________""")
            rut = int(input(f"{grey}*Ingrese RUT de alumno SIN punto ni guión: "))
            if rut not in mt:
                nombre = input(f"{grey}*Ingrese nombre completo de Alumno:")
                while len(nombre) < 10:
                    print(f"{red}*Nombre ingresado demasiado CORTO.{close}")
                    nombre = input(f"{grey}*Ingrese nombre completo de Alumno:")
                else:
                    edad = int(input(f"{grey}*Ingrese la edad del alumno: "))
                    while edad<4:
                        print(f"{red}*Edad invalida para matricula.{close}")
                        edad = int(input(f"{grey}*Ingrese edad valida para alumno: "))
                    else:
                        genero = input(f"""{grey}*Cual es el genero del alumno?:\nM = Masculino\nF = Femenino\n*Respuesta: """)
                    promedio = float(input(f"{grey}Promedio del alumno: "))
                    dd = int(input(f"""{grey}*Ingrese fecha en la que se esta efectuando esta matricula:\nDia: """))
                    mm = int(input(f"{grey}Mes: "))
                    aaaa = int(input(f"{grey}Año: "))
                    fecha = (f"{dd}/{mm}/{aaaa}")
                    apoderado = input(f"{grey}*Ingrese nombre de apoderado del alumno: ")
                    for x in range(10):
                        mt[x,0] = rut
                        mt[x,1] = nombre
                        mt[x,2] = edad
                        mt[x,3] = genero
                        mt[x,4] = promedio
                        mt[x,5] = fecha
                        mt[x,6] = apoderado
                        break
                    cleanscreen()
                    print(f"{green}*Procesando datos...{close}")
                    waittime(1)
                    cleanscreen()
                    print(f"{yellow}*Alumno registrado con Éxito.{close}")
                    waittime(2)
                    
            else:
                print(f"*{red}RUT de alumno ya registrado.{close}")
                waittime(2)

        elif option == 2:
            print("""BUSCAR ALUMNO\n_____________""")
            rut = int(input(f"*{grey}Ingrese RUT de alumno SIN puntos ni guión: {close}"))
            if rut in mt:
                print(f"{yellow}*Alumno encontrado.{close}")
                print(f"{green}*Cargando información...{close}")
                waittime(1)
                cleanscreen()
                for x in range(10):
                    if mt[x,0] == rut:
                        print(f"RUT:{mt[x,0]} | NOMBRE: {mt[x,1]} | EDAD: {mt[x,2]} | GENERO: {mt[x,3]}\n| PROMEDIO: {mt[x,4]}| FECHA MATRICULA: {mt[x,5]}| APODERADO: {mt[x,6]} ")
                        presskey()
            else:
                print(f"{red}*Alumno NO registrado.{close}")
                waittime(2)
        elif option == 3:
            print("""IMPRESION DE CERTIFICADOS\n_________________________""")
            rut = int(input(f"{grey}*Ingrese RUT de alumno.{close}"))
            if rut in mt:
                for x in range(10):
                    if mt[x,0] == rut:
                        cleanscreen()
                        print("""IMPRESION DE CERTIFICADOS\n_________________________""")
                        print(f"1) Anotaciones de Alumno\n2) Certificado de Notas\n3) Certificado alumno regular")
                        option = int(input("Seleccione: "))
                        while option<=1 and option>=3:
                            cleanscreen()
                            print(f"{red}Opción inválida, reintente.{close}")
                            print("""IMPRESION DE CERTIFICADOS\n_________________________""")
                            print(f"1) Anotaciones de Alumno\n2) Certificado de Notas\n3) Certificado alumno regular")
                            option = int(input("Seleccione: "))
                        else:
                            if option == 1:
                                print(f"{green}*Imprimiendo certificado...{close}")
                                waittime(1)
                                cleanscreen()
                                anotaciones = ["Grita en clase", "Falta el respeto a alumnos y a profesora", "Mantiene el orden en sala de clases", "Buen comportamiento", "Come en clases", "Insulta a su compañera", "No se baña D:"]
                                print(f"ANOTACIONES DEL ALUMNO\n\nAnotacion 1\nFecha:{random.randrange(1,29)}/{random.randrange(1,12)}/2023\nMotivo: {random.choice(anotaciones)}\n")
                                print(f"Anotacion 2\nFecha:{random.randrange(1,29)}/{random.randrange(1,12)}/2023\nMotivo: {random.choice(anotaciones)}\n")
                                print(f"Anotacion 3\nFecha:{random.randrange(1,29)}/{random.randrange(1,12)}/2023\nMotivo: {random.choice(anotaciones)}")
                                presskey()
                            elif option == 2:
                                print(f"{green}*Imprimiendo certificado...{close}")
                                waittime(1)
                                cleanscreen()
                                print(f"CERTIFICADO DE NOTAS ACTUALES\nNota 1: {random.randint}")
                                print(f"Nota 2: {random.randint}")
                                print(f"Nota 3: {random.randint}")
                                presskey()
                            elif option == 3:
                                print(f"{green}*Imprimiendo certificado...{close}")
                                waittime(1)
                                cleanscreen()
                                print(f"CERTIFICADO DE ALUMNO REGULAR\n_______________________________\nSe certifica que la persona presente {mt[x,1]} de RUT {mt[x,0]}, es alumno regular de la Institucion SAN CHARLIS.\n\n Firma ATTE. Coordinador de Enseñanza")
                                presskey()
            else:
                print(f"{red}*Alumno NO registrado.{close}")
                waittime(2)

    elif option == 0:
        cleanscreen()
        print(f"{yellow}*Gracias por su visita, vuelva pronto!{close}")
    else:
        print(f"{red}*Opción no válida, porfavor reintente.{close}")
        waittime(2)
