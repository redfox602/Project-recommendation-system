"""Many window."""
from appJar import gui
import pandas as pd
import view.gui_backend as bck
import view.gui_backend_sys_v2 as bck2

app = gui("Recommendation system")
controller = bck.Controller(app)
rec_mov_plot = bck2.Controller2(app)

app.startTabbedFrame("TabbedFrame")

app.startTab("TOP 10")
app.addButtons(["Next", "Back", "Top 10"], controller.top_press)
app.addLabel("l0", "Top 10")
app.addTable("Title", [["Title"]] + [[x] for x in controller.top_10])
app.stopTab()


app.startTab("Search")
app.addLabel("l11", "You can write the title and I will find similar movies")
app.addLabelEntry("Title")
app.addButtons(["Submit", "Reset", "Cancel"], rec_mov_plot.press)
app.addEmptyLabel("prompt")
app.stopTab()

app.startTab("Similar")
app.addLabel("new", "This is showing similar movies.")
app.addTable("Title2", [["Title"]] + [[x] for x in rec_mov_plot.recommendation])
app.stopTab()

app.stopTabbedFrame()
app.setSize("400x700")
app.go()
