class Rectangle:
    def __init__(self, x, y):
        if x <= 0 or y <= 0:
            raise ValueError("Ұзындығы мен ені оң сан болуы керек.")
        self.x = x
        self.y = y

    def calculate_area(self):
        area = self.x * self.y
        return area

    def calculate_perimeter(self):
        perimeter = 2 * (self.x + self.y)
        return perimeter
try:
    my_x = float(input("Ұзындығын енгізіңіз: "))
    my_y = float(input("Енін енгізіңіз: "))
    my_rectangle = Rectangle(my_x, my_y)
          
    area = my_rectangle.calculate_area()
    print(f"Тіктөртбұрыштың ауданы: {area}")  

    perimeter = my_rectangle.calculate_perimeter()
    print(f"Тіктөртбұрыштың периметрі: {perimeter}")  

except ValueError as e:
    print(f"Қате: {e}")