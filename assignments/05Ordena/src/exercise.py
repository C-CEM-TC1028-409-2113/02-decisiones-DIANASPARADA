""" 05Ordena;

   x =Ingresa el primer número:";
    y=Ingresa el segundo número:;
   z =Ingresa el tercer número:;
  {
    if( x < y and x < z)
  {
    {
       menor= x
    }
     if(y<z)
    {
       medio = y
       mayor = z
    }
    {
       medio = z
       mayor = y 
    }
  }
    if(y<xand y<z)
  {
    {menor = y;}
      if(x<z)
    {
        medio =x
        mayor =z
    }
    {
        medio=z
        mayor=x
    }
  }
  if(z<x and z<y)
  
    {
      menor=z
    }
      if(x<y)
    {
      medio =x 
      mayor =y 
    }
    {
       medio =y 
       mayor= x  
    }
  
   menor 
   medio 
   mayor  """
def main():
    # Escribe el código adecuado para completar el programa
    x = int(input("Ingresa el primer número:"))
    y = int(input("Ingresa el segundo número:"))
    z = int(input("Ingresa el tercer número:"))
    menor = x
    medio = y
    mayor = z
    if( x < y and x < z):
        menor= x
        if(y<z):
            medio = y
            mayor = z
        else:
            medio = z
            mayor = y 
    elif( y< x and y < z):
          menor = y
          if ( x<z):
              medio =x
              mayor =z
          else:
              medio=z
              mayor=x
    elif(z<x and z<y):
            menor=z
            if(x<y):
              medio =x 
              mayor =y 
            else: 
                medio =y 
                mayor= x  
    print(str(menor))
    print(str(medio))
    print(str(mayor))
    

            
                  
                
    

if __name__=='__main__':
    main()
