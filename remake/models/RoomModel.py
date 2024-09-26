from models.enums.Material import Material

class Room():
    """
    Une RoomModel est une matrice qui contient des tiles.
    Son implémentation est indépentante de la MapView.
    """

    def __init__(self) -> None:
        doorsNumbers = 0
        tile_texture = Material.wall

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
