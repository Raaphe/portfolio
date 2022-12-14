from remise import *

def game_loop(grid, size):
    """
    Boucle principale du jeu.

    Args:
        grid: liste de listes de string représentant la grille de jeu
        size: taille du côté de la grille
    """
    while True:
        display_grid(grid)
        current_action = select_action(grid, size)
        if current_action: #valid game command selected
            action, y_pos, x_pos = current_action
            if action == 'm' and grid[y_pos][x_pos] == 'X':
                #marked a spot with a mine
                grid[y_pos][x_pos] = 'M'
                if check_win(grid):
                    display_grid(grid)
                    print("Vous avez gagné!")
                    break
            elif action == 'm' and grid[y_pos][x_pos] == '-':
                #marked a spot without mines, this is a mistake
                grid[y_pos][x_pos] = 'W'
            elif action == 'd':
                #clearing a spot
                if grid[y_pos][x_pos] == 'X' or grid[y_pos][x_pos] == 'M':
                    #hit a bomb!
                    grid[y_pos][x_pos] = '#'
                    display_grid(grid, True)
                    print("Vous avez perdu!")
                    input("Appuyez sur Enter pour quitter.")
                    break
                else:
                    #successfully cleared a spot
                    to_process = [(y_pos, x_pos)]
                    mark_cell(grid, to_process, [])
                    if check_win(grid):
                        display_grid(grid)
                        print("Vous avez gagné!")
                        input("Appuyez sur Enter pour quitter.")
                        break
        else: #quit command selected
            print("Fin de la partie...")
            break

def mark_cell(grid, to_process, processed):
    """
    Marque un groupe de cellules ne contenant pas de mines.
    Selon les règles du jeu, lorsqu'une cellule ne contient pas de mine et
    qu'elle n'est pas adjacente à une mine, on ajoute toutes ses voisines
    à liste de cellules à marquer.

    Args:
        grid: liste de listes de string représentant la grille de jeu
        to_process: liste de tuples (y_pos, x_pos) représentant les cellules
            à marquer
        processed: liste de tuples (y_pos, x_pos) représentant les cellules
            déjà marquées
    """
    #C'est un exemple de "breadth first search" modifié si jamais vous voulez
    #googler ça.  Je suis pas assez méchant pour vous donnez ça à faire
    #en première session. :D
    y_pos = to_process[0][0]
    x_pos = to_process[0][1]
    neighbors = get_neighbors(grid, y_pos, x_pos)
    total_mines = 0
    mineless_neighbors = []
    for neighbor in neighbors:
        if has_mine(grid, neighbor[0], neighbor[1]):
            total_mines += 1
        elif not has_wrong_mark(grid, neighbor[0], neighbor[1]):
            mineless_neighbors.append(neighbor)
    if total_mines == 0:
        grid[y_pos][x_pos] = " "
        #space completely empty, need to mark neighbors now
        for neighbor in mineless_neighbors:
            if neighbor not in processed and neighbor not in to_process:
                to_process.append(neighbor)
    else:
        grid[y_pos][x_pos] = str(total_mines)
    processed.append((y_pos, x_pos))
    to_process.remove((y_pos, x_pos))
    if to_process:
        mark_cell(grid, to_process, processed)

def select_action(grid, size):
    """
    Permet à l'utilisateur d'entrer une commande.  Traite les commandes "i"
    (pour instructions) et "q" (pour quitter).

    Args:
        grid: liste de listes de string représentant la grille de jeu
        size: taille du côté de la grille

    Returns:
        La commande sélectionnée ou None si l'utilisateur a choisi de quitter.
    """
    while True:
        current = input("Entrez la prochaine commande (i pour les instructions): ")
        if current.lower() == 'i':
            print("""
            Actions:
                m pour marquer une cellule d'un drapeau
                d pour découvrir une cellule
                q pour quitter
            
            Format d'une commande: <commande> <y_pos> <x_pos}
            Ex:
                m 1 2
                Cette commande marque d'un drapeau la cellule de la deuxième
                rangée et de la troisième colonne.
            """)
        elif current.lower() == 'q':
            return None
        else:
            command = validate_command(grid, size, current.split())
            if command: #returns command to game_loop if it's valid
                return command

def main():
    """
    Point d'entrée du programme.
    """
    grid, size = set_up()
    game_loop(grid, size)
    
if __name__ == "__main__":
    main()