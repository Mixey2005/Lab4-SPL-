#Task 1
class String:
    def __init__(self, text):
        self.text = text
    def length(self):
        return len(self.text)
    def lowercase(self):
        return self.text.lower()
    def uppercase(self):
        return self.text.upper()
    def reverse(self):
        return self.text[::-1]
    def count_words(self):
        words = self.text.split()
        return len(words)
#Task 2
class Alphabet:
    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = letters
    def print(self):
        print("Alphabet:", self.letters)
    def letters_num(self):
        return len(self.letters)

class EngAlphabet(Alphabet):
    __letters_num = 26
    def __init__(self):
        super().__init__('En', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    def is_en_letter(self, letter):
        return letter.upper() in self.letters
    def letters_num(self):
        return self.__letters_num
    @staticmethod
    def example():
        return "Какая-то строка"

#Task 3
class Stationery:
    def __init__(self, title):
        self.title = title
    def draw(self):
        print("Запуск отрисовки")
class Pen(Stationery):
    def __init__(self):
        super().__init__("Ручка");
    def draw(self):
        print("Рисование ручки")
class Pencil(Stationery):
    def __init__(self):
        super().__init__("Карандаш")
    def draw(self):
        print("Рисование карандаша")
class Handle(Stationery):
    def __init__(self):
        super().__init__("Маркер")
    def draw(self):
        print("Рисование маркера")

pen = Pen()
pen.draw()
pencil = Pencil()
pencil.draw()
handle = Handle()
handle.draw()

#Task 4
class Figure():
    def __init__(self,figure,length,width):
        self.figure = figure
        self.length = length
        self.width = width
    def Perimetr(self,a,b):
        return "Периметр фигуры равен", a+b
class Square(Figure):
    def __init__(self):
        super().__init__("квадрата",4,6)
    def Perimetr(self,a,b):
        print("Периметр",self.figure ,"равен",(a+b)*2)
class Triangle(Figure):
    def __init__(self,threesline):
        super().__init__("треугольника",3,76)
        self.threesline = threesline
    def Perimetr(self,a,b,threesline):
        print("Периметр",self.figure,"равен",(a+b+threesline))
square = Square()
square.Perimetr(3,5)
