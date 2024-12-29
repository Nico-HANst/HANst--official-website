import reflex as rx
import link_bio.styles.styles as st
from link_bio.components.link_icon import link_icon
from link_bio.styles.colors import Color as Color



def header():
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                name="HAN St.",
                src="logo.jpg",
                fallback="HS",
                size="8",
                radius="full",
                border="solid",
                border_color = Color.nav.value,
                padding = st.Size.S.value,
                bg_color = "#040404"
            ),
            rx.box(
                rx.vstack(
                    rx.heading(
                        "NICOLÁS HUGO ADIB",
                        color = Color.fst.value,
                    ),
                    rx.text(
                        "aka - HAN St.",
                        color = Color.hover.value,
                    ),
                    rx.hstack(
                        link_icon(
                            "youtube",
                            "https://www.youtube.com/@Nico-HANst"
                        ),
                    ),
                    row_gap = st.Size.S.value,
                ),
                margin_y = st.Size.Def.value
            )
        ),
        align_items="start"
    )
