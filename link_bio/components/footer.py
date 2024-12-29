import reflex as rx
from link_bio.styles.colors import Color as Color
import link_bio.styles.styles as st

def footer():
    return rx.flex(
        rx.vstack(
            rx.box(
                rx.hstack(
                    rx.image(
                        src="logo.jpg",
                        height=st.Size.L.value,
                        width="auto"
                    ),
                    rx.text("Mail de contacto:"),
                    rx.link(
                        rx.text(
                            "nicoacole@gmail.com",
                            color = Color.hover.value,
                            _hover = {"color": Color.cont.value}
                        ),
                        href="mailto:nicoacole@gmail.com",
                        is_external = True,
                    )
                ),
                padding = "6px"
            ),
            align="center",
            width="100%",
            bottom = "0px"
        ),
        bg = Color.dark.value,
        z_index="999",
        bottom="0"

    )