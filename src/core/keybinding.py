import numpy as np

class KeyBinding(object):
    def __init__(self) -> None:
        super().__init__()

    def keybinding_sandbox(self, event):
        """
        Calculates clicked position into numpy array position.
        Tries to stay in bounderies.
        """
        click_type = 'double' if event.dblclick else 'single'
        mouse_button = event.button

        # Convert to position in numpy array
        if event.inaxes:
            if mouse_button == 3:
                self.modifications = (-69, -69)
            else:
                x, y = int(np.round(event.xdata % self.config["gridsize"])), int(np.round(event.ydata % self.config["gridsize"]))
                self.modifications = (x if x > 0 and x <= self.config["gridsize"] else 0, y if y > 0 and y <= self.config["gridsize"] else 0)
                # print(f'{click_type} click: button={mouse_button}, x={x}, y={y}, xdata={event.xdata}, ydata={event.ydata}')
