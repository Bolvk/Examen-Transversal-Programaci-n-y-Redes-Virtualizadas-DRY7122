while True:
    acl=int(input("Ingrese el tipo de ACL a consultar: "))

    if acl <=100:
        print("La ACL consultada es de tipo estándar.")
    else:
        print("La ACL consultada es de tipo extendida")