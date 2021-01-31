from libqtile.config import Key, Group, Match
from libqtile.lazy   import lazy

from settings.keys import MOD,SHIFT, keys


groups = [Group(i) for i in [
    "","","","",""
]]


for i, group in enumerate(groups):
    actual_key = str(i + 1)
    keys.extend([
        # Switch to workspace N
        Key([MOD], actual_key, lazy.group[group.name].toscreen()),
        # Send window to workspace N
        Key([MOD, SHIFT], actual_key, lazy.window.togroup(group.name))
    ])

