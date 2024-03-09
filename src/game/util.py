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

def red_button_check(bot:GameObject,board : Board):
    number_in_quarter_7= check_quarter_7(bot,board)
    total_dia = total_diamond(board)
    if total_dia//4>number_in_quarter_7:
        return True
    else:
        return False
   
#menghitung total diamond pada board
def total_diamond(board:Board):
    return len(board.diamonds)
#menghitung total diamond pada 7x7 dengan pusat base
def check_quarter_7(bot:GameObject,board:Board):
    curr_pos = bot.position

    left_bound  = max(curr_pos.x-3,0)
    right_bound = min(curr_pos.x-3,14)
    upper_bound = max(curr_pos.y-3,0)
    lower_bound = min(curr_pos.y-3,14)
    count = 0
    for dia in board.diamonds:
        if upper_bound<=dia.position.x<=lower_bound and left_bound<=dia.position.y<=right_bound:
            count+=1
    return count

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
    #mereturn posisi diamond terdekat dengan bot
    return best_dia.position

