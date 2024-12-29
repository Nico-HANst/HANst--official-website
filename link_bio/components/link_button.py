import reflex as rx
import link_bio.styles.styles as st


def link_button(icon: str, title: str, body: str, url: str):
    return rx.link(
        rx.button(
            rx.hstack(
                rx.icon(
                    tag=icon,
                    width = st.Size.L.value,
                    height = st.Size.L.value,
                    margin = st.Size.S.value
                ),
                rx.vstack(
                    rx.text(title, style = st.button_title_style),
                    rx.text(body, style = st.button_body_style),
                    row_gap = "0px",
                    margin_x = st.Size.S.value
                ),
                column_gap = "0px"
            )
        ),
        href=url,
        is_external=True,
        width="100%"
    )

