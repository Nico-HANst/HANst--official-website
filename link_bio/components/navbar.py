import reflex as rx
from link_bio.styles.colors import Color as Color
import link_bio.styles.styles as st

def navbar():
    return rx.hstack(
        rx.image(
            src = "hanst.jpg",
            height = st.Size.L.value,
            width = "auto"
        ),
        position="sticky",
        bg = Color.nav.value,
        padding_x="16px",
        padding_y="6px",
        z_index="999",
        top="0"
    )