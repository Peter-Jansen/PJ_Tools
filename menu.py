import nuke
import os

nuke.pluginAddPath('./tools')
nuke.pluginAddPath('./icons')

##########################################################################################################################################

toolbar = nuke.toolbar('Nodes') # The default nuke nodes toolbaron the left hand side of screen
p_tools = toolbar.addMenu('Peter Tools', icon = 'p.png') # add menu for Peter Tools

##########################################################################################################################################

# Draw

# Colour

# Filter
filter = p_tools.addMenu('Filter', icon = 'p.png')

filter.addCommand('Bump Displace', 'nuke.createNode(\'BumpDisplace.nk\')', icon = 'bumpDisplacepng')

# Keying

# Tansform

# Other