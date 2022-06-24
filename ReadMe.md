######Universidad La Salle - Arequipa
#Design Patterns: Abstract Factory
####por: Christian Rodriguez

###INTRODUCCIÓN:
- ####¿Qué es un "Patrón de Diseño"?
Los patrones de diseño (design patterns) son elementos reutilizables creados para resolver problemas comunes. Es decir que con su aplicación y utilización podremos corregir diferentes problemas que presenta nuestro código de una manera segura, estable y testeada por cientos de programadores de todo el mundo.

###Sabiendo esto podemos pasar a hablar sobre: ABSTRACT FACTORY - FÁBRICA ABSTRACTA
######PARA LO CUAL SE HA SEPARADO ESTA EXPLCIACIÓN EN 4 PARTES:
- ####1. ¿Qué es "ABSTRACT FACTORY"?
Perteneciente a los "Patrones Creacionales" (patrones que se utilizan para facilitar la creación de nuevos objetos que buscan incrementar la flexibilidad y reutilización del código existente). Podemos decir que "Abstract Factory" se utiliza para crear familias de objetos que se relacionan sin la necesidad de especificar sus clases.
[![AF](https://refactoring.guru/ "AF")](https://refactoring.guru/images/patterns/content/abstract-factory/abstract-factory-es.png?id=0378c9faca39afa20e41a4d37e7e3828 "AF")
- ####2. Un ejemplo de ABSTRACT FACTORY:
Imagina que quieres unirte a uno de los grupos de élite de GeeksforGeeks . Entonces, irá allí y preguntará sobre los cursos disponibles, su estructura de tarifas, sus horarios y otras cosas importantes. Simplemente mirarán el sistema y le darán toda la información que necesite. ¿Parece simple? Piense en los desarrolladores cómo hacen que el sistema esté tan organizado y cómo su sitio web tiene un aspecto de muy bien parecido.
Los desarrolladores crearán clases únicas para cada curso que contendrán sus propiedades como estructura de tarifas, horarios y otras cosas. Pero ¿cómo los llamarán y cómo instanciarán sus objetos?
Aquí surge el problema, suponga que inicialmente solo hay 3-4 cursos disponibles en GeeksforGeeks , pero luego agregaron 5 nuevos cursos.
Por lo tanto, tenemos que instanciar manualmente sus objetos, lo cual no es bueno según el lado del desarrollador.
[![abstractfactory.png](https://es.acervolima.com/ "abstractfactory.png")](https://media.geeksforgeeks.org/wp-content/uploads/20200117172244/abstractfactory.png "abstractfactory.png")

Solucionando esto sin hacer uso de "Abstract Factory"
class DSA: 
  
    
  
    def price(self): 
        return 11000
  
    def __str__(self): 
        return "DSA"
  
class STL: 
  
    
  
    def price(self): 
        return 8000
  
    def __str__(self): 
        return "STL"
  
class SDE: 
  
    
  
    def price(self): 
        return 15000
  
    def __str__(self): 
        return 'SDE'
  
if __name__ == "__main__": 
  
    sde = SDE()    
    dsa = DSA()    
    stl = STL()    
  
    print(f'Name of the course is {sde} and its price is {sde.price()}') 
    print(f'Name of the course is {dsa} and its price is {dsa.price()}') 
    print(f'Name of the course is {stl} and its price is {stl.price()}') 

- ###Solución utilizando el método Abstract Factory:
Su solución es reemplazar las llamadas directas de construcción de objetos con llamadas al método de fábrica abstracta especial. En realidad, no habrá diferencia en la creación de objetos, pero se llaman dentro del método de fábrica.
Ahora crearemos una clase única cuyo nombre es Course_At_GFG que manejará todas las instancias de objetos automáticamente. Ahora, no tenemos que preocuparnos por la cantidad de cursos que agregaremos después de un tiempo.
[![graphic](https://es.acervolima.com/ "graphic")](https://media.geeksforgeeks.org/wp-content/uploads/20200120114250/solution_abstarct_factory.png "graphic")
####Solución usando patrón abstracto de fábrica:

  
class Course_At_GFG: 
  
    import random 
  
    def __init__(self, courses_factory = None): 
        
  
        self.course_factory = courses_factory 
  
    def show_course(self): 
  
        
  
        course = self.course_factory() 
  
        print(f'We have a course named {course}') 
        print(f'its price is {course.Fee()}') 
  
  
class DSA: 
  
    
  
    def Fee(self): 
        return 11000
  
    def __str__(self): 
        return "DSA"
  
class STL: 
  
    
  
    def Fee(self): 
        return 8000
  
    def __str__(self): 
        return "STL"
  
class SDE: 
  
    
  
    def Fee(self): 
        return 15000
  
    def __str__(self): 
        return 'SDE'
  
def random_course(): 
  
    
  
    return random.choice([SDE, STL, DSA])() 
  
  
if __name__ == "__main__": 
  
    course = Course_At_GFG(random_course) 
  
    for i in range(5): 
        course.show_course() 

- ###3. Diagramas de clases con Abstract Factory:
Veamos el diagrama de clases considerando el ejemplo de Cursos en GeeksforGeeks.
DIAGRAMA A: Estructura de tarifas de todos los cursos disponibles en GeeksforGeeks:
[![graphic2](https://es.acervolima.com/ "graphic2")](https://media.geeksforgeeks.org/wp-content/uploads/20200120120103/class_diagram_abstarct.png "graphic2")
######(Diagrama de clases para patrón de fábrica abstracto)
DIAGRAMA B: Tiempos de todos los cursos disponibles en GeeksforGeeks:
[![graphic3](https://es.acervolima.com/ "graphic3")](https://media.geeksforgeeks.org/wp-content/uploads/20200120120403/class_2_diagram.png "graphic3")
######(Diagrama de clases 2 patrón de método abstract)
- ###4. VENTAJAS y DESVENTAJAS de usar Abstract Factory:
######VENTAJAS:
- Este patrón es particularmente útil cuando el cliente no sabe exactamente qué tipo crear.
- Es fácil introducir las nuevas variantes de los productos sin romper el código de cliente existente.
- Los productos que obtenemos de fábrica seguramente son compatibles entre sí.
######DESVENTAJAS:
- Nuestro código simple puede complicarse debido a la existencia de muchas clases.
- Terminamos con una gran cantidad de archivos pequeños, es decir, desorden de archivos.

###EXTRA: Aplicabilidad
Utiliza el patrón Abstract Factory cuando tu código deba funcionar con varias familias de productos relacionados, pero no desees que dependa de las clases concretas de esos productos, ya que puede ser que no los conozcas de antemano o sencillamente quieras permitir una futura extensibilidad.
[![pseudocode](https://refactoring.guru/ "pseudocode")](https://refactoring.guru/es/design-patterns/abstract-factory "pseudocode")

#####Bibliografía:

- https://refactoring.guru/es/design-patterns/abstract-factory

- https://refactoring.guru/es/design-patterns/abstract-factory/python/example#example-0--main-py

- https://es.acervolima.com/metodo-de-fabrica-abstracta-patrones-de-diseno-de-python/

- https://www.geeksforgeeks.org/abstract-factory-pattern/#:~:text=Abstract%20Factory%20provides%20interfaces%20for,of%20the%20family%20of%20objects.

- https://en.wikipedia.org/wiki/Abstract_factory_pattern

######Eso es todo, gracias por tomarte el tiempo de leer :D
