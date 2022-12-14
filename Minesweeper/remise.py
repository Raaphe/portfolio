from random import randint

def set_up():
    """
    Met en place une nouvelle partie.  Demande à l'utilisateur d'entrer les
    paramètres de la nouvelle grille de jeu.  Utilise ensuite ces valeurs
    dans des appels vers create_grid() et generate_mines().

    Returns:
        Un tuple (grid, size) dont le premier élément est une liste de listes
        de string représentant la grille de jeu de départ (incluant les mines),
        et le deuxième élément est la taille de la grille.
    """
    grid_size = int(input("Entrez la taille du champ de mines: "))
    num_mines = int(input("Entrez le nombre de mines: "))
    
    if num_mines > grid_size * grid_size:
        print("Vous avez entrez un nombre de bombes trop grands...")
        return False;

    grid = generate_mines(create_grid(grid_size),num_mines)

    return (grid, grid_size)


def create_grid(size):
    """
    Crée une grille de jeu carrée

    Args:
        size: taille du côté de la grille
    
    Returns:
        Une liste de liste contenant le caractère '-' représentant une nouvelle
        cellule de jeu.
    """
    grid = []
    
    for _ in range(size):
        grid.append(['-']*size)

    return grid

def generate_mines(grid, nb_mines):
    """
    Génère les mines dans la grille de jeu fournie

    Args:
        grid: liste de listes de string représentant la grille de jeu
        nb_mines: le  nombre de mines à ajouter à la grille
    """
    counter = nb_mines

    while counter > 0:
        grid[randint(0, len(grid)-1)][randint(0, len(grid)-1)] = 'X'
        counter -= 1

    
    #Vous allez devoir utiliser la fonction randint du module random
    #https://www.w3schools.com/python/ref_random_randint.asp
    #J'ai importé le module d'une manière qui vous permet d'utiliser
    #randint, et non random.randint
    return grid
    
def display_grid(grid, lost = False):
    """
    Affiche à l'écran la grille de jeu. 
    - Les mines sont cachées et les
        marques incorrectes sont indiqués de la même manière que les marques
        correctes lorsque le paramètre lost est mis à False.  
    -Lorsqu'il est mis à True, la vraie grille de jeu est révélée et la mine qui a explosé
    est marqué d'un #.

    Args:
        grid: liste de listes de string représentant la grille de jeu
        lost: True si la partie est perdue.  Dans ce cas, les mines sont
        affichées.
    
    """
    size = len(grid)
    first_row = "\nY\X| "
    first_row += "   ".join(map(str, list(range(size)))) + "\n"
    display = ""

    for ii in range(len(grid)):
        display += generate_row(grid[ii], ii)

    display = display.replace('X', '-')
    display = display.replace('W', 'M')

    #Une fois la grille affichée, vous pouvez utliliser la fonction replace()
    #pour cacher les mines "X" en les remplaçant par des "-".  Vous devez aussi
    #cacher les mauvaises marques "W" en les remplaçant par des marques normales.
    #Notez ici que c'est seulement l'affichaque que vous modifiez!  La grille
    #doit rester identique en mémoire.
    #https://www.w3schools.com/python/ref_string_replace.asp

    print(first_row + display)

def generate_row(row, y_pos):
    """
    Génère une chaîne représentant une rangée de la grille de jeu.
    
    Args:
        row: liste de string représentant une rangée de la grille
        y_pos: entier représentant la coordonnée en y de la rangée
    
    Returns:
        Une chaîne de caractère représentant la rangée.  Les mines
        sont visibles, tout commme les marques incorrectes.
    """
    start = f" {str(y_pos)} | "
    middle =  ' | '.join(row)
    
    new_row = start + middle + ' |'
    
    return new_row + ' \n'
    

def get_neighbors(grid, y_pos, x_pos):
    """
    Obtient toutes les cellules touchant à celle passée en argument.

    Args:
        grid: liste de listes de string représentant la grille de jeu
        y_pos: position en y de la cellule
        x_pos: position en x de la cellule
    
    Returns:
        Une liste de tuples (y_pos, x_pos), chacun représentant une cellule
        voisine.  La cellule visée ne fait pas partie de la liste.
    """
    # target = grid[y_pos][x_pos]
    list_dummy = []

    
    list_dummy.append((y_pos-1,x_pos-1))
    list_dummy.append((y_pos,x_pos-1))
    list_dummy.append((y_pos+1,x_pos-1))
    list_dummy.append((y_pos+1,x_pos))
    list_dummy.append((y_pos+1,x_pos+1))
    list_dummy.append((y_pos,x_pos+1))
    list_dummy.append((y_pos-1,x_pos+1))
    list_dummy.append((y_pos-1,x_pos))

    index_list = []

    
    for ii in range(8):
        if (list_dummy[ii][0] >= 0 and list_dummy[ii][1] >= 0) and (list_dummy[ii][0] < len(grid) and list_dummy[ii][1] < len(grid)):
            index_list.append(ii)



    list_tuples = []


    for ii in range(len(index_list)):
        list_tuples.append(list_dummy[index_list[ii]])

    return list_tuples


def has_mine(grid, y_pos, x_pos):
    """
    Determine si une cellule contient des mines.

    Args:
        grid: liste de listes de string représentant la grille de jeu
        y_pos: position en y de la cellule
        x_pos: position en x de la cellule
    
    Returns:
        True si la cellule contient une mine.

    """
    if grid[y_pos][x_pos] == 'X' or grid[y_pos][x_pos] == 'M':
        return True;
    else:
        return False;
 
def has_wrong_mark(grid, y_pos, x_pos):
    """
    Determine si une cellule contient une cellule marquée qui ne contient pas
    de mine.

    Args:
        grid: liste de listes de string représentant la grille de jeu
        y_pos: position en y de la cellule
        x_pos: position en x de la cellule
    
    Returns:
        True si la cellule est marquée mais ne contient pas de mine.
    """
    if grid[y_pos][x_pos] == "W":
        return True;
    else: 
        return False;
    

def check_win(grid):
    """
    Détermine si l'utilisateur a gagné.

    Args:
        grid: liste de listes de string représentant la grille de jeu

    Returns:
        True si l'utilisateur a gagné.
    """
    for row in grid:
        for cell in row:
            if cell == 'X' or cell == 'W':
                return False;
    
    return True;
            


def validate_command(grid, size, command):
    """
    Analyse et valide une commande entrée par l'utilisateur

    Args:
        grid: liste de listes de string représentant la grille de jeu
        size: taille du côté de la grille
        command: chaîne de caractère représentant la commande à valider

    Returns:
        Un tuple de la forme (<lettre>, y_pos, x_pos) où la lettre représente
        l'action à effectuer et les deux autres éléments représentent la
        cellule sur laquelle on agit.  Renvoie None si la commande est invalide.
    """
    
        # variables
    
    command[0] = command[0].lower()
    print(command)

    #makes sure command is 3 characters, is a valid command (M or D) and if arg 1 and 2 are numbers 
    if len(command) != 3:
        print("Commande invalide : mauvais nombre d'arguments.")
        return None;
    elif command[0] != "m" :
        if command[0] != "d":
            print("Commande invalide : action non recconue. ")
            return None;

    #Turns numericals from str to int
    if command[1].isnumeric() == True and command[2].isnumeric()== True:
        for _ in range(1, 3):
            str_num = command.pop(1) 
            command.append(int(str_num))
    else:
        print("Commande invalide : coordonée(s) non numérique(s).") 
        return None;

    #Makes sure commands [1] and [2] are in the grid itself
    if command[1] > (size - 1) or command[2] > (size - 1):
        print("Commande invalide : Les coordonnées dépassent les limites du jeux.")
        return None;
    
    command_target = grid[command[1]][command[2]]
    
    if command_target == ' ' or command_target.isnumeric() == True:
        return None;

    return (command[0], command[1], command[2]);




def count_mines(grid):
    """
    Compte le nombre de mines dans une grille.

    Args:
        grid: liste de liste de string contenant des caractère.
    Returns:
        Nombre entier qui représente le nombre de mines dans un champ donné.
    
    """
    
    counter = 0

    for row in grid:
        for cell in row:
            if cell == 'X' or cell == 'M':
                counter = counter + 1
                
    return counter

