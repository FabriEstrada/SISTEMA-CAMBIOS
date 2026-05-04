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