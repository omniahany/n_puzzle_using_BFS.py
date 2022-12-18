from Search_Algorithms import Best_First_search
goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]

#initial state
n = int(input("Enter n\n"))
print("Enter your" ,n,"*",n, "puzzle")
root = []
for i in range(0,n*n):
    p = int(input())
    root.append(p)

print("The given state is:", root)
counter = 0;
for i in range(n*n):
        if (root[i] != goal[i]):
            counter += 1


#count the number of inversions       
def inv_num(puzzle):
    inv = 0
    for i in range(len(puzzle)-1):
        for j in range(i+1 , len(puzzle)):
            if (( puzzle[i] > puzzle[j]) and puzzle[i] and puzzle[j]):
                inv += 1
    return inv

def solvable(puzzle): #check if initial state puzzle is solvable: number of inversions should be even.
    inv_counter = inv_num(puzzle)
    if (inv_counter %2 ==0):
        return True
    return False

from time import time

if solvable(root):
    print("Solvable, please wait. \n")

    
    time4 = time()
    Best_First_search_solution =  Best_First_search(root, n)
    Best_First_search_time = time() - time4
    print('best first search  Solution is ', Best_First_search_solution[0])
    print('Number of explored nodes is ', Best_First_search_solution[1])
    print('best first search Time:', Best_First_search_time)
    print('number of misplaced tiles  ', counter)
    
    
else:
    print("Not solvable")



     
