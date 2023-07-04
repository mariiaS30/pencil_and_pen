class Pencil:
    def __init__(self, color):
        self.color = color
    
    def draw(self):
        print(f'Нарисован рисунок цветом {self.color}')
    
class Pen(Pencil):
    def __init__(self, color):
        super().__init__(color)
    
    def draw(self):
        super().draw()
    
    def sign(self):
        if self.color == 'синий' or self.color == 'чёрный' or self.color == 'фиолетовый':
            print(f'Подписан документ')
        else:
            print(f'Ручкой цвета {self.color} нельзя подписать документ')


BluePen = Pen('синий')
BluePen.sign()
RedPen = Pen('красный')
RedPen.sign()
PinkPen = Pen('розовый')
PinkPen.sign()
PinkPen.draw()
BlackPencil = Pencil('черный')
BlackPencil.draw()