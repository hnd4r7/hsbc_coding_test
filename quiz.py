def reverse_list(l:list):

    """

    TODO: Reverse a list without using any built in functions

 

    The function should return a sorted list.

    Input l is a list which can contain any type of data.

    """
    
    left, right =0, len(l)-1
    while left < right:
        l[left], l[right] = l[right], l[left]
        left+=1
        right-=1
    #It doesn't make sense to return a sorted list after we reverse it!
    return l

assert reverse_list([1,23,4]) == [4,23,1]
 

def solve_sudoku(matrix):

    """

    TODO: Write a programme to solve 9x9 Sudoku board.

 

    Sudoku is one of the most popular puzzle games of all time. The goal of Sudoku is to fill a 9×9 grid with numbers so that each row, column and 3×3 section contain all of the digits between 1 and 9. As a logic puzzle, Sudoku is also an excellent brain game.

 

    The input matrix is a 9x9 matrix. You need to write a program to solve it.

    """

    pass