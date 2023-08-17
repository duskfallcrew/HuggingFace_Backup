

<a target="_blank" href="https://colab.research.google.com/github/kieranxsomer/HuggingFace_Backup/blob/main/HuggingFace_Backup.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>

![Discord](https://img.shields.io/discord/1024442483750490222?label=Earth%26Dusk&style=plastic)

If you've copied this to drive and it's no longer working check here: https://github.com/kieranxsomer/HuggingFace_Backup
-----------------
# **Hugging Face Backup**
<small> An extremely weird fork of content from Nocrypt's notebook, and as well as EveryDream2Trainer for JupyterLabs by a DID system that has no clue how to code. We'd call it opinionated! This is MISSING google stuff, we want to MAYBE add ocalmfuse to it eventually, it is NOW missing EMJOY finder because it's useless in a jupyter environment. (It is! LOL you can easy find stuff otherwise!)  BOTH VERSIONS will work on Colab, but Jupyter only works on NON google instances. Jupyter version won't connect to your google drive - it'll only connect to a certain folder.  I'm working on things, I don't know how to program *CRIES*. 

*Quickly upload stuff like merged models to huggingface*

-----------------

## ♦♦ **JUPYTER NOTEBOOK INSTRUCTIONS (NOT COLAB)** ♦♦

###  **HUGGING FACE HUB BACKUP** 

This. now works at RUNPOD AND VAST, and due to the patching should work with all file types, but see box 3 for what file types are suggested. 

WARNING: 
Make sure if you're using VAST, do not use "JUPYTER LABS" direct - use Jupyter PROXY.
Runpod doesn't give you an option between them, so this should be fine.

Currently on labs we get a "NO MODULE FOUND" for a bunch of conflicts that VENV isn't fixable with until we look into it. 

### ☢☢ **MAKE SURE:** ☢☢

You create a huggingface token, go to [this link](https://huggingface.co/settings/tokens), then `create new token` or copy available token with the `Write` role.

Instructions:

1. Run the first cell and paste your token into the prompt.  You can get your token from your [huggingface account page](https://huggingface.co/settings/tokens).
2. You'll need to note in "REPO" where you're uploading to   
3. At this stage it can only tolerate ONE type of file PER box, so safetensors for one, pt files for another etc (Three's three boxes)
4. make sure you change the HFUser to your username
5. Change your REPO to your repo name. It must exist, this one can't create it.
6. Cry when it's all completed

   WARNING: in. a proxy envioronment this may be slow.
    
-----------------
## ♦♦ **COLAB INSTRUCTIONS** ♦♦

### ✅ **Mount Drive!**
This is extremely optional, but y'know if you need it! 

### ✅ **Imjoy-Elfinder**

An optional file viewer that may give you a more visual way of looking at your files. Also good if you need to upload files instead of using terminal or gdrive. 

###  ✅ **Hugging Face Hub Options**

☢☢ **How to use this colab** ☢☢

Scream, because i couldn't get "THE FUN WAY" To work.
Which is OK,  because the "MANUAL" way is faster. 
There is no need to actually fix code, or anything just copy and paste your details as instructed. 

☢☢ **MAKE SURE:** ☢☢

You create a huggingface token, go to [this link](https://huggingface.co/settings/tokens), then `create new token` or copy available token with the `Write` role.

🔼 Run cell `1,2,3`

You only need to choose one between `3.2,and 3.3`

Note 3.1 was yoinked because right now I don't know how to patch it to work outside of a stable diffusion instance.  If you're using a free colab, try not to use the File Finder - as that's probably considerd a "REMOTE UI"

Make sure you `MOUNT` your google drive, I've patched in `Imjoy-Elfinder` for kicks. - Visual people like this, I know I do.


-----------------

## Support? 

Earth and Dusk Discord because REASONS: https://discord.gg/5t2kYxt7An

Support my stupid lack of coding here: https://ko-fi.com/duskfallcrew

Find our models here: https://civitai.com/user/duskfallcrew


![Discord](https://img.shields.io/discord/1024442483750490222?label=Earth%26Dusk&style=plastic) [![ko-fi](https://img.shields.io/badge/Ko--fi-F16061?logo=ko-fi&logoColor=white&style=flat)](https://ko-fi.com/duskfallcrew)


-----------------
### CHANGES SECTION AND CREDITS BELOW

-----------------
## CHANGES TO JUPYTER NOTEBOOK (NOT COLAB)
    
    1. Yoinked 90% of the code from EveryDream2Trainer
    2. Keeping Credit for Nocrypt because that's who made the original stuff.
    3. ATTEMPTING to get the requirements IN The notebook in case it legit cries
    4. Crawed into a hole nobody can find me now - *hiding under a rock*
    5. Cleared up how to work it, got it working on Vast and Runpod.   

-----------------
## ***Forked from - EVERYDREAM2 TRAINER - LYNN - AND NOCRYPT - Literally just yoinked it from this notebook:***

Credtis for original codes for Colab - NOCRYPT
[![](https://dcbadge.vercel.app/api/shield/442099748669751297?style=flat)](https://lookup.guru/442099748669751297) [![ko-fi](https://img.shields.io/badge/Ko--fi-F16061?logo=ko-fi&logoColor=white&style=flat)](https://ko-fi.com/nocrypt) [![ko-fi](https://img.shields.io/badge/Patreon-F1465A?logo=patreon&logoColor=white&style=flat)](https://patreon.com/nocrypt) 

Open the SD Colab here: 
<a target="_blank" href="https://colab.research.google.com/drive/1wEa-tS10h4LlDykd87TF5zzpXIIQoCmq">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>

-----

Jupyter/EveryDream:
**https://github.com/victorchall/EveryDream2trainer**


If you've copied this to drive and it's no longer working check here: https://github.com/kieranxsomer/HuggingFace_Backup


WIP: May see if we can patch the other version from jupyter as an extension in the colab version later on.


