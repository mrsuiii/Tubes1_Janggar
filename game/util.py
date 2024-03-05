from .models import Position
from .models import GameObject,Board

def clamp(n, smallest, largest):
    return max(smallest, min(n, largest))


def get_direction(current_x, current_y, dest_x, dest_y):
    delta_x = clamp(dest_x - current_x, -1, 1)
    delta_y = clamp(dest_y - current_y, -1, 1)
    if delta_x != 0:
        delta_y = 0
    return (delta_x, delta_y)


def position_equals(a: Position, b: Position):
    return a.x == b.x and a.y == b.y


def closest_diamond(bot : GameObject , board : Board):
    list_diamond  = board.diamonds
    closest = 10000000
    best_dia  =  None
    
    for dia in list_diamond:
        x_len = abs(dia.position.x-bot.position.x)
        y_len = abs(dia.position.x-bot.position.y)
        dist = x_len + y_len
        if best_dia == None:
            closest = dist
            best_dia = dia
        else:
            if closest > dist:
                closest = dist
                best_dia = dia
    #mereturn posisi diamon terdekat dengan bot
    return best_dia.position

