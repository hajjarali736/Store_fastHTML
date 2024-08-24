from fasthtml.common import *
from inspect import getsource
from jokeapi import Jokes # Import the Jokes class
from home_component import *
import asyncio

description = 'Modern joke generator'


def  navigation_bar():
    return Header(Nav(
        A(
            Img(src='/assets/k.svg', alt="jokes generator",width='105',height='24'),href="/"),
        A("About The Developer", href='/about', cls=f'bg-black text-white py-2 px-4 s-body rounded-[62.5rem] hover:bg-black/80 transition-colors duration-300 px-4 py-1 h-10 {center} justify-center'),
        cls=f'py-2 px-4 {between} items-center rounded-full w-full max-w-[400px] bg-yellow1 backdrop-blur-lg border border-white/20'
        ),cls=f'fixed top-0 w-full left-0 p-4 {center} justify-center z-50 bg-yellow1'
                  )
    
    



hdrs = [
    Meta(charset='UTF-8'),
    Meta(name='viewport', content='width=device-width, initial-scale=1.0, maximum-scale=1.0'),
    Meta(name='description', content=description),
    *Favicon('favicon.ico', 'favicon-dark.ico'),
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

app,rt = fast_app(hdrs=hdrs, default_hdrs=False,live = True)

joke = ()

@rt("/")
def home():
    return navigation_bar(),Title("Joke Generator")



@app.post("/genjoke")
def gen():
    global joke
    joke = asyncio.run(tuple_joke())
    return home()
    

        
        
        
    


serve()




    



