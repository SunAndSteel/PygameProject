from Material import Material

class Room:
    items_of_room = [] 
    doorsNumbers = 0
    tile_size = 32
    col = 40
    row = 20
    tile_skin = Material.wall
    
    @staticmethod
    def generate_room(cols, rows):
        """
        Génération d'une matrice de représentant une salle vide avec une bordure
        """
        matrix = [[0 for _ in range(cols)] for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
                    matrix[i][j] = 1
        return matrix
