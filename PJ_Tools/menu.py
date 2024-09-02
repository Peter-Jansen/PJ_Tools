import nuke
import os

# P_FolderPath = os.path.dirname(__file__)


nuke.pluginAddPath('./gizmos')
nuke.pluginAddPath('./icons')

toolbar = nuke.toolbar('Nodes') # The default nuke nodes toolbaron the left hand side of screen

p_tools = toolbar.addMenu('Peter Tools', icon = 'p.png') # add menu for Peter Tools

# Draw

# Colour

# Filter
filter = p_tools.addMenu('Filter', icon = 'p.png')

filter.addCommand('Fractal Blur', 'nuke.createNode(\'fractalBlur2.nk\')', icon = 'fractalBlur.png')

# Keying

# Tansform

# Other