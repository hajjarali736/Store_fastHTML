from fasthtml.common import *
from home_component import *
from fasthtml import ft
from jokegen import *


first_line = joke[0]
second_line = joke[1]

    

def nav_bar():
    return Header(Nav(A(Img(src="/assets/k.svg",alt="Joke generator",width='105',height='24'),href="/"),
                  A("About the Developer",hred="/",cls=f'bg-black text-white py-2 px-4 s-body rounded-[62.5rem] hover:bg-white/80 transition-colors duration-300 px-4 py-1 h-10 {center} justify-center',href="/about"),
                  cls=f'py-2 px-4 {between} items-center  w-full max-w-[400px]  backdrop-blur-lg rounded-full border-black/20 hover:bg-white/80 transition-colors duration-300'),
                  cls='nav'
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
                CheckboxX(value="Programming", hx_post="/add/programming", cls="custom-checkbox"), 
                cls="option-container"
            ),
            Div(
                P("dark", cls="option-text"), 
                CheckboxX(value="dark", hx_post="/add/dark", cls="custom-checkbox"), 
                cls="option-container"
            ),
            Div(
                P("pun", cls="option-text"), 
                CheckboxX(value="pun", hx_post="/add/pun", cls="custom-checkbox"), 
                cls="option-container"
            ),
            cls="selector",
            _id="counter"
        ),
        # Generate button with an id
        Button(
            "Generate",
            id="generate-btn",
            hx_post="/generate",
            hx_target="#joke-card",
            hx_swap="outerHTML"
        ),
        id="main-container",  # ID for the big Div
    ),  joke_card()
    
def joke_card():
    return Div(Div(P('The joke will be appear',id ="first_line",cls="joke-text",),
               P('Here',id ="joke-text",cls="joke-text",hx_target="#second_line",),
               id = "joke-card",cls="joke-card",),cls="centered-container")
    




hdrs = [ Meta(charset='UTF-8'),
    Meta(name='viewport', content='width=device-width, initial-scale=1.0, maximum-scale=1.0'),
     Link(href='/css/main.css', rel='stylesheet'),
    Link(href='tailwind.css', rel='stylesheet'),
        ]

#creating the app
app,rt = fast_app(live=True,
                  hdrs=hdrs,)



@rt("/")
def home():
    return Main(nav_bar(),select())
    # return Main()



@app.post("/add/{categorie}")
def add_cat(categorie:str):
    global categories
    
    if categorie in categories:
        categories.remove(categorie)
    else:
        if ('any' in categories): categories.remove('any')
        categories.append(categorie)
        
    if (len(categories) == 0): categories = ['any']
    print(categories)
    
@app.post("/generate")
def generate():
    global categories,first_line,second_line
    joke = asyncio.run(list_joke(categories))
    joke_card()
    first_line = joke[0]
    second_line = joke[1]
    print(joke)
    return Div(Div(Ul(ft.Li(f'{first_line}',id ="first_line",cls="joke-text",),
            ft.Li(f'{second_line}',id ="joke-text",cls="joke-text")),
            id = "joke-card",cls="joke-card",), cls="centered-container")
    
    





serve()