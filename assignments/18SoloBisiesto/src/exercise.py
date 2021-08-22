"""Bisiesto;
    Año:
    if(year<=0)
  {
    {
    Dato incorrecto
    }
  }
    if(year % 4 == 0 and year % 100!= 0)
    {
     True
    }
     if(year % 4! =0)
    {
     False
    }
    if(year % 4 == 0 and year % 100== 0 and year% 400 != )
    {
      False
    }
   if(year % 100 == 0 and year % 400 == 0 and year % 4 == 0)
    {
      True
    }"""
def main():
    #escribe tu código abajo de esta línea
    year = int(input("Año:"))
    if(year<=0):
        print("Dato incorrecto")
    else:    
        if(year % 4 == 0 and year % 100!= 0):
          print(True)
        else:
            if(year % 4!= 0):
                print(False)
            else:
                if(year % 4 == 0 and year % 100== 0 and year% 400 != 0):
                     print(False)
                else:
                   if(year % 100 == 0 and year % 400 == 0 and year % 4 == 0):
                     print(True)
    







if __name__=='__main__':
    main()
