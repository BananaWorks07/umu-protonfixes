"""Game fix for SP-Tushonka"""

from protonfixes import util

def main() -> None:
    # Required by commonly used mod launchers (e.g "SVM")
    util.protontricks('dotnetdesktop9')

    # Required to not crash on game launch ("BepInEx" hook)
    util.winedll_override('winhttp', util.OverrideOrder.NATIVE_BUILTIN) # recheck with proton 12
    util.winedll_override('version', util.OverrideOrder.NATIVE_BUILTIN)
