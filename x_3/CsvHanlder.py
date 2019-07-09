import os
import pandas as pd
from scipy import stats
from random import sample, choice, choices
from string import ascii_letters, digits

""" file path setting """
PATH = "ilovecoffee"

""" Name setting """
NAME_LIST = ['tom', 'peter', 'hank', 'vivian', 'kevin', 
             'mark', 'ting', 'clara', 'mark', 'rex']

""" number of data """
CUSTOMER_NUM = 500 

class CsvHanlder(object):
    
    """ 初始化時，會偵測相同目錄下是否存在一個 ilovecoffee 資料夾，若無則建立，有則略過 """
    def __init__(self):
        if not os.path.isdir(PATH):
            os.mkdir(PATH)      
               
    def create_id_name(self):
        """ 長度8, 由數字[0-9], 大寫[A-Z]，小寫[a-z]隨機組成，但開頭不可為數字 """
        sample_id = ''.join([choice(ascii_letters)] + choices(ascii_letters + digits, k = 8))
        
        """
        隨意用10個英文名字建立一組list: 如 ['tom','peter','hank'....] 
        將customer_id與隨機從 name list 中取出的一個元素進行合併，例如產出"tom.y88xTa"
        """
        sample_name = ''.join(sample(NAME_LIST, 1) + ["."] + [sample_id])
        
        return [sample_id, sample_name]
    
    """ 隨機產生一個+886開頭的台灣電話號碼 """    
    def create_phonenum(self):

        return [''.join(["+8869"] + choices(digits, k = 8))]
    
    """ 從 [0-20] 中隨機進行選擇 """
    def create_freq(self):
        return [str(choice(range(20)))]
        
    """ combine customer data """
    def create_customer(self):
        sample_customer = self.create_id_name() + self.create_phonenum() + self.create_freq()
        return sample_customer
    
    """
    create_csv() 隨機寫入 500 筆客戶資料至 /ilovecoffee/customers.csv
    """
    def create_csv(self):
        customer_arr = []
        for i in range(CUSTOMER_NUM): 
            customer_arr = customer_arr + [self.create_customer()]
        
        customer_df = pd.DataFrame(customer_arr, columns = ["customer_id", 
                                                            "customer_name", 
                                                            "customer_mobile", 
                                                            "frequency"])
        
        """ 若新產出的電話號碼有重複，則需要重新產生 """
        dup_df = customer_df[customer_df.duplicated("customer_mobile")]
         
        while len(dup_df) != 0:
            self.create_csv()
        
        customer_df.to_csv("ilovecoffee/customers.csv", index = 0)    
    
    """ 讀取 /ilovecoffee/customers.csv，並列印出frequency 的中數、眾數及平均數 (取至小數點後 5 位) """
    def  calculate_csv(self):
        try:
            customer_df = pd.read_csv("ilovecoffee/customers.csv")
        except:
            print("The file 'customers.csv' does not exist.")
        
        Freq = pd.Series(data = customer_df["frequency"])
        print("Frequency: median: %.1f, mode: %x, mean: %.5f" %(Freq.median(), stats.mode(Freq).mode[0], Freq.mean()))
        
                     
"""
Testing
"""
                                           
TryCsv = CsvHanlder()
TryCsv.create_csv()
TryCsv.calculate_csv()
