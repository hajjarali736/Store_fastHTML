from fasthtml.common import *

app = FastHTML(live= True)

@app.get("/")
def home():
    return H1("hello"),Img(src='assets/k.svg')



serve()