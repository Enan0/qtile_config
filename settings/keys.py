from libqtile.config  import Key
from libqtile.lazy import lazy

MOD     = "mod4"
ALT     = "ALT"
SHIFT   = "shift"
CONTROL = "control"

LEFT = "h"
RIGHT= "l"
DOWN = "j"
UP   = "k"

keys = [
        #move focus window
        Key([MOD],LEFT, lazy.layout.left()),
        Key([MOD],RIGHT, lazy.layout.right()),
        Key([MOD],DOWN, lazy.layout.down()),
        Key([MOD],UP, lazy.layout.up()),

        #windows size
        Key([MOD,SHIFT], LEFT, lazy.layout.grow()),
        Key([MOD,SHIFT], RIGHT, lazy.layout.shrink()),
        
        #move in stack
        Key([MOD,SHIFT], DOWN, lazy.layout.suffle_down()),
        Key([MOD,SHIFT], UP, lazy.layout.suffle_up()),

        #kill windows
        Key([MOD],"q", lazy.window.kill()),

        #restart shutdown
        Key([MOD, CONTROL,SHIFT], "r", lazy.restart()),
        Key([MOD, CONTROL,SHIFT], "q", lazy.shutdown()),

        #change layout
        Key([MOD], "Tab", lazy.next_layout()),
        Key([MOD, SHIFT], "Tab", lazy.prev_layout()),
        #spawn windows
        Key([MOD],"Return", lazy.spawn("alacritty")),

        Key([], "XF86AudioLowerVolume", lazy.spawn(
            "pactl set-sink-volume @DEFAULT_SINK@ -5%")),
        Key([], "XF86AudioRaiseVolume", lazy.spawn(
            "pactl set-sink-volume @DEFAULT_SINK@ +5%"
        )),
        Key([], "XF86AudioMute", lazy.spawn(
            "pactl set-sink-mute @DEFAULT_SINK@ toggle"
        )),
        Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
        Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),
        
        #menu 
        Key([MOD], "d", lazy.spawn("rofi -show drun -show-icons -disable-history")),


]
