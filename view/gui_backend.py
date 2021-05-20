"""Backend GUI for base recommendation system"""
from base_sys import top

class Controller:

    def __init__(self, app):
        self.app = app
        self.count = 0
        self.top = top

    top_10 = top[0 : 10]
    def top_press(self, name):
        """Give feedback about press button."""
        if name == "Next":
            self.count += 1
            top_10 = top[10 * self.count : 10 * (self.count + 1)]
            self.app.replaceAllTableRows("Title",[[x] for x in top_10], deleteHeader=False)
            self.app.setLabel("l0", str( str((self.count * 10) + 1) + " - "  + str((self.count + 1) * 10)))
        elif name == "Back":
            self.count -= 1
            if self.count <= 0: 
                self.count = 0
                self.app.replaceAllTableRows("Title",[[x] for x in top[0:10]], deleteHeader=False)
                self.app.setLabel("l0", str( "Top " + str((self.count+1) * 10)))
            else:
                top_10 = top[10 * self.count : 10 * (self.count + 1)] 
                self.app.replaceAllTableRows("Title", [[x] for x in top_10], deleteHeader=False)
                self.app.setLabel("l0", str(str(self.count * 10 + 1) + " - " + str((self.count + 1) * 10)))
        else:
            self.count = 0
            self.app.setLabel("l0", str("Top " + str(self.count + 10)))
            self.app.replaceAllTableRows("Title",[[x] for x in top[0:10]], deleteHeader=False)