from Sudoku import Sudoku

print("\nWelcome...\n\nGenerating new sudoku board\n")
a = Sudoku()
print(a)
input("Press enter to view solution\n")
solved = a.solve()

print(a) if solved else print("Not solvable")

print("\nThe Backtracking Algorithm is used to generate the solution")

input("\nThanks for play... Press enter to exit")