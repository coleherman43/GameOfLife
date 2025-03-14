import collections

ALIVE = "♥"
DEAD = "‧"


class LifeGrid:
    def __init__(self, pattern):
        self.pattern = pattern

    def evolve(self):
        neighbors = (
            (-1, -1), # up left
            (-1, 0), # up
            (-1, 1), # up right
            (0, -1), # left
            (0, 1), # right
            (1, -1), # down left
            (1, 0), # down
            (1, 1) # down right
        )
        num_neighbors = collections.defaultdict(int)
        for row,col in self.pattern.alive_cells:
            for drow, dcol in neighbors:
                num_neighbors[(row + drow, col + dcol)] += 1
        
        # determine which cells should stay alive (if they have 2 or 3 neighbors)
        stay_alive: set[tuple] = {
            cell for cell, num in num_neighbors.items() if num in {2, 3}
        } & self.pattern.alive_cells
        # determine which cells should come alive (if they have 3 neigbors)
        come_alive: set[tuple] = {
            cell for cell, num in num_neighbors.items() if num == 3
        } - self.pattern.alive_cells
        # update det of alive cells to have any that are still alive or coming alive
        self.pattern.alive_cells = stay_alive | come_alive

    def as_string(self, bbox: tuple):
        # define variables from bounding box tuple
        start_col, start_row, end_col, end_row = bbox
        # initialize display list
        display = [self.pattern.name.center(2 * (end_col - start_col))]
        # generate rows
        for row in range(start_row, end_row):
            display_row = [
                ALIVE if (row, col) in self.pattern.alive_cells else DEAD
                for col in range(start_col, end_col)
            ]
            display.append(" ".join(display_row))
        # return string representation
        return "\n ".join(display)

    def __str__(self):
        # create a more human-friendly way to display current state of alive cells
        return (
            f"{self.pattern.name}:\n"
            f"Alive cells -> {sorted(self.pattern.alive_cells)}"
        )
