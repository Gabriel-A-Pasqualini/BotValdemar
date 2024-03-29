import asyncio
import os
from torch import autocast 
import torch
from diffusers import StableDiffusionPipeline
from huggingface_hub import hf_hub_url

SAVE_PATH = './img'
repo_type = 'model'
done = False

if not os.path.exists(SAVE_PATH):
    os.mkdir(SAVE_PATH)

def create(prompt):

    pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5", torch_dtype=torch.float16)
    pipe = pipe.to('cuda')

    with autocast('cuda'):          
        image = pipe(prompt).images[0]

    image_path = uniquify(os.path.join(SAVE_PATH,(prompt[:100]+'...') if len(prompt) > 100 else prompt) + '.png')
    image.save(image_path)


def uniquify(path):
    filename, extension = os.path.splitext(path)
    counter = 1

    while os.path.exists(path):
        path = filename + ' ('+str(counter)+')'+ extension 
        counter += 1

    return str(path).replace(' ', '_')
