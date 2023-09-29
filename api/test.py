from auth_token import auth_token
import torch
from torch import autocast
from diffusers import StableDiffusionPipeline

device = "cuda"
model_id = "waifu-diffusion/"
pipe = StableDiffusionPipeline.from_pretrained(model_id, revision="fp16", torch_dtype=torch.float16, use_safetensors=True)
pipe.to(device)

prompt = "cute, long hair, blonde, school girl"
# pipe.enable_sequential_cpu_offload()
# pipe.enable_vae_slicing()
# pipe.enable_model_cpu_offload()
with autocast(device): 
    image = pipe(prompt, height=256, width=256).images[0]


image.save("astronaut.jpg")