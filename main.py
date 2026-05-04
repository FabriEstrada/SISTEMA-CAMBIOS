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