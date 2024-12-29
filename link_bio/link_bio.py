import reflex as rx
from link_bio.components.navbar import navbar
from link_bio.components.footer import footer
from link_bio.views.header.header import header
from link_bio.views.links.links import links
from link_bio.views.bio.bio import bio
import link_bio.styles.styles as st



# class State(rx.State):
#     pass
    


def index():
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                links(),
                bio(),
                max_width = st.mx_width,
                width="100%",
                align="center",
                margin_y = st.Size.L.value,
                padding_x = st.Size.L.value,
            )
        ),
        footer(),
    )


app = rx.App(
    style=st.B_Style,
    head_components=[
        rx.el.link(
            rel="icon",
            href="/logo.jpg"
        ),
    ]
)
app.add_page(
    index,
    title="HAN St. - sitio oficial",
    description="Yo soy Nico y bienvenidos a HAN Street!!"
)
app._compile()
