import reflex as rx
from enum import Enum
from .colors import Color as Color

# CONSTANTS
mx_width = "500px"

# SIZES
class Size(Enum):
    S = "0.5em"
    M = "0.8em"
    Def = "1em"
    L = "2em"

# STYLES

B_Style = {
    
    "background_color": Color.bg.value,
    "color": Color.snd.value,
    
    rx.button: {
        "width": "100%",
        "height": "100%",
        "padding": Size.S.value,
        "border_radius": Size.Def.value,
        "bg_color": Color.fst.value,
        "color": Color.nav.value,
        "justify_content": "start",
        "white_space": "normal",
        "text_align": "start",
        "_hover": {
            "background_color": Color.snd.value,
            "color": Color.hover.value
        }
    },
    
    rx.link: {
        "text_decoration": "none",
        "_hover": {}
    },
    
    
}


title_style = dict(
    width = "100%",
    padding_top = Size.Def.value,
    color = Color.cont.value
)


button_title_style = dict(
    font_size = Size.Def.value,
)

button_body_style = dict(
    font_size = Size.M.value,
)
