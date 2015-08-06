def print_menu():
    print('1.Quit')
    print('2.MOVE LEFT')
    print('3.MOVE RIGHT')
    print('4.MOVE UP')
    print('5.MOVE DOWN\n')
    
    # define a function to find an item in the 2s list
def find(l, elem):
    for row, i in enumerate(l):
        try:
            column = i.index(elem)
        except ValueError:
            continue
        return row, column
    return -1    
    
def new_print(myList):
    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
      for row in myList]))
    
    
puzzle =   [
    
           [' 1', '2' , '3' , '4'],
    
           [ '5', '6' , '7' , '8'],
    
           [ '9', '10' ,'11','12'],
    
           [ '13', '14', '15', 'X']
      
           ]
           
    
quit = False
item = 'X'
while not quit:
    print_menu()
    new_print(puzzle)
    command = int(input("\nEnter command: "))
    
    if command == 1:
        print('Come back to play again!')
        quit = True
        
    elif command ==2:
        #find the X in the list first
        row,column = find(puzzle,item)
        puzzle[row].pop(column)
        puzzle[row].insert(column-1,item)
    elif command ==3:
        #find the X in the list first
        row,column = find(puzzle,item)
        puzzle[row].pop(column)
        puzzle[row].insert(column+1,item)
    elif command ==4:
        #find the X in the list first
        row,column = find(puzzle,item)
        puzzle[row].pop(column)
        new_item = puzzle[row-1][column]
        puzzle[row-1].pop(column)
        puzzle[row-1].insert(column,item)
        puzzle[row].insert(column,new_item)
    elif command ==5:
        #find the X in the list first
        row,column = find(puzzle,item)
        if(row<=2):
            puzzle[row].pop(column)
            new_item = puzzle[row+1][column]
            puzzle[row+1].pop(column)
            puzzle[row+1].insert(column,item)
            puzzle[row].insert(column,new_item)
        elif(row==3):
            puzzle[row].pop(column)
            new_item = puzzle[0][column]
            puzzle[0].pop(column)
            puzzle[0].insert(column,item)
            puzzle[row].insert(column,new_item)
        
