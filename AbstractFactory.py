import random 
  
class Course_At_GFG: 
  
    
  
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