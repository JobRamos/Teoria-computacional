def aceptarCadena(cadenaInput):
    cadenaAceptada = False
    estadoActual = []
    estadoAnterior = []

    estadoActual.append(0) # Estado inicial q0
    for caracter in cadenaInput:

        estadoAnterior = estadoActual
        estadoActual = []

        for estado in estadoAnterior:
            if estado == 0:
                if caracter == '0':
                    estadoActual.append(0)
                    estadoActual.append(1)
                elif caracter == '1':
                    estadoActual.append(0)
            elif estado == 1:
                if caracter == '0':
                    cadenaAceptada = False
                elif caracter == '1':
                    estadoActual.append(2)
                    cadenaAceptada = True
            elif estado == 2:
                if caracter == '0':
                    cadenaAceptada = False
                elif caracter == '1':
                    cadenaAceptada = False

        print(estadoActual)

    print(cadenaAceptada)

cadenaInput = "01"
aceptarCadena(cadenaInput)  
    



 