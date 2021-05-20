"""Backend GUI for second recommendation system"""
from sys_v2_rec_fun import get_recommendations

class Controller2:

    def __init__(self, app):
        self.app = app
        self.recommendation = [" "]*10

    def press(self, name):
        """Give feedback about press button."""
    
        if name == "Cancel":
            self.app.stop()

        elif name == "Reset":
            self.app.clearEntry("Title")
            self.app.setFocus("Title")
            self.app.replaceAllTableRows("Title2",[[x] for x in [" "]*10], deleteHeader=False)
            self.app.setLabel("prompt", "")
        
        elif name == "Submit":
            try: 
                self.recommendation = get_recommendations(self.app.getEntry("Title"))
                self.app.replaceAllTableRows("Title2",[[x] for x in self.recommendation], deleteHeader=False)
                self.app.setLabel("prompt", "Check in similar!")
            except KeyError:
                self.app.setLabel("prompt", "Sorry we do not have the requested\n movie in our database!")