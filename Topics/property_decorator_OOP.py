##@property = Decorator used to define a method as a property (it can be accessed like an attribute)
#             Benefit: add additional logic when read, write or delete attribute 
#             Gives you Getter, setter and delete methods 

class Regtengle:
    def __init__(self, width, height):
        self._width = width
        self._height = height 

    @property
    def width (self):
        return f"{self._width:.1f}cm"

    @property
    def height (self):
        return f"{self._height:.1f}cm" 
    
    @width.setter
    def width (self, new_width):
        if new_width > 0 :
            self._width = new_width 
        else:
            print("width must be grater than zero")

    @height.setter
    def height (self, new_height):
        if new_height > 0 :
            self._height = new_height 
        else:
            print("height must be grater than zero")

rectengle = Regtengle(3, 4)

rectengle.width = 7
rectengle.height = 4

print (rectengle.width)
print (rectengle.height)
