import reflex as rx
from link_bio.components.link_button import link_button
from link_bio.components.title import title


def links():
    return rx.vstack(
        title("Mis proyectos"),
        link_button(
            "github",
            "GitHub",
            "Ver mis proyectos actuales.",
            "https://github.com/Nico-HANst"
        ),
        link_button(
            "computer",
            "SGames_Studio",
            "Proyectos hechos con Scratch - prototipos.",
            "https://scratch.mit.edu/users/SGames_Studio/"
        ),
        link_button(
            "code-xml",
            "Código de Esta Página",
            "Por si quieres consultar y aprender del código de esta página.",
            "https://github.com/Nico-HANst/Link-in-BIO"
        ),
        align="center",
        width="100%"
    )

