import threading
import time


mid = []

def another_function():
    print("This is another function running in a separate thread.")
    while True:
        print(2)
        time.sleep(1)
        print(mid)

if __name__ == "__main__":
    # 创建一个新线程并指定要运行的函数
    thread = threading.Thread(target=another_function)

    # 启动新线程
    thread.start()

    # # 等待新线程完成
    # thread.join()

    print("Main thread continues...")

    while True:
        print(1)
        mid.append(1)
        time.sleep(1)
