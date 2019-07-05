# ORDERLY Python / Django Interview

Hi,

感謝您

這是根據您的回覆所訂製的問題，大約會花費 3- 5 小時的挑戰時間

若您決定要開始這項挑戰，請 fork 此專案，並將每個問題的答案放至對應的資料夾

完成後，請發個PR到此專案

### 挑戰一: OO觀念運用 (folder: x_1)

> 現在您的手上有 3 支手機，手機來自不同品牌，其規格屬性大同小異，但各自擁有一項特殊功能，請使用OO繼承及如下的規格，設計出這三支手機的class。

```
手機共通屬性: price, camera_count, screen_size
特殊功能: special_freature() 

手機一 google phone:
price=10, camera_count=3, screen_size=5
special_freature 輸入一個int list, 回傳偶數且大於10的元素，並由大至小進行排序
例如: 輸入 [3, 43, 62, 15, 18, 22] 回傳 [62, 22, 18]

手機二 taiwan phone:
price=20, camera_count=1, screen_size=3
special_freature
輸入一個數字自動計算Fibonacci斐波那契數列的運算結果，並取最後二位(十位為 x、個位為 y)數字進行 p x 取 y (排序組合) 計算。
例如: ---

```


### 挑戰二: pip 及 Django 實作  (folder: x_3)

> 請參考 https://github.com/twtrubiks/django-tutorial 的教學，將您的Django 運行起來，並進行以下步驟:

1) 使用 pip 將你安裝的所有 python 模組及其版本變成一個 requirement 檔案
2) 將 Django 後台路徑從 /admin 修改成 /superadmin 
3) 新增一個 django app "ilovecoffee", 並於settings.py啟用它
4) 在 ilovecoffee 中，新增 models.py 檔 ，並創建一個 Coffee class, 不需要任何屬性和功能 (請注意這不代表class code裡面沒東西)
5) 在當前的虛擬環境中使用 python manage.py shell，並將 Coffee import 進來，將結果截圖放至此資料夾，取名為 coffee.jpg


### 挑戰三: 檔案與資料操作 (folder: x_3)
> 請設計一個 CsvHanlder class，當它被初始化時，會偵測相同目錄下是否存在一個 ilovecoffee 資料夾，若無則建立，有則略過。賦予此 class 一個 create_csv() method, 當被呼叫時，會隨機寫入 500 筆客戶資料至 /ilovecoffee/customers.csv，結構如下:
```
customer_id,customer_name, customer_mobile, frequency
"y88xTa", "tom.y88xTa","+886938766119", "4"
"uYt49x", "peter.uYt49x","+886938922440", "6"
"p9g5As", "hank.p9g5As","+886918300227", "1"
.....
````

##### customer_id:
長度8, 由數字[0-9], 大寫[A-Z]，小寫[a-z]隨機組成，但開頭不可為數字

##### customer_name: 
隨意用10個英文名字建立一組list: 如 ['tom','peter','hank'....]
將customer_id與隨機從 name list 中取出的一個元素進行合併，例如產出"tom.y88xTa"

##### customer_mobile
隨機產生一個+886開頭的台灣電話號碼，若新產出的電話號碼有重複，則需要重新產生

##### frequency
從 [0-20] 中隨機進行選擇

>
> 賦予此 class 一個 calculate_csv() method, 當被呼叫時，會讀取 /ilovecoffee/customers.csv，並列印出frequency 的中數、眾數及平均數 (取至小數點後 5 位)
>


## 當您挑戰結束時，請在您的最後一次 commit 中輸入您對此份工作，在程式上的期待，謝謝您。

