from fasthtml.common import *
from jokeapi import Jokes # Import the Jokes class
import asyncio

description = 'Modern joke generator'

hdrs = [
    Meta(charset='UTF-8'),
    Meta(name='viewport', content='width=device-width, initial-scale=1.0, maximum-scale=1.0'),
    Meta(name='description', content=description),
    *Favicon('favicon.ico', 'favicon-dark.ico'),
    *Socials(title='FastHTML',
        description=description,
        site_name='fastht.ml',
        twitter_site='@answerdotai',
        image=f'/assets/og-sq.png',
        url=''),
    # surrsrc,
    Script(src='https://cdn.jsdelivr.net/gh/gnat/surreal@main/surreal.js'),
    scopesrc,
    Link(href='css/main.css', rel='stylesheet'),
    Link(href='css/tailwind.css', rel='stylesheet'),
    Link(href='css/stack.css', rel='stylesheet'),
    Link(href='css/preview-stack.css', rel='stylesheet'),
    Link(href='css/highlighter-theme.css', rel='stylesheet')]



def listing(t):
    k = ""
    for i in t:
        k+=i 
        k+= "\n"
    return t

async def tuple_joke():
    j = await Jokes()  # Initialise the class
    joke = await j.get_joke(category=['Dark'])  # Retrieve a random joke
    if joke["type"] == "single": # Print the joke
        return (joke["joke"])
    else:
        return(joke["setup"] ,joke["delivery"])

app = FastHTML(live = True)

joke = ()

@app.get("/")
def home():
    return Title("Joke Generator"),Main(Button("generate joke", hx_post="/genjoke"),
                                        Div(P(listing(joke))))


@app.post("/genjoke")
def gen():
    global joke
    joke = asyncio.run(tuple_joke())
    return home()
    

        
        
        
    


serve()




    



