while True:
    acl=int(input("Ingrese el tipo de ACL a consultar: "))

    if acl <=99:
        print("La ACL consultada es de tipo estándar.")
    elif acl <=199:
        print("La ACL consultada es de tipo extendida")
    else:
        print("Ingrese una ACL correcta")