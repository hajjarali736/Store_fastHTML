from fasthtml.common import *
from home_component import *

def nav_bar():
    return Header(Nav(A(Img(src="/assets/k.svg",alt="Joke generator",width='105',height='24'),href="/"),
                  A("About the Developer",hred="/",cls=f'bg-black text-white py-2 px-4 s-body rounded-[62.5rem] hover:bg-white/80 transition-colors duration-300 px-4 py-1 h-10 {center} justify-center'),
                  cls=f'py-2 px-4 {between} items-center  w-full max-w-[400px]  backdrop-blur-lg rounded-full border-white/20 hover:bg-white/80 transition-colors duration-300'),
                  cls=f'fixed top-0 w-full left-0 p-4 {center} justify-center z-50 bg-yellow'
    )

hdrs = [ Meta(charset='UTF-8'),
    Meta(name='viewport', content='width=device-width, initial-scale=1.0, maximum-scale=1.0'),
    Link(href='css/tailwind.css', rel='stylesheet'),
    Link(href='css/main.css', rel='stylesheet'),
        ]

#creating the app
app,rt = fast_app(live=True, hdrs=hdrs)

@rt("/")
def home():
    return nav_bar()




serve()