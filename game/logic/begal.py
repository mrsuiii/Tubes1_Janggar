from game.logic.random import RandomLogic
from typing import Optional, Tuple
from game.api import Api
from game.logic.base import BaseLogic
from game.models import GameObject, Board, Position,Properties,Base
from ..util import get_direction


#strategi begal yang kerjaannya begal bot lawan
class Begal(BaseLogic):
    def __init__(self):
        self.goal_position: None
        self.current_dirrection = 0
        self.halang =[]

    def next_move(self, board_bot: GameObject, board: Board) -> Tuple[int, int]:
        if board_bot.properties.diamonds >=4:
            
            return get_direction(board_bot.position.x,board_bot.position.y,board_bot.properties.base.x,board_bot.properties.base.y)
        current_position = board_bot.position
        # menghindari tabrakan, tombol, dan tp
        teleporter=[]
        for barang in board.game_objects:
            if  barang.type == "BotGameObject" and (barang.position != current_position):
                self.halang.append((barang.position.x+1,barang.position.y))
                self.halang.append((barang.position.x,barang.position.y+1))
                self.halang.append((barang.position.x-1,barang.position.y))
                self.halang.append((barang.position.x,barang.position.y-1))
            if barang.type == "DiamondButtonGameObject":
                self.halang.append((barang.position.x, barang.position.y))
                diabutton=barang.position
            if barang.type == "TeleportGameObject":
                print(barang)
                self.halang.append((barang.position.x, barang.position.y))
                teleporter.append((barang.position))

        list_base = []
        list_bot = {}
        item = board.game_objects
        my_time_left = board_bot.properties.milliseconds_left
        for i in item:
            if i.type == "BotGameObject" and i.properties.name != board_bot.properties.name:
                list_bot[i.properties.name] = i.properties.milliseconds_left
            if i.type == "BaseGameObject" and i.properties.name!=board_bot.properties.name:
                list_base.append(i)
        nearest = 1000000
        nearest_base = None
        if(len(list_base)==0):
            return 1,0
        if(list_base):
            for base in list_base:
                dx = abs(base.position.x - board_bot.position.x)
                dy = abs(base.position.y - board_bot.position.y)
                dist = dx+dy
                dist1 = abs(base.position.x-board_bot.properties.base.x)+abs(base.position.y-board_bot.properties.base.y)
                if(nearest_base == None):
                        nearest = dist
                        nearest_base = base
                else:
                    if(dist<nearest and list_bot[base.properties.name]%1000<my_time_left%1000 and dist1 %2 ==0):
                        nearest = dist
                        nearest_base = base
                    elif(dist<nearest and list_bot[base.properties.name]%1000>my_time_left%1000 and dist1 %2 ==1):
                        nearest = dist
                        nearest_base = base
            print(nearest_base)
            if nearest == 0:  #sudah berada di base musuh terdekat
                #calculate distance between me and other bot 

                dx,dy = self.calculate_distbot(board_bot,nearest_base.properties,board)
                
                x,y=   get_direction(board_bot.position.x,board_bot.position.y,dx,dy)
                
                return x,y
            else:
                 x,y=   get_direction(board_bot.position.x,board_bot.position.y,nearest_base.position.x,nearest_base.position.y)
                 return x,y
                
            
        return 0,0
    def calculate_distbot(self,board_bot : GameObject,props: Properties,board : Board):
        
        for bot in board.game_objects:
            if bot.type =="BotGameObject" and bot.properties.name == props.name:
                
                return  bot.position.x,bot.position.y

    def selamatsampaitujuan(self, curpos, target):
        dx = target.x - curpos.x
        dy = target.y - curpos.y
        adx = abs(dx)
        ady = abs(target.y - curpos.y)
        # handling bug
        if(dx == 0 and dy == 0):
            if(curpos.x+1<15):
                return 1,0
            else: return -1,0
        if ((adx+ady)==1):
            return dx,dy
        else:
            if(adx>ady):
                # tidak terhalang
                if (curpos.x+(dx/adx),curpos.y) not in self.halang:
                    return (dx/adx),0
                # terhalang
                if(ady != 0):
                    return 0,(dy/ady)
                else:
                    # tidak di tepi
                    if(curpos.y-1 >= 0 and curpos.y+1 < 15):
                        if(curpos.x,curpos.y-1) not in self.halang:
                            return 0,-1
                        else:
                            return 0, 1
                    # di tepi
                    else:
                        if(curpos.y-1 >= 0):
                            return 0,-1
                        else:
                            return 0,1
            # tidak terhalang
            if (curpos.x,curpos.y+(dy/ady)) not in self.halang:
                return 0,(dy/ady)
            # terhalang
            if(adx != 0):
                return (dx/adx),0
            else:
                # tidak di tepi
                if(curpos.x-1>=0 and curpos.x+1<15):
                    if(curpos.x-1,curpos.y) not in self.halang:
                        return -1,0
                    else:
                        return 1,0
                # di tepi
                else:
                    if(curpos.y-1>=0):
                        return -1,0
                    else:
                        return 1,0

    #menentukan apakah perlu teleport
    def determinetargetndistance(self,position,teleporter,target):
        t1x = teleporter[0].x
        t1y = teleporter[0].y
        t2x = teleporter[1].x
        t2y = teleporter[1].y
        p1 = abs(position.x-target.x)+abs(position.y-target.y)
        p2 = abs(position.x-t1x)+abs(position.y-t1y)+abs(target.x-t1x)+abs(target.y-t2y)
        p3 = abs(position.x-t2x)+abs(position.y-t2y)+abs(target.x-t1x)+abs(target.x-t1y)
        if(p1<p2 and p1<p3): return target,p1 #ga tele
        if(p2<p1 and p2<p3): return teleporter[0],p2 #lewat teleporter 1
        return teleporter[1],p3 #lewat teleporter 2
                
