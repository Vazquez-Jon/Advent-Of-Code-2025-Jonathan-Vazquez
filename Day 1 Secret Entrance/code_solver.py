# Jonathan Vazquez


filepath = './Input.txt'

def negOrPosLetter(turnDirection):
    if (turnDirection == "R"):
        return True
    return False

def main():
    print('Hello')

    code = 0
    lock = 50
    with open(filepath, 'r') as file:
        for line in file:
            int(file[1:])
