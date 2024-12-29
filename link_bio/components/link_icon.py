import reflex as rx
import link_bio.styles.styles as st
from link_bio.styles.colors import Color as Color

def link_icon(icon: str, url: str):
    return rx.link(
        rx.icon(
            tag = icon,
            color = Color.cont.value,
            _hover={"color": Color.snd.value},
        ),
        href = url,
        is_external = True,
    )

