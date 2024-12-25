# 🚀 Hugging Face Uploader Notebook

This notebook provides a user-friendly tool for uploading files directly to your Hugging Face repositories. It's designed to streamline your workflow and make sharing your models and data easier.
Coded with help from ![Google Gemini](https://img.shields.io/badge/google%20gemini-8E75B2?style=for-the-badge&logo=google%20gemini&logoColor=white) and mostly in ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
------
**📦 Colab Users:**

 <a target="_blank" href="https://colab.research.google.com/github/duskfallcrew/HuggingFace_Backup/blob/Huggingface_Backup/HuggingFace_Backup_2024_Colab.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a> <br/>

------

**🔑 Initial Setup (One Time Only)**

1.  **Authenticate:**
    *   Run the `notebook_login()` cell *once* to securely store your Hugging Face API token.
    *   **Important:** For security, avoid sharing your notebook file or system state after you have run `notebook_login()`. Do not commit your notebook file to a shared repository, as this could expose your API token.

**🗂️ Using the Uploader**

1.  **Repository Details:**
    *   Enter your Hugging Face Organization or Username in the "Owner" field.
    *   Enter your repository name in the "Repo" field.

2.  **Directory Selection:**
    *   Enter a directory path where your files are located.
    *   Select the 'Update Dir' button to set that path.

3.  **File Selection:**
    *   Select the appropriate file type from the dropdown menu.
    *   Select the files you want to upload from the list. You can sort them by name or date modified.

4.  **Commit Message (Optional):**
    *   Add a commit message to your upload, or use the default message.

5.  **Upload Options:**
    *   Choose whether to create a pull request or upload directly to the main branch.
    *   Select whether to clear the output after a successful upload.

6.  **Start Upload:**
    *   Click the "⬆️ Upload" button.

**💡 Important Notes**

*   **Direct Uploads:** This uploader uses the Hugging Face API for direct file uploads, bypassing the need for traditional Git operations for core functionality.
*   **Git LFS:** Most users will not need to interact with Git or Git LFS. If you need to clone or push changes to a repository *outside this notebook*, it requires a separate Git credential setup (e.g., your operating system's credential manager or SSH keys). This credential is separate from the API token used in the uploader, and should not be stored in this notebook.
*   **Troubleshooting:** If you encounter any issues, please review the steps or double-check that you have write access to the repository, and that your API token has the correct scope of access.

**📣 Updates & Community**

*   This tool will continue to be updated.
*   For the latest patches, fixes, and community contributions, visit [https://github.com/duskfallcrew/HuggingFace_Backup](https://github.com/duskfallcrew/HuggingFace_Backup)

We hope this notebook makes your Hugging Face uploads easier! If you have any questions or suggestions, please reach out.

<br/>

## 🌈 About Us

Heya! We're a vibrant system of 300+ alters, proudly rocking life with DID, ADHD, Autism, and CPTSD. We believe AI can be a game-changer for mental health and creativity, and we're here to explore that potential together!

<br/>

### 🤝 Let's Connect!

*   🏠 [End Media](https://www.end-media.org/)
*   🎮 [Discord Community](https://discord.gg/5t2kYxt7An)
*   🤗 [HuggingFace Space](https://huggingface.co/EarthnDusk)
*   🎵 [YouTube](https://www.youtube.com/channel/UCk7MGP7nrJz5awBSP75xmVw)
*   🎨 [DeviantArt Group](https://www.deviantart.com/diffusionai)
*   🎪 [Subreddit](https://www.reddit.com/r/earthndusk/)

<br/>

### ☕ Support Our Adventures

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/Z8Z8L4EO)

<br/>

## 🏴‍☠️ Proudly Supported By

*   [Pirate Diffusion](https://www.piratediffusion.com/)
*   [Yodayo](https://yodayo.com/)

<br/>

## 🛠️ Need Help?

Found a bug? We've got multiple ways to help:

*   GitHub PR & Bug tracker
*   CivitAi DM/comments
*   Earth & Dusk Discord

<br/>

## 💝 Credits & Origins

Big thanks to our code ancestors:

*   EVERYDREAM2 TRAINER [https://github.com/victorchall/EveryDream2trainer](https://github.com/victorchall/EveryDream2trainer)
*   LINAQRUF
*   NOCRYPT [![](https://dcbadge.vercel.app/api/shield/442099748669751297?style=flat)](https://lookup.guru/442099748669751297)

Try the original SD Colab:

<a target="_blank" href="https://colab.research.google.com/drive/1wEa-tS10h4LlDykd87TF5zzpXIIQoCmq">
<img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>

<br/>

## 📝 Changelog: Our Journey So Far

1.  🔧 Added EveryDream2Trainer's Python widget magic
2.  🌟 Kept Nocrypt's awesome contributions front and center
3.  📦 Packed all the essentials into one Jupyter notebook
4.  🤓 Made friends with proper file extensions (*.safetensors)
5.  📝 Wrote instructions in human-friendly language
6.  🤖 Got GPT to help make things clearer
7.  🎨 Prettied up the Jupyter edition
8.  🔄 Synced up Colab and Jupyter versions
9.  🧹 Cleaned up dependencies (bye-bye, unnecessary transformers!)
10. ✨ Added some extra folder upload superpowers
11. Cleaned up Colab & Updated Colab
12. Added more concise features to the widgets-Colab is working again.
13. Gemini overhaul
14. Added more file types to Colab, streamlined the instructions
    
Remember: We're not pro programmers, and that's totally okay! If you see something that could be better, pull requests are always welcome! 🎉
