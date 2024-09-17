import time

while True:
    with open('templates/index.html', 'r') as file:
        print(file.read())
    print("---")
    time.sleep(5)