# Sudoku CLI : Generator and solver

### Sudoku_CLI is a portfolio project in which I:
* Implement the [Backtracking Algorithm](https://en.wikipedia.org/wiki/Backtracking "Wikipedia Article") to solve a Sudoku puzzle.
* Programaticaly create a Sudoku Puzzle.
* Implementation of a [windows .exe](https://github.com/AHardReset/Sudoku-CLI/releases/download/1.0/sudoku_cli.exe "Download file") file for Installling.
No need of python and its dependences. (Exe in dist folder).
<p align="center">
  <img width="300" src="https://upload.wikimedia.org/wikipedia/commons/8/8c/Sudoku_solved_by_bactracking.gif">
</p>

##### Pseudocode
---
*  root(P): return the partial candidate at the root of the search tree.
* reject(P,c): return true only if the partial candidate c is not worth completing.
* accept(P,c): return true if c is a solution of P, and false otherwise.
* first(P,c): generate the first extension of candidate c.
* next(P,s): generate the next alternative extension of a candidate, after the extension s.
* output(P,c): use the solution c of P, as appropriate to the application.

#### Use
[Download](https://github.com/AHardReset/Sudoku-CLI/releases/download/1.0/sudoku_cli.exe "Download file") the installer, execute and go to dist folder to execute **or** clone and use Sudoku methods.

##### Future implementations
---

* Web-app to solve a printed Sudoku (Use of camera).