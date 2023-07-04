class Pencil:
    def __init__(self, color):
        self.color = color
    
    def draw(self, color):
        print(f'Нарисован рисунок цветом {color}')
    
class Pen(Pencil):
    def __init__(self, color):
        super().__init__(color)
    
    def draw(self, color):
        super().draw(color)
    
    def sign(self, color):
        if self.color == 'красный':
            print(f'Ручкой цвета {color} нельзя подписать документ')
        elif self.color == 'синий' or self.color == 'чёрный' or self.color == 'фиолетовый':
            print(f'Подписан документ')

BluePen = Pen('синий')
BluePen.sign('фиолтовый')


