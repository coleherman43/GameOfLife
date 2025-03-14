import pygame
from game.grid import LifeGrid

class PygameView:
    def __init__(self, pattern, gen=100, frame_rate=7, cell_size=10, grid_color=(200,200,200), alive_color=(0,255,0), dead_color=(0,0,0)):
        self.pattern = pattern
        self.gen = gen
        self.frame_rate = frame_rate
        self.cell_size = cell_size
        self.grid_color = grid_color
        self.alive_color = alive_color
        self.dead_color = dead_color
        self.grid = LifeGrid(pattern)
        self.width = 800
        self.height = 600
        self.screen = None

    def show(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Conway's Game of Life")
        clock = pygame.time.Clock()

        for _ in range(self.gen):
            self.handle_events()
            self.draw_grid()
            self.grid.evolve()
            pygame.display.flip()
            clock.tick(self.frame_rate)

        pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        
    def draw_grid(self):
        self.screen.fill(self.dead_color)
        for row in range(self.height // self.cell_size):
            for col in range(self.width // self.cell_size):
                color = self.alive_color if (row, col) in self.grid.pattern.alive_cells else self.dead_color
                pygame.draw.rect(
                    self.screen,
                    color,
                    pygame.Rect(col * self.cell_size, row * self.cell_size, self.cell_size, self.cell_size)
                )
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, self.grid_color, (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, self.grid_color, (0, y), (self.width, y))

    