from fastcore.parallel import threaded
from fasthtml.common import *
import os, uvicorn, requests, replicate
from PIL import Image


app = FastHTML(live = True,hdrs=(picolink,))


rak = os.environ['REPLICATE_API_KEY']
client = replicate.Client(api_token=rak)  

generations = []
folder = f"gens/"
os.makedirs(folder, exist_ok=True)



@app.get("/")
def home():
    inp = Input(id="new-prompt", name = "prompt", placeholder = "Enter a prompt: ")
    add = Form(Group(inp,Button("Generate")),hx_post="/",target_id='gen-list', hx_swap="afterbegin")
    gen_list = Div(id = 'gen-list')
    return Title("Image generator"), Main(H1('Text to Image generator'),add , gen_list, cls="container")


def gen_preview(id):
    if os.path.exists(f"gens/{id}.png"):
        return Div(Img(src= f"gens/{id}.png",id = f"gen-{id}"))
    else:
        return Div("Generating...", id = f"gen-{id}", hx_post=f"generations/{id}", hx_trigger="every 1s", hx_swap="outerHTML")
    

@app.post("/generation/{id}")
def get(id:int): return gen_preview(id)


@app.get("/{filename:path}.{ext:static}")
def static(fname:str,ext:str): return FileResponse(f"{fname}.{ext}")
serve()
    
@app.post("/")
def post(prompt:str):
    id = len(generations)
    generate_and_save(prompt,id)
    generations.append(prompt)
    clear_input =  Input(id="new-prompt", name="prompt", placeholder="Enter a prompt", hx_swap_oob='true')
    return gen_preview(id),clear_input

@threaded
def generate_and_save(prompt,id):
    output = replicate.run(
        "black-forest-labs/flux-schnell",
        input={
            "prompt": prompt,
            "num_outputs": 1,
            "aspect_ratio": "1:1",
            "output_format": "webp",
            "output_quality": 80
        }
    )
    Image.open(requests.get(output[0], stream=True).raw).save(f"{folder}/{id}.png")
    return True
    
    
    
    if __name__ == '__main__': uvicorn.run("draft1:app", host='0.0.0.0', port=int(os.getenv("PORT", default=5000)))
    
    
serve()