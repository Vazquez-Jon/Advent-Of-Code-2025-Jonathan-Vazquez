# Jonathan Vazquez


filepath = 'Day 1 Secret Entrance\Input.txt'

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

    if (lock > 100):
        lock = lock % 100
    elif (lock < 0 and lock > -100):
        lock = 100 - abs(lock)
    elif (lock < -100):
        lock = 100 - (abs(lock) % 100)
    
    if (lock == 0 or lock == 100 or lock == -100):
        lock = 0
        resets += 1
    
    return [lock, resets]

def main():
    code = 0
    lock = 50
    with open(filepath, 'r') as file:
        for line in file:
            print(f'code: {code}  lock: {lock}')
            turns = int(line[1:])
            dir   = line[:1]
            lockupdates = updateLock(lock, dir, turns)
            lock = lockupdates[0]
            code += lockupdates[1]
    print(f'code: {code}')

main()