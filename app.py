from fastcore.parallel import threaded
from fasthtml.common import *
import os, uvicorn, requests, replicate
from PIL import Image

app = FastHTML(live = True,hdrs=(picolink,))


replicate_api_token = os.environ['REPLICATE_API_KEY']
client = replicate.Client(api_token=replicate_api_token)  

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
    output= client.run(
         "xlabs-ai/flux-dev-controlnet:f2c31c31d81278a91b2447a304dae654c64a5d5a70340fba811bb1cbd41019a2",
          input={
        "steps": 28,
        "prompt": prompt,
        "lora_url": "",
        "control_type": "depth",
        "control_image": "https://replicate.delivery/pbxt/LUSNInCegT0XwStCCJjXOojSBhPjpk2Pzj5VNjksiP9cER8A/ComfyUI_02172_.png",
        "lora_strength": 1,
        "output_format": "webp",
        "guidance_scale": 2.5,
        "output_quality": 100,
        "negative_prompt": "low quality, ugly, distorted, artefacts",
        "control_strength": 0.45,
        "depth_preprocessor": "DepthAnything",
        "soft_edge_preprocessor": "HED",
        "image_to_image_strength": 0,
        "return_preprocessed_image": False
    })
    Image.open(requests.get(output[0], stream=True).raw).save(f"{folder}/{id}.png")
    return True
    
    
    
    if __name__ == '__main__': uvicorn.run("draft1:app", host='0.0.0.0', port=int(os.getenv("PORT", default=5000)))