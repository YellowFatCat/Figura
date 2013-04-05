import math;

class Figure:
    '''
    Базовый класс
    '''
    def perimeter(): # Периметр фигуры (или длина окружности).
        pass;

    def square(): # Площадь фигуры.
        pass;

    def show(self): # Вывод параметров фигуры на экран.
        pass;

class Circle(Figure):
    '''
    Класс, описывающий окружность.
    '''
    def __init__(self, R=0):
        try:
            self.r = float(R);
        except ValueError:
            print("Введено некорректное значение параметра. Для создания объекта будут\nиспользованы параметры по умолчанию.");
            self.r = 0;
        
    def show(self):
        print("Радиус =", self.r);
        
    def perimeter(self):
        return float(2)*math.pi*float(self.r);

class FillCircle(Circle):
    '''
    Класс, описывающий круг.
    '''
    def square(self):
        return math.pi*math.pow(float(self.r), 2);

    def show(self):
        Circle.show(self);

class Rect(Figure):
    '''
    Класс, описывающий прямоугольник.
    '''
    def __init__(self, A=0, B=0):
        try:
            self.a = float(A);
            self.b = float(B);
        except ValueError:
            print("Введены некорректные значения параметров. Для создания объекта будут\nиспользованы параметры по умолчанию.");
            self.a = 0;
            self.b = 0;

    def perimeter(self):
        return 2*self.a + 2*self.b;
    
    def square(self):
        return self.a*self.b;

    def show(self):
        print("Длина =", self.a);
        print("Ширина =", self.b);

def mainMenu(): # Главное меню.
    answ = 0;
    print("Добро пожаловать в программу \"Геометрические фигуры\"!");
    print("Пожалуйста, выберите пункт меню:");
    print("1 - создать окружность;");
    print("2 - создать круг;");
    print("3 - создать прямоугольник;");
    print("4 - выход.");
    while (answ == 0):
        answ = input("Ваш выбор: ");
        try:
            answ = int(answ);
        except ValueError:
            answ = 0;
        if (answ < 1 or answ > 4):
            print("Введено некорректное значение. Пожалуйста, повторите попытку.");
            answ = 0;

    return answ;

a = mainMenu();
if (a == 1):
    a = input("Введите радиус окружности: ");
    f = Circle(a);
    f.show();
    print("Длина окружности =", f.perimeter());
else:
    if (a == 2):
        a = input("Введите радиус круга: ");
        f = FillCircle(a);
        f.show();
        print("Длина окружности =", f.perimeter());
        print("Площадь круга =", f.square());
    else:
        if (a == 3):
            a = input("Введите длину прямоугольника: ");
            b = input("Введите ширину прямоугольника: ");
            f = Rect(a, b);
            f.show();
            print("Периметр прямоугольника =", f.perimeter());
            print("Площадь прямоугольника =", f.square());
    
    
