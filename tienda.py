def calcular_total(precio, cantidad):
    return precio * cantidad

def aplicar_descuento(total, descuento):
    if descuento < 0 or descuento > 100:
        raise ValueError("Descuento inválido")
    return total - (total * descuento / 100)

def procesar_pago(total, metodo):
    metodos_validos = ["tarjeta", "efectivo", "transferencia"]
    if metodo not in metodos_validos:
        raise ValueError("Método de pago no válido")
    return f"Pago de ${total} procesado con {metodo}"