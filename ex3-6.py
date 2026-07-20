from datetime import datetime
import time

for i in range(10):   # 執行 10 次
    # 取得目前時間
    now = datetime.now()
    
    # 格式化輸出
    print(now.strftime("%Y-%m-%d %H:%M:%S"))
    print(str(time.localtime().tm_min) + " min " + str(time.localtime().tm_sec) + " sec")
    # 暫停 1 秒
    time.sleep(1)
