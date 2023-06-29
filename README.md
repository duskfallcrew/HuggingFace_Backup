

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

### ☢☢ **MAKE SURE:** ☢☢

You create a huggingface token, go to [this link](https://huggingface.co/settings/tokens), then `create new token` or copy available token with the `Write` role.

Instructions:

1. Run the first cell and paste your token into the prompt.  You can get your token from your [huggingface account page](https://huggingface.co/settings/tokens).
2. You'll need to note in "REPO" where you're uploading to - please go TO your model page or sorry your user page, create a new repo.  This means that unlike colab, where it can CREATE ONE - somehow on jupyter lab it's easier to just have one pre created.
3. At this stage it can only tolerate ONE type of file PER box, so safetensors for one, pt files for another etc (Three's three boxes)
4. make sure you change the HFUser to your username and your REPO to your name. It must exist, this one can't create it.
5. Cry when it's all completed

   WARNING: in. a proxy envioronment this may be slow.



-----------------
## CHANGES TO JUPYTER NOTEBOOK (NOT COLAB)
    
    1. Yoinked 90% of the code from EveryDream2Trainer
    2. Keeping Credit for Nocrypt because that's who made the original stuff.
    3. ATTEMPTING to get the requirements IN The notebook in case it legit cries
    4. Crawed into a hole nobody can find me now - *hiding under a rock*
    5. Cleared up how to work it, got it working on Vast and Runpod.

    
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
### ***Forked from - EVERYDREAM2 TRAINER - LYNN - AND NOCRYPT - Literally just yoinked it from this notebook:***
    
**https://colab.research.google.com/drive/1wEa-tS10h4LlDykd87TF5zzpXIIQoCmq** 
    
**https://github.com/victorchall/EveryDream2trainer**

-----------------

## Support? 

Earth and Dusk Discord because REASONS: https://discord.gg/5t2kYxt7An

Support my stupid lack of coding here: https://ko-fi.com/duskfallcrew

-----------------






