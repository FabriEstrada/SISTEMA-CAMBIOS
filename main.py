def calcular_cambio(monto_pagado,costo_producto):
    if monto_pagado<costo_producto:
        return None,None
    
    monto_devolver = round(monto_pagado-costo_producto,2)
    billetes_monedas = [100, 50, 20, 10, 5, 1, 0.5, 0.25, 0.1, 0.05, 0.01]
    desglose = {}
    
    for dinero in billetes_monedas:
        dinero_aceptado = int(monto_devolver//dinero)
        monto_devolver = round(monto_devolver%dinero,2)
        
        if dinero_aceptado>0:
            desglose[dinero] = dinero_aceptado
    
    return desglose, monto_devolver

def guardar_cambios(monto_pagado,costo_producto, cambio, desglose):
    with open('Devolucion_cambios.txt', 'a', encoding='utf-8') as archivo:
        archivo.write("-----TRANSACCIONES-----\n")
        archivo.write(f"MONTO PAGADO: {monto_pagado}\n")
        archivo.write(f"COSTO PRODUCTO: {costo_producto}\n")
        archivo.write(f"TOTAL DEVOLVER: {cambio}\n")
        archivo.write("DESGLOSE CAMBIO:\n")
        
        for dinero,cantidad in desglose.items():
            archivo.write(f"{dinero}:{cantidad}\n")
        
        archivo.write("\n")

def mostrar_resultados_cambio(desglose,monto_devolver):
    print("----CAMBIO A DEVOLVER----")
    print(f"TOTAL: {monto_devolver}")
    print("CAMBIO: ")
    
    for dinero,cantidad in desglose.items():
        print(f"{dinero}:{cantidad}")

def ingreso_datos():
    while True:
        try:
            monto_pagado = float(input("Ingrese el monto que pagarás:\t"))
            costo_producto = float(input("Introduce el costo del producto:\t"))
            return monto_pagado, costo_producto
        
        except ValueError:
            print("Error al ingresar los datos, vuelve a intentarlo")

def menu():
    while True:
        print("----DEVOLUCION DE CAMBIOS----")
        print("1.  DEVOLVER CAMBIO          ")
        print("2.  SALIR DEL PROGRAMA       ")
        
        opcion_usuario = input("Ingrese una opcion:\t")
        
        match opcion_usuario:
            case "1":
                monto_pagado, costo_producto = ingreso_datos()
                desglose, monto_devolver = calcular_cambio(monto_pagado=monto_pagado,costo_producto=costo_producto)
                
                if desglose is None:
                    print("El monto pagado es insuficiente")              
                
                else:
                    mostrar_resultados_cambio(desglose,monto_devolver)
                    guardar_cambios(monto_pagado,costo_producto,monto_devolver,desglose)  
            
            case "2":
                print("Saliendo del programa")
                break
            
            case _:
                print("Opcion invalida, vuelve a internarlo\n")

menu()