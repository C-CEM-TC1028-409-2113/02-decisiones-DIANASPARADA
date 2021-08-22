"""09;
    Introduce los cm:;

   FORMULAS Y VARIABLES;

    km = (c//100000)
    Restante_1 = (c-(km*100000))
    metros = (Restante_1 // 100)
    Restante_2 = (Restante_1 - (metros * 100))
    centi = (Restante_2//1)
    
    if( km>0)
    {
        kilometros
    }
    if( metros>0)
    {
        Metros
    }
    if(centi>0 )
    {
       Centimetros
    } """
def main():
    # Escribe tu código abajo de esta línea
    c = int(input("Introduce los cm:"))

    km = (c//100000)
    Restante_1 = (c-(km*100000))
    metros = (Restante_1 // 100)
    Restante_2 = (Restante_1 - (metros * 100))
    centi = (Restante_2//1)
    
    if( km>0):
        print(str(km), "km")
    if( metros>0 ):
        print(str(metros), "m")
    if(centi>0 ):
        print(str(centi), "cm")
                
                            
if __name__ == '__main__':
    main()


