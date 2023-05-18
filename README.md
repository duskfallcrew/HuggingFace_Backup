# HuggingFace_Backup
A colab notebook to be able to upload backups of files like Stable Diffusion models, code repos or otherwise. May need tweaking a little in future but I don't code so this is funny. 

# Hugging Face Backup - Upload your junk from Google Drive
*Quickly upload stuff like merged models to huggingface*

Run cell `1,2,3`

You only need to choose one between `3.1,3.2,and 3.3`

<small>Forked from LYNN - AND NOCRYPT - Literally just yoinked it from this notebook: https://colab.research.google.com/drive/1wEa-tS10h4LlDykd87TF5zzpXIIQoCmq

WE TAKE NO CREDIT ON THIS. FOLLOW NOCRYPTS STUFF HERE: 

[![](https://dcbadge.vercel.app/api/shield/442099748669751297?style=flat)](https://lookup.guru/442099748669751297) [![ko-fi](https://img.shields.io/badge/Ko--fi-F16061?logo=ko-fi&logoColor=white&style=flat)](https://ko-fi.com/nocrypt) [![ko-fi](https://img.shields.io/badge/Patreon-F1465A?logo=patreon&logoColor=white&style=flat)](https://patreon.com/nocrypt) 


<small> You can find updates on NoCrypt's toys: https://discord.gg/touhouai

<small> Earth & Dusk Discord because REASONS: https://discord.gg/5t2kYxt7An
  
 ## WAIT! Just a warning of things you'll need to be able to change when you use this notebook: 
  ## How to set up the files

What you need to NOW sadly is just replace certain "code" or locations with the locations of where you need to back up to your folder. 

### Double click on the `UPLOAD VIA HUGGINGFACE` section and see the following section:
paths_map 
    
    `Models`  /content/sdw/models/Stable-diffusion
    
    `VAEs`  /content/sdw/models/VAE
    
    `LORAs`  /content/sdw/models/Lora
    
    `Embeddings`  /content/sdw/embeddings
   
    `Hypernetworks`  /content/sdw/models/hypernetworks


You will need to change the `MODELS` section or any of the above sections to whatever folder you're looking to back up.  It's easy as just looking on the side file browser, scrolling through and copying the path of the folder in question. 

Example: `/content/drive/MyDrive/cagliostro-colab-ui` may be your content folder you're looking for, just copy the path and paste it to one of the above sections.


<small> Sadly I don't code. So there's no easier way of doing this LOL. 

### Also Note! 

Make sure you `MOUNT` your google drive (I have stated this is optional, as some people may use command line to upload), I've patched in `Imjoy-Elfinder` for kicks. - Visual people like this, I know I do.

### MAKE SURE: 

You create a huggingface token, go to [this link](https://huggingface.co/settings/tokens), then `create new token` or copy available token with the `Write` role.

## Head off to use this colab here: https://github.com/kieranxsomer/HuggingFace_Backup/blob/main/HuggingFace_Backup.ipynb
