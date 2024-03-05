from game.logic.random import RandomLogic
from typing import Optional
from game.api import Api
from game.logic.base import BaseLogic
from game.models import GameObject, Board, Position
from ..util import get_direction
from game.board_handler import BoardHandler
from game.bot_handler import BotHandler
class NearestLogic(BaseLogic):
    
    def __init__(self):
        self.directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        self.goal_position: Optional[Position] = None
        self.current_direction = 0
        self.next_pos = None
    def next_move(self,board_bot : GameObject, board:Board):
        if self.next_pos:
            current_position = board_bot["position"]
            self.goal_position = {"x":current_position["x"]+self.next_pos[0],"y":current_position["x"]+self.next_pos[1]}
            self.next_pos  = None        
        elif board_bot.properties.diamonds == 5:
            base  = board_bot["base"]
            self.goal_position = base
        else:
            me = board_bot["position"]
            nearest_dist = None
            best_dia = None
            for dia in board.diamonds:
                x_len = abs(me["x"]-dia["y"])
                y_len = abs(me["y"]-dia["y"])
                if best_dia == None:
                    dist = x_len + y_len
                    best_dia = dia
                else :
                    if dist<nearest_dist:
                        nearest_dist = dist
                        best_dia = dia
            
            self.goal_position = best_dia

        if self.goal_position:
            current_position = board_bot["position"]
            delta_x1,delta_y1 = get_direction(current_position["x"],current_position["y"],self.goal_position["x"],self.goal_position["y"])
            going_to = {"x":current_position["x"]+delta_x1, "y":current_position["y"]+delta_y1}
            list_of_bot = board.bots
            delta_x,delta_y = 0,0
            for bot in list_of_bot:
                while(going_to == bot["position"]or going_to["x"]<0 or going_to["y"]<0):
                    temp = board.bots
                    print("=======temp=======")
                    print(temp)
                    print("=======temp=======")
                    delta_x,delta_y  = RandomLogic.next_move(board_bot,board)
                    going_to = {"x":current_position["x"]+delta_x,"y":current_position["y"]+delta_y}
            
            return delta_x,delta_y
        


        return 0,0