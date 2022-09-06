from datetime import datetime

def obtener_hora():
    now = datetime.now()
    return(now.strftime("%H:%M:%S"))

def display(cola):
    posicion = 1
    print("\n\nA continuacion se mostrara un breve resumen de los textos que hay en la pila:\n")
    for text in cola:
        if (len(text) > 60):
            print("["+str(posicion)+"] "+text[0:60])
        else:
            print("["+str(posicion)+"] "+text)
        posicion += 1
    return posicion-1

cola = []
log = open("log.txt", "w")
while (True):
    print("\nMENU: ")
    print("\n[1] Introducir texto")
    print("[2] Imprimir algun texto")
    print("[3] Comparar tamaño entre textos")
    print("[4] Salir\n")
    opcion_main = input("Seleccione la accion a realizar: ")

    if (opcion_main == "1"):
        hora_actual = obtener_hora()
        log.write(hora_actual + ": Se escojio introducir un texto\n")
        texto = input("\nIntroduzca el texto que quiera ingresar: ")
        hora_actual = obtener_hora()
        log.write(hora_actual + ": Se introdujo el texto: " + texto + "\n")
        cola.append(texto)
        print("\nEl texto se agrego exitosamente")
    elif (opcion_main == "2"):
        hora_actual = obtener_hora()
        log.write(hora_actual + ": Se escojio imprimir un texto\n")
        opcion_text = ""
        while (opcion_text != "No"):
            if (opcion_text == "Si"):
                hora_actual = obtener_hora()
                log.write(hora_actual + ": Se escribio \"Si\" en el menu de volver a imprimir un texto\n")
            tamaño_cola = display(cola)
            opcion_text = input("\n\nSeleccione el texto a imprimir (Escriba \"Volver\" para salir): ")
            if (opcion_text == "Volver"):
                hora_actual = obtener_hora()
                log.write(hora_actual + ": Se escribio \"Volver\" en el menu de texto a imprimir\n")
                break
            try:
                if (int(opcion_text) > tamaño_cola):
                    hora_actual = obtener_hora()
                    log.write(hora_actual + ": Se introdujo una opcion que no esta en el menu de impresion\n")
                    print("\nOpcion invalida, porfavor seleccione una opcion mostrada en pantalla")
                else:
                    print("\n" + cola[int(opcion_text)-1])
                    hora_actual = obtener_hora()
                    log.write(hora_actual + ": Se imprimio un texto exitosamente\n")
                    opcion_text = input("\nTexto impreso exitosamente, desea imprimir otro texto? (Escriba \"Si\" o \"No\"): ")
                    while (opcion_text != "Si" and opcion_text != "No"):
                        opcion_text = input("\nOpcion invalida, porfavor escriba \"Si\" o \"No\": ")
                        hora_actual = obtener_hora()
                        log.write(hora_actual + ": Se introdujo una opcion distinta a \"Si\" o \"No\"\n")
            except ValueError:
                print("\nOpcion invalida, porfavor seleccione una opcion mostrada en pantalla")
                hora_actual = obtener_hora()
                log.write(hora_actual + ": Se introdujo una letra como opcion en el menu de impresion\n")
        hora_actual = obtener_hora()
        log.write(hora_actual + ": Se escribio \"No\" en el menu de volver a imprimir un texto\n")
    elif (opcion_main == "3"):
        opcion_text = ""
        while (opcion_text != "No"):
            if (opcion_text == "Si"):
                hora_actual = obtener_hora()
                log.write(hora_actual + ": Se escribio \"Si\" en el menu de volver a comparar textos\n")
            tamaño_cola = display(cola)
            opcion_comparar1 = input("\n\nSeleccione el primer texto a comparar (Escriba \"Volver\" para salir): ")
            if (opcion_comparar1 == "Volver"):
                hora_actual = obtener_hora()
                log.write(hora_actual + ": Se escribio \"Volver\" al momento de seleccionar el primer texto\n")
                break
            hora_actual = obtener_hora()
            log.write(hora_actual + ": Se escojio el texto " + opcion_comparar1 + " como primer texto a comparar\n")
            opcion_comparar2 = input("Seleccione el segundo texto a comparar (Escriba \"Volver\" para salir): ")
            if (opcion_comparar2 == "Volver"):
                hora_actual = obtener_hora()
                log.write(hora_actual + ": Se escribio \"Volver\" al momento de seleccionar el primer texto\n")
                break
            hora_actual = obtener_hora()
            log.write(hora_actual + ": Se escojio el texto " + opcion_comparar2 + " como segundo texto a comparar\n")
            try:
                if ((int(opcion_comparar1) > tamaño_cola) or (int(opcion_comparar2) > tamaño_cola)):
                    print("\nUna o ambas opciones son invalidas, porfavor seleccione una opcion mostrada en pantalla")
                    hora_actual = obtener_hora()
                    log.write(hora_actual + ": Se introdujo una opcion que no esta en el menu de comparacion\n")
                else:
                    len_text1 = len(cola[(int(opcion_comparar1)-1)])
                    len_text2 = len(cola[(int(opcion_comparar2)-1)])
                    print("Largo del primer texto: " + str(len_text1))
                    print("Largo del segundo texto: " + str(len_text2))
                    total = len_text1 - len_text2

                    if (total > 0):
                        print("\nEl primer texto es mas largo que el segundo, teniendo "+str(total)+" caracteres mas")
                    elif (total < 0):
                        print("\nEl segundo texto es mas largo que el primero, teniendo "+str(abs(total))+" caracteres mas")
                    else:
                        print("\nAmbos textos tienen el mismo largo")
                    hora_actual = obtener_hora()
                    log.write(hora_actual + ": Comparacion de textos exitosa\n")
                    opcion_text = input("\nDesea comparar otros textos? (Escriba \"Si\" o \"No\"): ")
                    while (opcion_text != "Si" and opcion_text != "No"):
                        opcion_text = input("\nOpcion invalida, porfavor escriba \"Si\" o \"No\": ")
                        hora_actual = obtener_hora()
                        log.write(hora_actual + ": Se introdujo una opcion distinta a \"Si\" o \"No\"\n")
            except ValueError:
                print("\nUna o ambas opciones son invalidas, porfavor seleccione una opcion mostrada en pantalla")
                hora_actual = obtener_hora()
                log.write(hora_actual + ": Se introdujo una letra como opcion en el menu de comparacion\n")
    elif (opcion_main == "4"):
        hora_actual = obtener_hora()
        log.write(hora_actual + ": Se cierra el programa\n")
        break
    else:
        hora_actual = obtener_hora()
        log.write(hora_actual + ": Se introdujo una opcion que no esta en el menu principal\n")
        print("\nOpcion invalida, porfavor seleccione una opcion mostrada en pantalla")
log.close()
                    
        

    
