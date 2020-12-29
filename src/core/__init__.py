from src.core.keybinding import KeyBinding
import numpy as np
class Core(KeyBinding):

    def __init__(self) -> None:
        self._configured = False
        KeyBinding.__init__(self)
        self.modifications = ()
        super().__init__()

    def update(self, frame_number, img, grid) -> tuple:
        """
        Updates each frame in matplotlib, responsible for calling game logic/ruling and applies this for each frame
        """
        self.grid = grid
        newGrid = grid.copy()
        for x in range(self.config["gridsize"]):
            for y in range(self.config["gridsize"]):
                newGrid = self.apply_conway_rules(newGrid, self.compute_grid(grid, x, y), x, y)    
        # update data
        img.set_data(newGrid)
        if self.modifications:
            if self.modifications == (-69, -69):
                print("* Cleared playing field")
                newGrid[newGrid >= 0] = 0
            else:
                print("* Added star in the universe")
                gridsize = int(self.config["gridsize"])
                try:  # Add pixel!
                    newGrid[ self.modifications[1], self.modifications[0] ] = 255
                    newGrid[ self.modifications[1], self.modifications[0] + 1 if self.modifications[0] + 1 <= gridsize else gridsize ] = 255
                    newGrid[ self.modifications[1] - 1 if self.modifications[1] - 1 >= 0 else 0, self.modifications[0] ] = 255
                except IndexError: pass
            self.modifications = ()
        grid[:] = newGrid[:]
        return (img,)
    
    def apply_conway_rules(self, grid, computed_grid, x, y) -> object:
        """
        This method applies the conway rules. A fast reminder from the game rules:
        
        1. Any live cell with fewer than two live neighbours dies, as if caused by under-population.
        2. Any live cell with two or three live neighbours lives on the next generation.
        3. Any live cell with more than three live neighbours dies, as if by overcrowding
        4. Any dead cell with exactly three live neigbours becomes a live cell, as if by reproduction

        Note; 255 == ON; 0 == OFF
        """
        if grid[x, y] == 255:
            if (computed_grid < 2) or (computed_grid > 3):
                grid[x, y] = 0
        else:
            if computed_grid == 3:
                grid[x, y] = 255
        return grid

    def compute_grid(self, grid, x, y) -> int:
        """
        Calculates the neighbour sum of the current neighbours.
        The result out of the method is used to calculate the conway rules.
        """
        return int((
            grid[ x, ( y - 1 ) % self.config["gridsize"]] + 
            grid[ x, ( y + 1 ) % self.config["gridsize"]] +
            grid[( x - 1 ) % self.config["gridsize"], y ] +
            grid[( x + 1 ) % self.config["gridsize"], y ] +
            grid[( x - 1 ) % self.config["gridsize"], ( y - 1 ) % self.config["gridsize"]] + 
            grid[( x - 1 ) % self.config["gridsize"], ( y + 1 ) % self.config["gridsize"]] +
            grid[( x + 1 ) % self.config["gridsize"], ( y - 1 ) % self.config["gridsize"]] + 
            grid[( x + 1 ) % self.config["gridsize"], ( y + 1 ) % self.config["gridsize"]]
            ) / 255 )
    
    def set_figure(self, fig) -> None:
        """
        Updates fig with the current available fig.
        """
        self.fig = fig
        if not self._configured:
            # This section only applies on startup
            if self.settings["sandbox"]:
                # Apply keybinding for sandbox mode
                fig.canvas.mpl_connect('button_press_event', self.keybinding_sandbox)

            # Let the application know the configuration parameters have been configured
            self._configured = True