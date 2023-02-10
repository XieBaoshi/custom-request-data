filename = "horde_generation.png"
api_key = "0000000000"
source_image = None
# You can fill these in to avoid putting them as args all the time
imgen_params = {
    "n": 1,
    "width": 64*8,
    "height":64*8,
    "steps": 25,
    "denoising_strength": 0.7,
    "sampler_name": "k_euler",
    "cfg_scale": 12,
    "karras": True,
    "hires_fix": True,
    # Uncomment the below line to pass a specific seed
    # "seed": "the little seed that could",
    # You can put extra SD webui params here if you wish
}
submit_dict = {
    # "prompt": "a swarm of incredibly cute stable robots, intricate, highly detailed, artstation, concept art, smooth, sharp focus, colorful scene,  in the style of don bluth, greg rutkowski, disney, and hans zatzka",
    "prompt": "masterpiece. a heroine with pleated skirt, jacket, thighhighs and necktie. pose, contrapposto, floating hair, perfectly shaped shapes, perfect body, cute, ArtStationHQ, pixiv, kodak portra fuji superia",
    "nsfw": True,
    "censor_nsfw": False,
    "trusted_workers": False,
    # Put the models you allow to fulfil your request in reverse order of priority. The last model in this list is the most likely to be chosen
    "models": [
        "ACertainThing",
        # "waifu_diffusion",
        # "Yiffy",
        # "trinart",
    ]
}
# Uncomment this line to try img2img
# Change the filename to your own image
# source_image = './db0.jpg'
# Uncomment these three lines to try inpainting. If the source_mask is not provided, the image sent has to have areas already erased-to-alpha
# source_image = './inpaint_original.png'
# source_processing = 'inpainting'
# source_mask = './inpaint_mask.png'
