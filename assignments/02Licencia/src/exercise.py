

"""Licencia;
edad = "Ingresa tu edad:"
      if (Si tienes menos de 18)
    {
        No cumples con los requisitos }
      else
       { 
         Tienes identificacion oficial (s/n)
       if(Respuesta = s)
          {
           Tramite de licencia concedido}
       else
    {
      {if Respuesta = n
       { No cumples requisitos}
      else
      { Respuesta incorrecta }"""

def main():
    edad = int(input("Ingresa tu edad:"))
    if (edad<=0):
       print("Respuesta incorrecta")
    else:
       if (edad>=18):
           id = input("¿Tienes identificación oficial?(s/n):")
           if (id == "s"):
              print("Trámite de licencia concedido")
           else:
              if(id == "n"):
                print("No cumples requisitos")
              else:
                print("Respuesta incorrecta")
       else:
           print("No cumples requisitos")
if __name__ == '__main__':
    main()
