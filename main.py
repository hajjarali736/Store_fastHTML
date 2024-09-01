from fasthtml.common import *
from home_component import *
from fasthtml import ft
from jokegen import  *


# Define global variables for joke content for faster response
first_line, second_line = joke[0], joke[1]

#defining HTML component
def nav_bar():
    return Header(
        Nav(
            A(
                Img(
                    src="/assets/k.svg", alt="Joke generator", width="105", height="24"
                ),
                href="/",
            ),
            A("About the Developer", hred="/", cls="about_home", href="/about"),
            cls=f"bar",
        ),
        cls="nav",
    )


def select():
    return Div(
        # Title section aligned to the left
        Div(
            P("Choose a category:", id="choose-text"),
            id="title-container",
        ),
        # Centered options
        Ul(
            Div(
                P("Programming", cls="option-text"),
                CheckboxX(
                    value="Programming",
                    hx_post="/add/programming",
                    cls="custom-checkbox",
                ),
                cls="option-container",
            ),
            Div(
                P("miscellaneous", cls="option-text"),
                CheckboxX(value="Misc", hx_post="/add/Misc",
                          cls="custom-checkbox"),
                cls="option-container",
            ),
            Div(
                P("pun", cls="option-text"),
                CheckboxX(value="pun", hx_post="/add/pun",
                          cls="custom-checkbox"),
                cls="option-container",
            ),
            cls="selector",
            _id="counter",
        ),
        # Generate button with an id
        Button(
            "Generate",
            id="generate-btn",
            hx_post="/generate",
            hx_target="#joke-card",
            hx_swap="outerHTML",
        ),
        id="select-container",  # ID for the big Div
    ), joke_card()


def joke_card():
    return Div(
        Div(
            P(
                "The joke will be appear",
                id="first_line",
                cls="joke-text",
            ),
            P(
                "Here",
                id="joke-text",
                cls="joke-text",
                hx_target="#second_line",
            ),
            id="joke-card",
            cls="joke-card",
        ),
        cls="centered-container",
    )


# Initialize the FastHTML application with headers
hdrs = [
    Meta(charset="UTF-8"),
    Meta(
        name="viewport",
        content="width=device-width, initial-scale=1.0, maximum-scale=1.0",
    ),
    Link(href="/css/main.css", rel="stylesheet"),
]

# creating the app
app, rt = fast_app(
    live=True,
    hdrs=hdrs,
)

# Define route handlers


@rt("/")
def home():
    return Main(nav_bar(), select())


@app.post("/add/{categorie}")
def add_cat(categorie: str):
    global categories

    if categorie in categories:
        categories.remove(categorie)
    else:
        if "any" in categories:
            categories.remove("any")
        categories.append(categorie)

    if len(categories) == 0:
        categories = ["any"]
    print(categories)


@app.post("/generate")
def generate():
    global categories, first_line, second_line
    joke = asyncio.run(list_joke(categories))
    joke_card()
    first_line = joke[0]
    second_line = joke[1]
    return Div(
        Div(
            Ul(
                ft.Li(
                    f"{first_line}",
                    id="first_line",
                    cls="joke-text",
                ),
                ft.Li(f"{second_line}", id="joke-text", cls="joke-text"),
            ),
            id="joke-card",
            cls="joke-card",
        ),
        cls="centered-container",
    )


@rt("/about")
def about():
    return Main(
        Header(
            Nav(
                A(
                    Img(
                        src="/assets/k.svg",
                        alt="Joke generator",
                        width="105",
                        height="24",
                    ),
                    href="/",
                ),
                A("Home", href="/", cls="about_home"),
                cls="bar",
            ),
            cls="nav",
        ),
        Div(
            H2("About Me", cls="about-title"),
            Div(
                P(
                    "Hello! I am Ali Zaghlan El Hajjar, a dedicated computer science student at the Lebanese American University with a deep passion for technology and software engineering. 👨🏽‍💻",
                    cls="about-text",
                ),
                P(
                    "I am currently exploring the FastHTML framework—a cutting-edge, Python-based tool designed for building modern, efficient web applications. Through this dynamic web app, I am rigorously testing the framework's capabilities, including its dynamicity and API integration, all while keeping the process simple and effective. 🚀✨",
                    cls="about-text",
                    style="margin-top: 3rem;",
                ),
                P(
                    "Feel free to connect with me on ",
                    A(
                        "LinkedIn",
                        href="https://www.linkedin.com/in/allielhajjar/",
                        cls="linkedin-link",
                    ),
                    " and explore more about my projects and interests.",
                    cls="about-text",
                    style="margin-top: 3rem;",
                ),
                cls="about-content",
            ),
            id="about-container",
            cls="center-about-container",
        ),
    )


# Start the server to listen for requests
serve()
