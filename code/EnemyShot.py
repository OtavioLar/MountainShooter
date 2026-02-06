from code.Const import ENTITY_SPEED
from code.Entity import Entity


class EnemyShot(Entity):

    def __init__(self, name: str, position: tuple):
        # desloca o tiro um pouco para frente (esquerda)
        x = position[0] - 51   # quanto maior, mais à frente
        y = position[1]

        super().__init__(name, (x, y))

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]
