class Pencil:
    def __init__(self, color):
        self.color = color
    
    def draw(self):
        print(f'Нарисован рисунок цветом {self.color}')
    
class Pen(Pencil):
    def __init__(self, color, pen_type):
        super().__init__(color)
        self.pen_type = pen_type
    
    def draw(self):
        super().draw()
    
    def sign(self):
        if (self.color == 'синий' or self.color == 'чёрный' or self.color == 'фиолетовый') and self.pen_type != 'гелевая':
            print(f'Подписан документ')
        elif self.pen_type == 'гелевая':
            print(f'Ручкой типа {self.pen_type} нельзя подпиать')
        else:
            print(f'Ручкой цвета {self.color} нельзя подписать документ')


# RedPen = Pen('красный', 'гелевая')
# RedPen.sign()
# PinkPen = Pen('розовый', 'шариковая')
# PinkPen.sign()
# PinkPen.draw()
# BlackPencil = Pencil('черный')
# BlackPencil.draw()
# BluePencil = Pencil('синий')
# BluePencil.draw()
BluePen = Pen('синий', 'гелевая')
BluePen.sign()
