def gridChallenge(grid):
    if not grid:
        return 'NO'

    grid = [sorted(list(item)) for item in grid]
    gridt = [[grid[i][j] for i in range(len(grid))] for j in range(len(grid[0]))]
    
    result = all(gridt[i] == sorted(gridt[i]) for i in range(len(gridt)))
    return 'YES' if result else 'NO'
