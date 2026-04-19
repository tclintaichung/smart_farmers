import time

for i in range(10):   # 執行 10 次
    # 取得目前時間
    t = time.localtime()
    
    # 格式化輸出
    print(time.strftime("%Y-%m-%d %H:%M:%S", t))
    
    # 暫停 1 秒
    time.sleep(1)
