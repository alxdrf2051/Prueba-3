import examfunctions as exf

while True:
    exf.cleanscreen()
    print("< Para continuar presione una tecla >")
    exf.presskey()

    print(f"""
    MATRICULAS
    San Charlis
    ------------------------
    1) Registrar Alumno
    2) Buscar Alumno
    3) Imprimir certificado
    0) Salir
    ------------------------
    """)
    option = int(input("Seleccione: "))

    exf.selection(option)
    if option == 0:
        break