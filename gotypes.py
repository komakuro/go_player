# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 09:57:03 2019

碁のプレイヤや座標などパーツを定義する部分！

@author: 鈴木洋平
"""

import enum
from collections import namedtuple

#黒番か白番か
class Player(enum.Enum):
    black = 1
    white = 2
    
    # 相手は？
    # 自身を書き換え不可とするためにproperty宣言？まぁ動いているからいいか。
    @property
    def other(self):
        return Player.black if self == Player.white else Player.white
    
#石を置く場所
class Point(namedtuple('Point','row col')):
    def neighbors(self):
        return [
                Point(self.row - 1, self.col),
                Point(self.row + 1, self.col),
                Point(self.row, self.col + 1),
                Point(self.row, self.col - 1)]

