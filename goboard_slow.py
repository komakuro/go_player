# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 09:57:02 2019

碁の進行に関わる部分

@author: 鈴木洋平
"""

import copy
from gotypes import Player

#プレイヤの行動を定義
class Move():
    def __init__(self, point=None, is_pass=False, is_resign=False):
        #プレイヤが選択できるのは、石を置く、パス、投了
        #石を置く場合はpointに何か格納されているはず
        #上記三選択肢で排他的論理和をとりどれか一つだけtrueになっていることを確認する
        #※パスかつ投了とかはありえないから
        assert ( point is not None ) ^ is_pass ^ is_resign
        self.point = point
        self.is_play = (self.point is not None)
        self.is_pass = is_pass
        self.is_resign = is_resign
        
    #インスタンス生成を求めるメソッドのためclassmethodとして定義するよーだ（pass_turn,resignも同様)
    @classmethod
    def play(cls, point):
        return Move(point=point)
    
    @classmethod
    def pass_turn(cls):
        return Move(is_pass=True)
    
    @classmethod
    def resign(cls):
        return Move(is_resign=True)

#連（隣接した同色の石が連なっていること）を定義
class GoString():
    def __init__(self, color, stones, liberties):
        #手番
        self.color = color
        #連に参加する石の集合
        self.stones = set(stones)
        #呼吸点の集合
        self.liberties = set(liberties)
    
    def remove_liberty(self, point):
        self.liberties.remove(point)
    
    def add_liberty(self, point):
        self.liberties.add(point)
    
    #連同士がつながった際の処理
    def merged_with(self, go_string):
        assert go_string.color == self.color
        #連に参加する石の和集合をとる
        combined_stones = self.stones | go_string.stones
        #呼吸点はそれぞれの集合の和集合のうち、石が置かれていないものとなるため下記の記述となる
        return GoString(self.color, combined_stones, (self.liberties | go_string.liberties) - combined_stones)
    
    #呼吸点の数
    @property
    def num_liberties(self):
        return len(self.liberties)
    
    #連が一致するとはどういうことか
    def __eq__(self, other):
        return isinstance(other, GoString) \
            and self.color == other.color \
            and self.stones == other.stones \
            and self.liberties == other.liberties \
    
#盤    
class Board():
    def __init__(self, num_rows, num_cols):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self._grid = {}
        
    def place_stone(self, player, point):
        assert self.is_on_grid(point)
        assert self._grid.get(point) is None
        adjacent_same_color = []
        adjacent_opposite_color = []
        liberties = []
        
        for neighbor in point.neighbors():
            if not self.is_on_grid(neighbor):
                continue
            neighbor_string = self._grind.get(neighbor)
            if neighbor_string is None:
                liberties.append(neighbor)
            elif neighbor_string.color == player:
                if neighbor_string not in adjacent_same_color:
                    adjacent_same_color.append(neighbor_string)
                else:
                    if neighbor_string not in adjacent_opposite_color:
                        adjacent_opposite_color.append(neighbor_string)
            new_string = GoString(player, [point], liberties)
            
    def is_on_grid(self, point):
        return 1 <= point.row <= self.num_rows
    
    
        
        
        
        
    
        