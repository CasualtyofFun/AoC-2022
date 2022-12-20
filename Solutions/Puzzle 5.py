import math

inputfile = open("Puzzle 5.txt", 'r')
fullinput = inputfile.read()
print("This is your starting puzzle:\n", fullinput, '\n')

fullinput = fullinput.split('\n')
print("This is your puzzle after you split it:\n", fullinput, '\n')

column1 = []
column2 = []
column3 = []
column4 = []
column5 = []
column6 = []
column7 = []
column8 = []
column9 = []

board = [column1, column2, column3, column4, column5, column6, column7, column8, column9]
workingRow = 0
numberOfRows = 7

while numberOfRows >= 0:

    row = fullinput[numberOfRows]

    if "1" in row:
        break

    print("\nThis is row", workingRow, ":", row)

    """
    boxes = row.split(" ")
    print("\nThe boxes in this row are:", boxes)
    """


    counter = 0
    start = 1

    while counter < 9:
        box = row[start]
        if " " in box:
            print("I didn't append anything for I was empty")
            start = start + 4
            counter = counter + 1
            continue
        board[counter].append(box)
        print("I appended", box, "To column", counter+1)
        start = start + 4
        counter = counter + 1

    print('The resulting board is:', board, '\n')
    numberOfRows = numberOfRows - 1
    workingRow = workingRow + 1

print("We have hopefully successfully generated the board! Now we need to read the movement instructions\n")
workingRow = workingRow + 2

instructions = fullinput[workingRow:]
print("Here's our list of instructions: \n", instructions, "\n")

for instruction in instructions:
    print("Incoming Movement Instruction: \n", instruction, "\n")
    instruction = instruction.split(' ')
    print("Let's make that machine readable: \n", instruction, "\n")


    numberOfBoxes = int(instruction[1])
    print(numberOfBoxes)
    startColumn = int(instruction[3])-1
    endColumn = int(instruction[5])-1
    load = []
    for y in range(0, numberOfBoxes):
        load.append(board[startColumn].pop())
    for z in range(0,len(load)):
        board[endColumn].append(load.pop())

print("All instructions executed! The resulting board is:", board)

print("Drumroll Please \n")
answer = ""
for column in board:
   answer = answer + column.pop()

print("Your answer is:\n", answer)