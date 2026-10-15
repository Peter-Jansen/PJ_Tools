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

toolbar = nuke.toolbar('Nodes') # The default nuke nodes toolbar on the left hand side of screen
p_tools = toolbar.addMenu('Peter Tools', icon = 'p.png') # add menu for Peter Tools

##########################################################################################################################################

# Draw
draw = p_tools.addMenu('Draw')
draw.addCommand('CellNoise', 'nuke.createNode(\'CellNoise.nk\')', icon = 'CellNoise.png')
p_tools.addSeparator()

# Colour
colour = p_tools.addMenu('Colour')
colour.addCommand('GradeAOV', 'nuke.createNode(\'GradeAOV.nk\')', icon = 'GradeAOV.png')
colour.addCommand('HueCorrect Soft', 'nuke.createNode(\'HueCorrectSoft.nk\')', icon = 'HueCorrectSoft.png')
colour.addCommand('HueVsHue', 'nuke.createNode(\'HueVsHue.nk\')', icon = 'HueVsHue.png')
colour.addCommand('LogSat', 'nuke.createNode(\'LogSat.nk\')', icon = 'LogSat.png')
colour.addCommand('Soft Crush Highlights', 'nuke.createNode(\'SoftCrushHighlights.nk\')', icon = 'SoftCrushHighlights.png')
colour.addCommand('SoftContrast', 'nuke.createNode(\'SoftContrast.nk\')', icon = 'SoftContrast.png')
p_tools.addSeparator()

# Filter
filter = p_tools.addMenu('Filter')
filter.addCommand('Bump Displace', 'nuke.createNode(\'BumpDisplace.nk\')', icon = 'BumpDisplace.png')
filter.addCommand('ImageLight', 'nuke.createNode(\'ImageLight.nk\')', icon = 'ImageLight.png')
filter.addCommand('Edge Inpaint', 'nuke.createNode(\'Edge_Inpaint.nk\')', icon = 'Edge_Inpaint.png')
filter.addCommand('Edge Push', 'nuke.createNode(\'EdgePush.nk\')', icon = 'EdgePush.png')
filter.addCommand('Glass', 'nuke.createNode(\'Glass.nk\')', icon = 'Glass.png')
filter.addCommand('Guided Blur Fast', 'nuke.createNode(\'GuidedBlurFast.nk\')', icon = 'GuidedBlurFast.png')
filter.addCommand('DualPassGuidedBlur', 'nuke.createNode(\'DualPassGuidedBlur.nk\')', icon = 'GuidedBlurFast.png')
filter.addCommand('Lens Juice', 'nuke.createNode(\'Lens_Juice.nk\')', icon = 'Lens_Juice.png')
filter.addCommand('RSMB Ghetto', 'nuke.createNode(\'RSMB_Ghetto.nk\')', icon = 'RSMB_Ghetto.png')
filter.addCommand('Sharpie', 'nuke.createNode(\'Sharpie.nk\')', icon = 'Sharpie.png')
filter.addCommand('Vignette', 'nuke.createNode(\'Vignette.nk\')', icon = 'Vignette.png')
filter.addCommand('VectorBlurOverscan', 'nuke.createNode(\'VectorBlurOverscan.nk\')', icon = 'VectorBlurOverscan.png')
filter.addCommand('DiffusionRays', 'nuke.createNode(\'DiffusionRays.nk\')', icon = 'DiffusionRays.png')
filter.addCommand('Confocus', 'nuke.createNode(\'Confocus.nk\')', icon = 'Confocus.png')
filter.addCommand('InpaintFaster', 'nuke.createNode(\'InpaintFaster.nk\')', icon = 'InpaintFaster.png')
filter.addCommand('Astigmatism', 'nuke.createNode(\'Astigmatism.nk\')', icon = 'Astigmatism.png')
filter.addCommand('ArtLens', 'nuke.createNode(\'ArtLens.nk\')', icon = 'ArtLens.png')
filter.addCommand('ArtLensDepth', 'nuke.createNode(\'ArtLensDepth.nk\')', icon = 'ArtLensDepth.png')
filter.addCommand('VibeFractal', 'nuke.createNode(\'VibeFractal.nk\')', icon = 'VibeFractal.png')

p_tools.addSeparator()

# Keying

# Particle Blinkscripts
p_blinks = p_tools.addMenu('Particle Blinks')
p_blinks.addCommand('ParticleCurlNoise', 'nuke.createNode(\'ParticleCurlNoise.nk\')', icon = 'ParticleCurlNoise.png')
p_blinks.addCommand('ParticleWindNoise', 'nuke.createNode(\'ParticleWindNoise.nk\')', icon = 'ParticleWindNoise.png')
p_blinks.addCommand('ParticleVelocityProjection', 'nuke.createNode(\'ParticleVelocityProjection.nk\')', icon = 'ParticleVelocityProjection.png')
p_blinks.addCommand('Random Rotation', 'nuke.createNode(\'random_rotation.nk\')', icon = 'random_rotation.png')
p_blinks.addCommand('ParticleFade', 'nuke.createNode(\'ParticleFade.nk\')', icon = 'ParticleFade.png')
p_blinks.addCommand('ParticleLookatXZ', 'nuke.createNode(\'ParticleLookatXZ.nk\')', icon = 'ParticleLookatXZ.png')
p_tools.addSeparator()

# Tansform
transform = p_tools.addMenu('Transform')
transform.addCommand('CopyAndTransform', 'nuke.createNode(\'CopyAndTransform.nk\')', icon = 'CopyAndTransform.png')
transform.addCommand('CardPlacer', 'nuke.createNode(\'Card_Placer.nk\')', icon = 'Card_Placer.png')

p_tools.addSeparator()

# Other
other = p_tools.addMenu('Other')
other.addCommand('Fuse', 'nuke.createNode(\'Fuse.nk\')', icon = 'Fuse.png')
other.addCommand('Wire3D', 'nuke.createNode(\'Wire3D.nk\')', icon = 'Wire3D.png')
other.addCommand('Subframer', 'nuke.createNode(\'Subframer.nk\')', icon = 'Subframer.png')
other.addCommand('MultiWipe', 'nuke.createNode(\'MultiWipe.nk\')', icon = 'MultiWipe.png')
other.addCommand('Arri_Grain', 'nuke.createNode(\'Arri_Grain.nk\')', icon = 'Arri_Grain.png')
other.addCommand('DeepThicknessTextured', 'nuke.createNode(\'DeepThicknessTextured.nk\')', icon = 'DeepThicknessTextured.png')
other.addCommand('STMapExpand', 'nuke.createNode(\'STMapExpand.nk\')', icon = 'STMapExpand.png')
#other.addCommand('MultiWipeICE', lambda: nuke.loadToolset(r"Z:\depts\comp\users\peter.jansen\nuke_tools\PJ_Tools\tools\MultiWipeICE.nk"), icon = 'p.png')