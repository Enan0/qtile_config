from libqtile.config import Key, Group
from libqitle.command import lazy
from settings.keys import MOD,SHIFT, keys


groups = [Group(i) for i in [
    "","","","","",
]]


for i, group in enumerate(groups):
    actual_key = str(i+1)
    keys.extend([
        #mover al grupo
        Key([MOD], actual_key, lazy.group[group.name].toscreen()),

        #mover ventana al grupo
        Key([MOD,SHIFT], actual_key, lazy.window.togroup(group.name)),
    ])
