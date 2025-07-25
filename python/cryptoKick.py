"""
Cryptomatte takes a million years to render after making a selection
For some reason, setting the downrez to 2:1 makes it load instantly, but then
you can't select properly in that downrez..
This script allows you to select in 1:1, hit this, it switches to 2:1, and back to 1:1 after a very
short pause.
"""


import nuke
import threading
import time

def _cryptoKick_thread_task():
    
    # Set downrez to 2
    nuke.executeInMainThread(lambda: nuke.activeViewer().node().knob('downrez').setValue(2))
    time.sleep(0.3)
    
    # Set downrez back to 1
    nuke.executeInMainThread(lambda: nuke.activeViewer().node().knob('downrez').setValue(1))


def cryptoKick():
    thread = threading.Thread(target=_cryptoKick_thread_task)
    thread.start()
