from collections import deque

name = input()
name_queue = deque()
while name != "End":

    if name == "Paid":
        while name_queue:
            print(name_queue.popleft())
    else:
        name_queue.append(name)
    name = input()

print(f'{len(name_queue)} people remaining.')
