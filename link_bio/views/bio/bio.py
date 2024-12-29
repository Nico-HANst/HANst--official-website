import reflex as rx
from link_bio.styles.colors import Color as Color
from link_bio.components.title import title
import link_bio.styles.styles as st

def bio():
    return rx.box(
        title("Mi historia con la programación"),
        
        rx.text(
            '''Tengo 17 años y hace ya 8 años empecé a meterme en el mundo de la programación!
        Entre mis 9 y 10 años descubrí estando en 4to grado de primaria lo que es Scratch.
        Allí comencé con cosas muy muy simples pero ya me era un paso gigante personalmente hablando para lo que quería ser de grande, PROGRAMADOR DE VIDEOJUEGOS.
        Para 6to grado ya había dominado Scratch y me sumé a una propuesta nueva en mi colegio (Jesús María), Robótica. Allí mejoré ampliamente mi manejo de la herramienta de Scracth y comencé a ver algo de Arduino para robots hechos con Mis Ladrillos.
        En 1er año del secundario me tocó experimentar la pandemia y en Informática vimos Scratch nuevamente. Allí no solo perfeccioné sino que también demostré mi capacidad.
        Ese año empecé a sentir que debía avanzar, allí aprendí lo básico de Batch.
        En 3er año, en Informática, aprendí HTML y empecé a sentirme atraído por el código escrito más que el de bloques y los resultados visuales como las posibilidades gráficas de la programación o hasta el diseño gréfico y el desarrollo web (aunque este se vería más adelante).
        4to año fue cuando empecé un curso de Python por mi cuenta incentivado por mi papá. En ese mismo año conseguí un gran dominio del lenguaje.
        En 5to, mientras mejoraba en Python, quise comenzar con Java y C#.
        C# no pude continuar por la capacidad de mi computadora que se quedaba corta. Java continué pero me encontré con la posibilidad del Java 3D y quise seguir por ese lado. Lamentablemente me frené con eso por tener que seguir un curso de Blender que aún no terminé pero si arranqué. Quise volver al Java común pero no contaba con la licencia de la página donde lo estaba viendo por ende también lo pausé.
        Ahora estoy finalizando 5to año y comencé a avocar Python al desarrollo web para empezar a explotar mi manejo del lenguaje y poder encontrar algún trabajito a mi edad.''',
            
            font_size = st.Size.M.value
        ),
        
        bg_color = Color.nav.value,
        margin_top = st.Size.Def.value,
        padding = st.Size.Def.value,
        border_radius = st.Size.L.value
    )
