import matplotlib.animation as animation
import matplotlib.pyplot as plt 
import numpy as np
import json, pathlib
from src.core import Core

class Game(Core):
    def __init__(self) -> None:
        """
        Instantiate before the game launches
        """
        Core().__init__()
        self.config = self.load_config()
        self.settings = self.config["settings"]
        self.gridvalues = [255, 0] # ON / OFF ; True / False
    
    def load_config(self) -> object:
        """
        Tries to read the game configuration.

        Returns the configuration file in JSON if loaded correctly
        Otherwise it will raise a FileNotFoundError exception.
        """
        try:
            with open(str(pathlib.PurePosixPath(pathlib.Path(__file__).parent.parent.resolve(), "game_config.json"))) as F:
                return json.load(F)
        except FileNotFoundError: raise FileNotFoundError(
            "Could not find the game configuration in the root directory, make sure you are up to date with the repository on github")

    def random_grid(self, N):
        """returns a grid of NxN random values"""
        return np.random.choice(self.gridvalues, N*N, p=[0.2, 0.8]).reshape(N, N)

    def start(self) -> None:
        print("Installing settings")
        gridsize = self.config["gridsize"]
        gamefps = self.settings["targetfps"]
        grid = self.random_grid(gridsize)

        print("Game started ... ")
        fig, ax = plt.subplots()
        img = ax.imshow(grid, interpolation='nearest')
        ani = animation.FuncAnimation(fig, self.update, fargs=(img, grid, gridsize, ),
                                frames = 10,
                                interval=gamefps,
                                save_count=50)
        plt.show()
        print("... Game ended")