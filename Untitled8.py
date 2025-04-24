def evaluar (nombre,nota1,nota2):
    promedio=(nota1+nota2)/2
    
    if promedio >= 6:
        return f"{nombre} aprobo con {promedio}"
    else:
        return f"{nombre} desaprobo con {promedio}"
        
resultado=evaluar("martina",10,8)
print(resultado)