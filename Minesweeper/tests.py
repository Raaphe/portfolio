from remise import *
#from tp_corrige import *

def count_mines(grid):
    count = 0
    for row in grid:
        for cell in row:
            if cell == 'X':
                count += 1
            elif cell != '-':
                return -1
    return count

def tests():
    grid = [['1', '-', 'X'], 
            ['X', '-', '-'],
            ['M', 'W', ' ']]
    assert not has_mine(grid, 0, 0)
    assert not has_mine(grid, 0, 1)
    assert has_mine(grid, 1, 0)
    assert has_mine(grid, 2, 0)
    assert has_mine(grid, 0, 2)
    assert not has_mine(grid, 2, 1)
    assert not has_mine(grid, 2, 2)

    assert not has_wrong_mark(grid, 0, 0)
    assert not has_wrong_mark(grid, 0, 1)
    assert not has_wrong_mark(grid, 1, 0)
    assert not has_wrong_mark(grid, 2, 0)
    assert has_wrong_mark(grid, 2, 1)
    assert not has_wrong_mark(grid, 2, 2)

    assert sorted(get_neighbors(grid, 0, 0)) == [(0,1), (1,0), (1,1)]
    assert sorted(get_neighbors(grid, 2, 1)) == [(1,0), (1,1), (1,2), (2,0), (2,2)]
    assert sorted(get_neighbors(grid, 1, 1)) == [(0,0), (0,1), (0,2), (1,0), (1,2), (2,0), (2,1), (2,2)]

    win_grid =             [['1', '-', 'M'], 
                            ['M', '-', '-'], 
                            ['M', ' ', ' ']]

    wrong_mark_grid =      [['1', '-', 'M'], 
                            ['M', '-', '-'],
                            ['M', 'W', ' ']]

    still_has_mines_grid = [['1', '-', 'X'],
                            ['M', '-', '-'], 
                            ['M', 'W', ' ']]

    assert not check_win(grid)
    assert not check_win(wrong_mark_grid)
    assert not check_win(still_has_mines_grid)
    assert check_win(win_grid)
    

    assert generate_row(grid[0], 0) == " 0 | 1 | - | X | \n"
    assert generate_row(grid[1], 1) == " 1 | X | - | - | \n"
    assert generate_row(grid[2], 2) == " 2 | M | W |   | \n"
    
    

    three_grid = create_grid(3)
    assert three_grid == [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
    four_grid = create_grid(4)
    assert four_grid == [['-', '-', '-', '-'], ['-', '-', '-', '-'], ['-', '-', '-', '-'], ['-', '-', '-', '-']]

    # three_grid = generate_mines(three_grid, 0)
    # four_grid = generate_mines(four_grid, 5)

    # assert count_mines(three_grid) == 0
    # assert count_mines(four_grid) == 5



    print('Tests de validation de commande:')
    assert not validate_command(grid, 3, ["m22"])
    assert not validate_command(grid, 3, ['z', '1', '2'])
    assert not validate_command(grid, 3, ['m', 'a', '2'])
    assert not validate_command(grid, 3, ['d', '1', 'b'])
    assert not validate_command(grid, 3, ['d', '3', '2'])
    assert not validate_command(grid, 3, ['d', '0', '3'])
    assert not validate_command(grid, 3, ['d', '0', '0'])
    assert not validate_command(grid, 3, ['d', '2', '2'])
    print('Tests de validation de commande terminés avec succès!')
    assert validate_command(grid, 3, ['D', '0', '1']) == ('d', 0, 1)
    assert validate_command(grid, 3, ['d', '0', '2']) == ('d', 0, 2)
    assert validate_command(grid, 3, ['m', '0', '2']) == ('m', 0, 2)
    assert validate_command(grid, 3, ['d', '2', '0']) == ('d', 2, 0)
    assert validate_command(grid, 3, ['d', '2', '1']) == ('d', 2, 1)

    #Vous devez vous-même tester les fonctions set_up() et display_grid()
    #Vous n'avez pas à écrire de tests, vous pouvez les tester manuellement.
    #Gardez en tête que les tests que je vous fournis pourraient ne pas couvrir tous les cas possibles!

if __name__ == "__main__":
    tests()