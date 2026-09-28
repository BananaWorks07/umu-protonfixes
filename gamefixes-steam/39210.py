"""Game fix for FFXIV"""

import os
from protonfixes import util

def main() -> None:
    """FFXIV add NOSTEAM option."""
    # Fixes the startup process.
    if 'NOSTEAM' in os.environ:
        util.replace_command('-issteam', '')

    # disable new character intro cutscene to prevent black screen loop
    configpath = os.path.join(
        util.protonprefix(),
        'drive_c/users/steamuser/My Documents/My Games/FINAL FANTASY XIV - A Realm Reborn',
    )
    if not os.path.exists(configpath):
        os.makedirs(configpath)
