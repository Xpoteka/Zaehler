import time

def count_up(number):
    if number <= 0:
        print("Invalide Nummer")
        return
    for start in range(1, number + 1):
        time.sleep(0.1)
        print(start)

count_up(10)