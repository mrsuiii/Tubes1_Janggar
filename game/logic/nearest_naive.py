from game.logic.random import RandomLogic
from typing import Optional
from game.api import Api
from game.logic.base import BaseLogic
from game.models import GameObject, Board, Position
from ..util import get_direction
from game.board_handler import BoardHandler
from game.bot_handler import BotHandler


#strategy yang sangat naive mencari diamond terdekat
class NearestLogic(BaseLogic):

    def __init__(self):
        self.directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        self.goal_position: Optional[Position] = None
        self.current_direction = 0
    def next_move(self,board_bot : GameObject, board:Board):
        props = board_bot.properties
        base = props.base
        if board_bot.properties.diamonds >= 4:
            #jika diamond >=4 maka akan balik
            base  = props.base
            self.goal_position = base
        else:
            me = board_bot.position
            nearest_dist =100000
            best_dia = None
            for dia in board.diamonds:
                x_len = abs(base.x-dia.position.x)
                y_len = abs(base.x-dia.position.y)
                dist = x_len + y_len
                if best_dia == None:
                    best_dia = dia
                    nearest_dist = dist
                else :
                    if dist<nearest_dist:
                        nearest_dist = dist
                        best_dia = dia
            
            self.goal_position = best_dia.position
            print("---temp diamond---")
            print(best_dia)
            print("---best_dia---")
        if self.goal_position:
            current_position = board_bot.position
            delta_x1,delta_y1 = get_direction(current_position.x,current_position.y,self.goal_position.x,self.goal_position.y)
            return delta_x1,delta_y1
        # base casae if move invalid
        return 0,0