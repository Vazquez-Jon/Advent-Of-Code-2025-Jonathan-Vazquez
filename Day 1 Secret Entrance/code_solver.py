# Jonathan Vazquez


filepath = './Input.txt'

def posLetter(turnDirection: str) -> bool:
    if (turnDirection == "R"):
        return True
    return False

def updateLock(lock: int, dir: str, turns: int) -> int:
    resets = 0
    if (dir == "R") :
        lock += turns 
    else:
        lock -= turns

    if (lock > 99):
        lock = lock % 100
        resets += 1
    elif (lock < 0):
        lock = abs(lock)
    elif (lock < -99):
        lock = 100 - (abs(lock) - 100)
        resets += 1 
    
    return [lock, resets]

def main():
    print('Hello')

    code = 0
    lock = 50
    with open(filepath, 'r') as file:
        for line in file:
            turns = int(line[1:])
            dir   = line[:1]
