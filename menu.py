



import nuke
import os

nuke.pluginAddPath('./python')
nuke.pluginAddPath('./tools')
nuke.pluginAddPath('./tools/ParticleBlinks')
nuke.pluginAddPath('./icons')


import cryptoKick


# Hotkeys
nuke.menu('Viewer').addCommand('cryptoKick', 'cryptoKick.cryptoKick()', 'ctrl+space')

##########################################################################################################################################

toolbar = nuke.toolbar('Nodes') # The default nuke nodes toolbaron the left hand side of screen
p_tools = toolbar.addMenu('Peter Tools', icon = 'p.png') # add menu for Peter Tools

##########################################################################################################################################

# Draw
# Colour
colour = p_tools.addMenu('Colour')
colour.addCommand('GradeAOV', 'nuke.createNode(\'GradeAOV.nk\')', icon = 'p.png')
colour.addCommand('HueCorrect Soft', 'nuke.createNode(\'HueCorrectSoft.nk\')', icon = 'p.png')
colour.addCommand('HueVsHue', 'nuke.createNode(\'HueVsHue.nk\')', icon = 'p.png')
colour.addCommand('LogSat', 'nuke.createNode(\'LogSat.nk\')', icon = 'p.png')
colour.addCommand('Soft Crush Highlights', 'nuke.createNode(\'SoftCrushHighlights.nk\')', icon = 'p.png')
colour.addCommand('SoftContrast', 'nuke.createNode(\'SoftContrast.nk\')', icon = 'p.png')
p_tools.addSeparator()

# Filter
filter = p_tools.addMenu('Filter')
filter.addCommand('Bump Displace', 'nuke.createNode(\'BumpDisplace.nk\')', icon = 'bumpDisplace.png')
filter.addCommand('ImageLight', 'nuke.createNode(\'ImageLight.nk\')', icon = 'p.png')
filter.addCommand('Edge Inpaint', 'nuke.createNode(\'Edge_Inpaint.nk\')', icon = 'p.png')
filter.addCommand('Edge Push', 'nuke.createNode(\'EdgePush.nk\')', icon = 'EdgePush.png')
filter.addCommand('Glass', 'nuke.createNode(\'Glass.nk\')', icon = 'p.png')
filter.addCommand('Guided Blur Fast', 'nuke.createNode(\'GuidedBlurFast.nk\')', icon = 'p.png')
filter.addCommand('DualPassGuidedBlur', 'nuke.createNode(\'DualPassGuidedBlur.nk\')', icon = 'p.png')
filter.addCommand('Lens Juice', 'nuke.createNode(\'Lens_Juice.nk\')', icon = 'p.png')
filter.addCommand('RSMB Ghetto', 'nuke.createNode(\'RSMB_Ghetto.nk\')', icon = 'p.png')
filter.addCommand('Sharpie', 'nuke.createNode(\'Sharpie.nk\')', icon = 'p.png')
filter.addCommand('Vignette', 'nuke.createNode(\'Vignette.nk\')', icon = 'p.png')
filter.addCommand('VectorBlurOverscan', 'nuke.createNode(\'VectorBlurOverscan.nk\')', icon = 'p.png')
filter.addCommand('DiffusionRays', 'nuke.createNode(\'DiffusionRays.nk\')', icon = 'p.png')
p_tools.addSeparator()

# Keying

# Particle Blinkscripts
p_blinks = p_tools.addMenu('Particle Blinks')
p_blinks.addCommand('ParticleCurlNoise', 'nuke.createNode(\'ParticleCurlNoise.nk\')', icon = 'p.png')
p_blinks.addCommand('ParticleVelocityProjection', 'nuke.createNode(\'ParticleVelocityProjection.nk\')', icon = 'p.png')
p_blinks.addCommand('Random Rotation', 'nuke.createNode(\'random_rotation.nk\')', icon = 'p.png')
p_blinks.addCommand('ParticleFade', 'nuke.createNode(\'ParticleFade.nk\')', icon = 'p.png')
p_tools.addSeparator()

# Tansform
transform = p_tools.addMenu('Transform')
transform.addCommand('CopyAndTransform', 'nuke.createNode(\'CopyAndTransform.nk\')', icon = 'p.png')
p_tools.addSeparator()

# Other
other = p_tools.addMenu('Other')
other.addCommand('Fuse', 'nuke.createNode(\'Fuse.nk\')', icon = 'p.png')
other.addCommand('Subframer', 'nuke.createNode(\'Subframer.nk\')', icon = 'p.png')
other.addCommand('MultiWipe', 'nuke.createNode(\'MultiWipe.nk\')', icon = 'p.png')
