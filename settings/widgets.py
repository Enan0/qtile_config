from libqtile import widget
from settings.theme import colors


base = lambda fg='text', bg='dark' : {
        'foreground': colors[fg],
        'background': colors[bg]
}

separator = lambda: widget.Sep(**base(), linewidth=0, padding=5)

icon = lambda fg='text', bg='dark', fontsize=16, text="?": widget.TextBox(
    **base(fg,bg),
    fontsize=fontsize,
    text=text,
    padding=3
)


powerline = lambda fg="light", bg="dark": widget.TextBox(
    **base(fg,bg),
    fontsize=37,
    text="",
    padding=-2
)

workspaces = lambda: [
    separator(),
    widget.GroupBox(
        **base(fg='light'),
        font='CodeNewRoman Nerd Font',
        fontsize=19,
        margin_y=3,
        margin_x=0,
        padding_y=8,
        padding_x=5,
        borderwidth=1,
        active=colors['active'],
        inactive=colors['inactive'],
        rounded=False,
        highlight_method='block',
        urgent_alert_method='block',
        urgent_border=colors['urgent'],
        this_current_screen_border=colors['focus'],
        this_screen_border=colors['grey'],
        other_current_screen_border=colors['dark'],
        other_screen_border=colors['dark'],
        disable_drag=True
    ),
    separator(),
    widget.WindowName(**base(fg='focus'), fontsize=14, padding=5),
    separator(),
]


primary_widgets = [
        *workspaces(),

        separator(),

        powerline('color4', 'dark'),
        
        icon(bg="color4", text=""),

        powerline('color3','color4'),

        icon(bg='color3', text=''),

        widget.Net(**base(bg='color3'), interface='wlp2s0'),

        powerline('color2','color3'),

        widget.CurrentLayoutIcon(**base(bg='color2'), scale=0.65),
        
        widget.CurrentLayout(**base(bg='color2'), padding=5),

        powerline('color1','color2'),

        icon(bg='color1', fontsize=17, text=""),

        widget.Clock(**base(bg='color1'), format='%d/%m/%Y - %H:%M'),


        widget.Systray(background=colors['dark'], padding=5),
        powerline('dark','color1'),
        widget.Battery(background=colors['dark'],foreground=colors['light'], format='{percent:2.0%} {char}', full_char="", charge_char="", discharge_char="", low_foreground=colors['urgent'], low_percentage=5, padding=5)
]


secondary_widgets = [
        *workspaces(),

        separator(),

        powerline("color1","dark"),

        widget.CurrentLayoutIcon(**base(bg='color1'), scale=0.65),

        widget.CurrentLayout(**base(bg='color1'), padding=5),
]


widget_defaults = {
        'font': 'CodeNewRoman Nerd Font Bold',
        "fontsize": 14,
        "padding": 1,
}

extension_defaults = widget_defaults.copy()
