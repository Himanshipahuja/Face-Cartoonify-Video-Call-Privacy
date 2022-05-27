import os
import shutil
import torch
import cv2
import gradio as gr
from PIL import Image

# Download sample images
os.makedirs("sample_images", exist_ok=True)
os.chdir("sample_images")
os.system("gdown 1LiKfKhksfu8f_A4x-BhOjZgZHADdLdWz -O img1.jpg")
os.system("gdown 1jJ6uP_bpdnCRqCuiqZjJG8yeexsz6IUp -O img2.jpg")
os.system("gdown 1usp9c4VcTX2yche5o2WCi7yJw85n_yeZ -O img3.jpg")

os.chdir("../")


examples = [['sample_images/img1.jpg', "Cartoonify"],
            ['sample_images/img2.jpg', "Cartoonify"],
            ['sample_images/img3.jpg', "Cartoonify"],
            ]

inference_on = ['Full Resolution Image', 'Downsampled Image']

title = "Face Cartoonify for Video Call Privacy"
description = """
Gradio demo for <b>Face Cartoonify for Video Call Privacy</b>.\n 
"""

article = "<p style='text-align: center'><a href='#'> Face Cartoonify for Video Call Privacy </a> | <a href='#'>Github Repo</a></p>"

model = torch.hub.load(
    "AK391/animegan2-pytorch:main",
    "generator",
    pretrained=True,
    device="cpu",
    progress=False
)


face2paint = torch.hub.load(
    'AK391/animegan2-pytorch:main', 'face2paint', 
    size=512, device="cpu",side_by_side=False
)

def inference(img, method):
    if not os.path.exists('temp'):
      os.system('mkdir temp')
    
    img.save("temp/image.jpg", "JPEG")

    if method == "Cartoonify AnimeGanV2":
      out = face2paint(model, img)
      return out
    else:
      os.system("python cartoon.py --input_path 'temp/image.jpg'  --result_dir './temp/'")
      return 'temp/image.jpg'
    
gr.Interface(
    inference,
    [
        gr.inputs.Image(type="pil", label="Input"),
        gr.inputs.Radio(["Cartoonify OpenCV", "Cartoonify AnimeGanV2"], default="Cartoonify AnimeGanV2", label='Method'),

    ],
    gr.outputs.Image(type="file", label="Output"),
    title=title,
    description=description,
    article=article,
    theme ="huggingface",
    examples=examples,
    allow_flagging=False,
    ).launch()
    