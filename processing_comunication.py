import multiprocessing
import time

def another_function(mid):
    print("This is another function running in a separate process.")
    while True:
        print(2)
        time.sleep(1)
        print(mid)

if __name__ == "__main__":
    with multiprocessing.Manager() as manager:
        mid = manager.list()
        process = multiprocessing.Process(target=another_function, args=(mid,))
        process.start()

        print("Main process continues...")

        while True:
            print(1)
            mid.append(1)
            time.sleep(1)
