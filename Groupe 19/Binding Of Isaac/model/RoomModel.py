from Material import Material

class Room:
    doorsNumbers = 0
    col = 45
    row = 80
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
