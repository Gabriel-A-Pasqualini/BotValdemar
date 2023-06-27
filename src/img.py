import os
from torch import autocast 
import torch
from diffusers import StableDiffusionPipeline
from huggingface_hub import hf_hub_url

#SDV5_MODEL_PAH = os.getenv('SDV5_MODEL_PAH')


SAVE_PATH = os.path.join(os.environ['USERPROFILE'],'Desktop','SD_OUTPUT')
repo_type = 'model'
#prompt = input('Type: ')

if not os.path.exists(SAVE_PATH):
    os.mkdir(SAVE_PATH)


def uniquify(path):
    filename, extension = os.path.splitext(path)
    counter = 1

    while os.path.exists(path):
        path = filename + ' ('+str(counter)+')'+ extension 
        counter += 1

    return path

#print(f"Character in prompt: {len(prompt)}, limit 200")

def create(prompt):
    
    pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5", torch_dtype=torch.float16)
    pipe = pipe.to('cuda')

    with autocast('cuda'):
        image = pipe(prompt).images[0]

    image_path = uniquify(os.path.join(SAVE_PATH,(prompt[:25]+'...') if len(prompt) > 25 else prompt) + '.png')

    print(image_path)

    image.save(image_path)

