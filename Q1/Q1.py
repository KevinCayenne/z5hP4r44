"""
手機共通屬性:
price, camera_count, screen_size 特殊功能: special_freature()。
"""

import abc

class Phone(metaclass = abc.ABCMeta):

    def __init__(self, price, camera_count, screen_size):
        self.price = price
        self.camera_count = camera_count
        self.screen_size = screen_size

    @abc.abstractmethod
    def special_feature(self):
        pass

"""
手機一：google phone: 
price=10, camera_count=3, screen_size=5, special_feature 輸入一個 int list, 回傳偶數且大於 10 的元素，並由大至小進行排序。
例如: 輸入 [3, 43, 62, 15, 18, 22] 回傳 [62, 22, 18]。
"""

class google_phone(Phone):
    
    def __init__(self):
        super().__init__(price=10, camera_count=3, screen_size=5)

    def special_feature(self, listattr):
        sorted_listattr = sorted(listattr, reverse=True)
        final_list = []
        for num in sorted_listattr: 
            if num > 10 and num%2==0:
                final_list.append(num)
        return final_list
    
"""
Testing
"""
GooglePhone1 = google_phone()
GooglePhone1.special_feature([3, 43, 62, 15, 18, 22])

"""
手機二：taiwan phone:
price=20, camera_count=1, screen_size=3, special_freature: 
輸入一個數字自動計算Fibonacci斐波那契數列的運算結果，並取最後二位(十位為 x、個位為 y)數字進行 p x 取 y (排序組合) 計算。
"""
from math import factorial

class taiwan_phone(Phone):
    
    def __init__(self):
        super().__init__(price=20, camera_count=1, screen_size=3)
    
    def fibomethod(self, fibonum):
        first = 0
        second = 1
        for i in range(fibonum):
            first += second
            first, second = second, first
        return first
    
    def special_feature(self, num):
        x = self.fibomethod(num)%100//10
        y = self.fibomethod(num)%10
        if x < y:
            return "Warning: invalid value for x < y!"
        else:
            return factorial(x)//factorial(x-y)
            
"""
Testing
"""
T = taiwan_phone()
T.special_feature(14)
