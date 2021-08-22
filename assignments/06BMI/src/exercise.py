"""MIC
PESO EN KG:;

ALTURA EN M:;

    indice = peso / altura^2);
    
  if( peso<=0 or altura<=0)
  {
    Revisa tus datos, alguno de ellos es erróneo.
  }
    else
  {
   if(indice<20)
   {
      PESO BAJO
   }
    else
    {
    if(20 <= indice < 25)
         NORMAL
    }
    else:
    {
    if(25 <= indice < 30)
    SOBREPESO
    }
    else:
    {
    if(30 <= indice < 40)
      OBESIDAD
    }
    else:
    {
    if( indice >= 40)
    OBESIDAD MORBIDA
    }
"""
def main():
    #escribe tu código abajo de esta línea
    peso = float(input("Peso en kg:"))
    altura = float(input("Altura en m:"))
    indice = float (peso / altura ** 2)
    if( peso<=0 or altura<=0):
        print("Revisa tus datos, alguno de ellos es erróneo.")
    else:
        if(indice<20):
          print("PESO BAJO")
        else:
             if(20 <= indice < 25):
                print("NORMAL")
             else:
                if(25 <= indice < 30):
                    print("SOBREPESO")
                else:
                    if(30 <= indice < 40):
                       print("OBESIDAD")
                    else:
                        if( indice >= 40):
                            print("OBESIDAD MORBIDA")

if __name__=='__main__':
    main()