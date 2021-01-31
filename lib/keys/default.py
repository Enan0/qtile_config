from libqtile import layout
from libqtile.config import Key
from libqitle.confgi import lazy

MOD     = "mod4"
SHIFT   = "shift"
ALT     = "alt"
CONTROL = "control"



keys = [
        #move focus hotkeys
        Key([MOD], "left" , lazy.layout.left()),    #move left
        Key([MOD], "right", lazy.layout.right()),   #move rigth
        Key([MOD], "down" , lazy.layout.down()),    #move down
        Key([MOD], "up"   , lazy.layout.up()),      #move up
        
        #move windows hotkeys

            Key([MOD, SHIFT], "left" , lazy.layout.shuffle_left()),
            #move window left
            Key([MOD, SHIFT], "right", lazy.layout.shuffle_right()),
            #move window right
            Key([MOD, SHIFT], "down" , lazy.layout.shuffle_down()),
            #move window down
            Key([MOD, SHIFT], "up"   , lazy.layout.shuffle_up()),
            #move window up

            #grow window hotkeys
            Key([MOD,CONTROL], "left", lazy.layout.grow_left()),
            #grow window left
            Key([MOD,CONTROL], "right", lazy.layout.grow_right()),
            #grow window left
            Key([MOD,CONTROL], "down", lazy.layout.grow_down()),
            #grow window left
            Key([MOD,CONTROL], "up", lazy.layout.grow_up()),
            #grow window left
            Key([MOD,CONTROL], "n", lazy.layout.normalize()),
            #normalize windows

        Key([MOD], "Return", lazy.spawn(terminal), desc="Launch terminal"),
        #spawn window
        Key([MOD], "w", lazy.window.kill()),
        #kill window
        





        
]
