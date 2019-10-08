# Programa simulacion de lo clasico a lo cuantico

# Operaciones Con Vectores y Matrices

**Sistemas Clasicos Deterministicos:**
Muestra el estado de un sistema clasico, despues de ciertos clicks de tiempo.

**Sistema Probabilistco:**

Muestra la probabilidad de que un elemento se encuentre en algun estado del sistema, despues de determinados clicks de tiempo.

**Sistema Cuantico:**

Muestra la probabilidad de que una particula,foton,electron se encuentre en algun estado del sistema, despues de determinados clicks de tiempo.





# Pre-requisitos 📋
![GitHub Logo](https://www.python.org/static/img/python-logo@2x.png)

Para poder usar esta libreria es necesario tener instalado python, si no se tiene, la descarga e instalación es como sigue:
Primero descargamos el programa de la página oficial:

![GitHub Logo](https://www.wikihow.com/images_en/thumb/1/14/Install-Python-Step-1-Version-2.jpg/v4-760px-Install-Python-Step-1-Version-2.jpg)
![GitHub Logo](https://www.wikihow.com/images_en/thumb/4/45/Install-Python-Step-2-Version-2.jpg/v4-760px-Install-Python-Step-2-Version-2.jpg)

Cuando termine de descargar hay que proceder a instalarlo:

![GitHub Logo](https://www.wikihow.com/images_en/thumb/f/fb/Install-Python-Step-4-Version-2.jpg/v4-760px-Install-Python-Step-4-Version-2.jpg)

 # Instalación de Operaciones Con Vectores y Matrices 🔧
Primero: 
![myimage-alt-tag](https://scontent-bog1-1.xx.fbcdn.net/v/t1.15752-9/69874998_750459472059681_3913524228170711040_n.png?_nc_cat=109&_nc_oc=AQnAHS7ixOACxFw9VZIuFwoJKytHypC0c9lCVCRXGIho84rLNJiPg55F4K2wzo2JtM4&_nc_ht=scontent-bog1-1.xx&oh=a5c49974e0f359c923370686c6d86f6e&oe=5DC80CBF) 


Segundo:
 
![myimage-alt-tag](https://scontent-bog1-1.xx.fbcdn.net/v/t1.15752-9/70678769_2608600409202096_5609513835909087232_n.png?_nc_cat=101&_nc_oc=AQk5bpFi6zdMwJygs22sr6bhKf6P0KFDBJcOLnnaSZ9jYS3D6cWzyF1gNewZOjFT8VI&_nc_ht=scontent-bog1-1.xx&oh=e2d320ca92637cf344136875a2d80a61&oe=5E031292) 


Luego abrimos el IDLE de python
![myimage-alt-tag](https://scontent-bog1-1.xx.fbcdn.net/v/t1.15752-9/69689175_475682319649824_1117122535582859264_n.jpg?_nc_cat=109&_nc_oc=AQncBZgHUk5xJWCUqEApXR0Jd2E_1hWuW4OYr4XiwiEsvhj0uYlr9-O6NLlb4Zkrjjs&_nc_ht=scontent-bog1-1.xx&oh=cebd69f85b23f8abab07548473591ce2&oe=5E03C862) 


Buscamos el archivo y lo abrimos

![myimage-alt-tag](https://scontent-bog1-1.xx.fbcdn.net/v/t1.15752-9/70778647_472135196670206_3245147181413302272_n.png?_nc_cat=100&_nc_oc=AQnxgrcF3EZL88MTpAI2jwDLclRoa72WBttNAznDA6vnFR88UHvB2M_Z9St3VWkMFoQ&_nc_ht=scontent-bog1-1.xx&oh=c41b02ea85e3f01c83da8b696a565ec9&oe=5DF5DC77) 

y listo!.


# Uso 
Para poder usar esta libreria es necesario:
Si lo prefiere puede usar el codigo depruebas y modificar los valores a su necesidad, o puede importar las librerias a su  archivo creado o crear uno nuevo.

![myimage-alt-tag](https://scontent-bog1-1.xx.fbcdn.net/v/t1.15752-9/71843673_440177066683469_5991082127804858368_n.png?_nc_cat=111&_nc_oc=AQnxII9gJV_fLRvidbgSfIOD9rFmKuFYEquhh7irBMmseF71IPX-G54oqJI3if9pQ3A&_nc_ht=scontent-bog1-1.xx&oh=c1b8cd68a2e6f4f261d5c870e4403a70&oe=5E3732EC) 


# Ejecutando las pruebas ⚙️
![myimage-alt-tag](https://scontent-bog1-1.xx.fbcdn.net/v/t1.15752-9/71056822_2372414239692893_8796974929317724160_n.png?_nc_cat=107&_nc_oc=AQnxxKZxfDKNnTtRb7C7eWKHYEAEdA2K2HcZYb26oOFbhMuXHbqxi1s8eh25obYUSnQ&_nc_ht=scontent-bog1-1.xx&oh=a2292a87113e6bf2af5f086ea2fe7361&oe=5E374446) 


![myimage-alt-tag](https://scontent-bog1-1.xx.fbcdn.net/v/t1.15752-9/70761707_682192895613485_8970786002314461184_n.png?_nc_cat=108&_nc_oc=AQnEM5LExX-nD9XvqGRQ6eYvxyioB_lxbcA2BNy1eXX5NFXiDo23a_SDX3TMs4CcC7k&_nc_ht=scontent-bog1-1.xx&oh=0379683216afe39ff016102489095870&oe=5E0240A1) 

# ...Explicacion:
**state** 
Al simulador se le ingresa una matriz con el estado inicial del sistema, este es el primer argumento de la funcion state, el segundo argumento es un vector que representa el estado del sistema al momento t, asi con el tercer argumento que indica la cantidad de clics(t+n), el simulador mostrara si el resultado es correcto, es decir si es igual al vector que esta antes de la llamada a la funcion.

    def test1(self):
        self.assertEqual([[0], 
                          [0],
                          [12],
                          [5], 
                          [1],
                          [9]], 
                         Programasimulaciondeloclasicoalocuantico.state([[False, False, False, False, False, False], 
                                                                                                          [False, False, False, False, False, False], 
                                                                                                          [False, True, False, False, False, True], 
                                                                                                          [False, False, False, True, False, False], 
                                                                                                          [False, False, True, False, False, False], 
                                                                                                          [True, False, False, False, True, False]],
                                                                                                         
                                                                                                         [[6],[2],[1],[5],[3],[10]],             2))   
                                                                                                         
**stateprobabilistic** 
A la funcion se le ingresa  una matriz (primer argumento) la cual describe la forma en que se moverá una particula después de hacer clic una vez.
El segundo argumento de la funcion es un vector que meustra los estados con la particula en 0
El tercer argumento es la cantidad de clics(t+n), y con esto el simulador mostrara si el resultado es correcto, es decir si es igual al vector que esta antes de la llamada a la funcion.

    def test2(self):
        self.assertEqual([[0.0], 
                          [0.0], 
                          [0.0], 
                          [0.16666666666666666],
                          [0.16666666666666666],
                          [0.3333333333333333],
                          [0.16666666666666666],
                          [0.16666666666666666]],
                         Programasimulaciondeloclasicoalocuantico.stateprobabilistic([[0, 0, 0, 0, 0, 0, 0, 0], 
                                                                                      [0.5, 0, 0, 0, 0, 0, 0, 0], 
                                                                                      [0.5, 0, 0, 0, 0, 0, 0, 0],
                                                                                      [0, 0.3333333333333333, 0, 1, 0, 0, 0, 0],
                                                                                      [0, 0.3333333333333333, 0, 0, 1, 0, 0, 0],
                                                                                      [0, 0.3333333333333333, 0.3333333333333333, 0, 0, 1, 0, 0],
                                                                                      [0, 0, 0.3333333333333333, 0, 0, 0, 1, 0],
                                                                                      [0, 0, 0.3333333333333333, 0, 0, 0, 0, 1]],
                                                                                     
                                                                                     [[1],[0],[0],[0],[0],[0],[0],[0]],       2))
                                                                                     
                                                                                     
 **quantumstate**                                                                                    
A la funcion se le ingresa  una matriz (primer argumento) la cual describe la forma en que se moverá una particula en un sistema cuantico después de hacer clic una vez.
El segundo argumento de la funcion es la cantidad de clics(t+n), y con esto el simulador mostrara si el resultado es correcto, es decir si es igual a la matriz que esta antes de la llamada a la funcion.  


    def test3(self): 
        self.assertEqual([[0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0],
                          [0.1666666666666667, 0.3333333333333334, 0, 1, 0, 0, 0, 0],
                          [0.1666666666666667, 0.3333333333333334, 0, 0, 1, 0, 0, 0],
                          [0, 0.3333333333333334, 0.3333333333333334, 0, 0, 1, 0, 0],
                          [0.1666666666666667, 0, 0.3333333333333334, 0, 0, 0, 1, 0],
                          [0.1666666666666667, 0, 0.3333333333333334, 0, 0, 0, 0, 1]],
                         
                         Programasimulaciondeloclasicoalocuantico.quantumstate([[(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],
                                                                                [(0.7071067811865475, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],
                                                                                [(0.7071067811865475, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],
                                                                                [(0, 0), (-0.4082482904638631, 0.4082482904638631), (0, 0), (1, 0), (0, 0), (0, 0), (0, 0), (0, 0)],
                                                                                [(0, 0), (-0.4082482904638631, -0.4082482904638631), (0, 0), (0, 0), (1, 0), (0, 0), (0, 0), (0, 0)],
                                                                                [(0, 0), (0.4082482904638631, -0.4082482904638631), (-0.4082482904638631, 0.4082482904638631), (0, 0), (0, 0), (1, 0), (0, 0), (0, 0)],
                                                                                [(0, 0), (0, 0), (-0.4082482904638631, -0.4082482904638631), (0, 0), (0, 0), (0, 0), (1, 0), (0, 0)],
                                                                                [(0, 0), (0, 0), (0.4082482904638631, -0.4082482904638631), (0, 0), (0, 0), (0, 0), (0, 0), (1, 0)]]                  ,2))

# Ejemplo1:

    def stateprobabilistic(X,Y,n):
    result =[[0 for x in range(len(Y[0]))] for y in range(len(Y))]
    p=X
    result2=[[0 for x in range(len(p[0]))] for y in range(len(p))]
    
    for h in range(n-1):
        for i in range(len(X)):
           
           for j in range(len(p[0])):
               
               for k in range(len(p)):
                   result2[i][j] += X[i][k] * p[k][j]
                   
                        

    for i in range(len(result2)):
       
       for j in range(len(Y[0])):
           
           for k in range(len(Y)):
               result[i][j] += result2[i][k] * Y[k][j]
         
    return result
# Ejemplo2:         
    def state(X,Y,n):
                
    result =[[0 for x in range(len(Y[0]))] for y in range(len(Y))]
    for h in range(n-1):
        for i in range(len(X)):
           
           for j in range(len(Y[0])):
               
               for k in range(len(Y)):
            
                   
                   result[i][j] += X[i][k] * Y[k][j]
            
        Y=result
     
    return result 



# Autor ✒️
Andres Felipe Cubillos Hurtado


