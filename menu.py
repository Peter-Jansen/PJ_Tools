import nuke
import os

nuke.pluginAddPath('./tools')
nuke.pluginAddPath('./tools/ParticleBlinks')
nuke.pluginAddPath('./tools/Taupo')
nuke.pluginAddPath('./icons')

##########################################################################################################################################

toolbar = nuke.toolbar('Nodes') # The default nuke nodes toolbaron the left hand side of screen
p_tools = toolbar.addMenu('Peter Tools', icon = 'p.png') # add menu for Peter Tools

##########################################################################################################################################

# Draw
# Colour

p_tools.addCommand('GradeAOV', 'nuke.createNode(\'GradeAOV.nk\')', icon = 'p.png')
p_tools.addCommand('HueCorrect Soft', 'nuke.createNode(\'HueCorrectSoft.nk\')', icon = 'p.png')
p_tools.addCommand('HueVsHue', 'nuke.createNode(\'HueVsHue.nk\')', icon = 'p.png')
p_tools.addCommand('LogSat', 'nuke.createNode(\'LogSat.nk\')', icon = 'p.png')
p_tools.addCommand('Soft Crush Highlights', 'nuke.createNode(\'SoftCrushHighlights.nk\')', icon = 'p.png')
p_tools.addCommand('SoftContrast', 'nuke.createNode(\'SoftContrast.nk\')', icon = 'p.png')
p_tools.addSeparator()
# Filter

p_tools.addCommand('Bump Displace', 'nuke.createNode(\'BumpDisplace.nk\')', icon = 'bumpDisplace.png')
p_tools.addCommand('Edge Inpaint', 'nuke.createNode(\'Edge_Inpaint.nk\')', icon = 'p.png')
p_tools.addCommand('Edge Push', 'nuke.createNode(\'EdgePush.nk\')', icon = 'EdgePush.png')
p_tools.addCommand('Glass', 'nuke.createNode(\'Glass.nk\')', icon = 'p.png')
p_tools.addCommand('Guided Blur Fast', 'nuke.createNode(\'GuidedBlurFast.nk\')', icon = 'p.png')
p_tools.addCommand('DualPassGuidedBlur', 'nuke.createNode(\'DualPassGuidedBlur.nk\')', icon = 'p.png')
p_tools.addCommand('Lens Juice', 'nuke.createNode(\'Lens_Juice.nk\')', icon = 'p.png')
p_tools.addCommand('RSMB Ghetto', 'nuke.createNode(\'RSMB_Ghetto.nk\')', icon = 'p.png')
p_tools.addCommand('Sharpie', 'nuke.createNode(\'Sharpie.nk\')', icon = 'p.png')
p_tools.addCommand('Vignette', 'nuke.createNode(\'Vignette.nk\')', icon = 'p.png')
p_tools.addCommand('VectorBlurOverscan', 'nuke.createNode(\'VectorBlurOverscan.nk\')', icon = 'p.png')
p_tools.addCommand('DiffusionRays', 'nuke.createNode(\'DiffusionRays.nk\')', icon = 'p.png')
p_tools.addSeparator()

# Keying

# TaupoRender
taupo = p_tools.addMenu('Taupo')
taupo.addCommand('TaupoRender', 'nuke.createNode(\'TaupoRender.nk\')', icon = 'p.png')
p_tools.addSeparator()

# Particle Blinkscripts
p_blinks = p_tools.addMenu('Particle Blinks')
p_blinks.addCommand('ParticleCurlNoise', 'nuke.createNode(\'ParticleCurlNoise.nk\')', icon = 'p.png')
p_blinks.addCommand('ParticleVelocityProjection', 'nuke.createNode(\'ParticleVelocityProjection.nk\')', icon = 'p.png')
p_blinks.addCommand('Random Rotation', 'nuke.createNode(\'random_rotation.nk\')', icon = 'p.png')
p_blinks.addCommand('ParticleFade', 'nuke.createNode(\'ParticleFade.nk\')', icon = 'p.png')
p_tools.addSeparator()

# Tansform
p_tools.addCommand('CopyAndTransform', 'nuke.createNode(\'CopyAndTransform.nk\')', icon = 'p.png')
p_tools.addSeparator()
# Other

p_tools.addCommand('Fuse', 'nuke.createNode(\'Fuse.nk\')', icon = 'p.png')
p_tools.addCommand('Subframer', 'nuke.createNode(\'Subframer.nk\')', icon = 'p.png')
p_tools.addCommand('MultiWipe', 'nuke.createNode(\'MultiWipe.nk\')', icon = 'p.png')


