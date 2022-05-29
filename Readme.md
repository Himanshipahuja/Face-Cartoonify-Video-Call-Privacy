# Face Cartoonify using AnimeGANV2 and OpenCV

<img width="1298" alt="Screenshot 2022-05-29 at 6 20 21 PM" src="https://user-images.githubusercontent.com/72742160/170869467-cbc561d0-3a85-490f-a541-d9d41ac399ea.png">


## News

- **April 27, 2022:** Integrated into [Huggingface Spaces 🤗](https://huggingface.co/spaces) using [Gradio](https://github.com/gradio-app/gradio). Try out the web demo: [![Hugging Face Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://huggingface.co/spaces/Himanshi/Face-Cartoonify-for-Video-Call-Privacy)

## Motivation

Taking insipiration from work done by [Bryan Pratte](https://www.linkedin.com/in/bryanpratte/) by creating [Hallway](https://joinhallway.com/) a fun way to stream yourself with a digital avatars on any video conferencing tools.

Hallway provides users option to interact with others while preserving their **original identity**.

## Idea

Following the footsteps of the Bryan, I tried to create a similar experience with a **digital avatar** using 2 separate methods.

I tried to use the *OpenCV* and [AnimeGANv2](https://tachibanayoshino.github.io/AnimeGANv2/) to create a **face cartoon**.

I started off using OpenCV to cartoonify the faces but I faced problems such as it was far away from being realistic and it was not well optimized as well.

<img width="1318" alt="Screenshot 2022-05-29 at 6 15 53 PM" src="https://user-images.githubusercontent.com/72742160/170869353-6af87fed-5fad-4061-9360-939ffb7e7012.png">

I used *AnimeGANv2* in this project as it prevents the generation of high-frequency artifacts by simply changing the normalization of features in the network. In addition, we further reduce the scale of the generator network to achieve more efficient animation style transfer. *AnimeGANv2* trained on the newly established high-quality dataset can generate animation images with better visual quality than *OpenCV*.

<img width="1293" alt="Screenshot 2022-05-29 at 6 15 31 PM" src="https://user-images.githubusercontent.com/72742160/170869368-86d47e03-21f2-43e6-aa77-58a9158baa35.png">


## Future Work

This project is still in early stages. I am working on adding more features and improving the performance. Eventually, I would like to create an SDK where 3rd party apps like social media apps, etc can use this SDK to easily integrate image cartoonification as filter into their applications

## How to Start

- Fork and clone the repository using:

    ```
    git clone https://github.com/Himanshipahuja/Face-Cartoonify-Video-Call-Privacy
    ```

- Create virual enviornment:

    ```
    conda create -n cartoonify python=3.10
    conda activate cartoonify
    ```

- Install dependencies:

    ```
    pip install -r requirements.txt
    ```

- Goto project directory:

    ```
    cd Face-Cartoonify-Video
    ```

- Start the project:

    ```
    python app.py
    ```

- Click on the localhost server link to start with the Gradio App.
