#------------------------------------------------------------------------------#
#-------------------------------------------------------------------- HEADER --#

"""
:author:
    acarlisle

:description:
    Main reloader for core.
"""
#------------------------------------------------------------------------------#
#------------------------------------------------------------------- IMPORTS --#

# built-in
from maya import OpenMaya

# internal
import build

#------------------------------------------------------------------------------#
#----------------------------------------------------------------- FUNCTIONS --#

def reload_core():
    reload(build)
    return OpenMaya.MGlobal_displayInfo("-------------> CORE RELOAD: OK")
