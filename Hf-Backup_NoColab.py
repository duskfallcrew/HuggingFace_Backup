import os
import glob
import time
from pathlib import Path
from huggingface_hub import HfApi
from tqdm import tqdm

def format_size(size):
    """Formats a file size into a human-readable string."""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024
    return f"{size:.2f} TB"

def find_files(file_location, file_type):
    """Finds files matching the selected file type in the given directory."""
    try:
        files = sorted(
            glob.glob(os.path.join(file_location, f"*.{file_type}")),
            key=os.path.getmtime
        )
        return files
    except Exception as e:
        print(f"❌ Error finding files: {e}")
        return []

def upload_files(hfuser, hfrepo, file_location, file_type, commit_message, create_pr):
    """Uploads selected files to the Hugging Face repository."""
    if not hfuser or not hfrepo:
        print("❗ Please enter both your Organization/Username and Repository name.")
        return
    if not file_location:
      print("No directory was selected!")
      return
    files = find_files(file_location, file_type)
    if not files:
      print("📝 No files found matching your criteria. Check your file type and ensure files are in the location specified above.")
      return

    api = HfApi()
    repo_id = f"{hfuser}/{hfrepo}"
    print(f"🎯 Preparing to upload to: huggingface.co/{repo_id}")

    total_files = len(files)
    print(f"\n🚀 Starting upload of {total_files} file(s)...")
    # Create a progress bar for the overall upload
    with tqdm(total=total_files, desc="Total Progress", unit="file") as pbar:
        for idx, file in enumerate(files, 1):
            size = os.path.getsize(file)
            print(f"\n📦 Uploading file {idx}/{total_files}: {file} ({format_size(size)})")
            try:
                start_time = time.time()
                response = api.upload_file(
                  path_or_fileobj=file,
                  path_in_repo=os.path.basename(file),
                  repo_id=repo_id,
                  repo_type=None,
                  create_pr=create_pr,
                  commit_message=commit_message
                )
                duration = time.time() - start_time
                print(f"✅ Upload completed in {duration:.1f} seconds")
            except Exception as e:
              print(f"❌ Error uploading {file}: {e}")

            pbar.update(1)

    print("\n✨ All uploads complete!")
    if create_pr:
        print("🎉 Check your repository for the new Pull Request!")
    else:
      print("🎉 Files uploaded directly to your repository!")

if __name__ == "__main__":
    print("🌟 Hugging Face File Uploader - Standalone 🌟")

    hfuser = input("Enter your Hugging Face Username/Organization: ")
    hfrepo = input("Enter your Hugging Face Repository Name: ")
    file_type = input("Enter the file type to upload (e.g., safetensors, mp3, png): ")
    file_location = input("Enter the directory to search for files (e.g., /content/drive/MyDrive/MyModels, or /content/my_models): ")
    commit_message = input("Enter your commit message: ")
    create_pr_input = input("Create a Pull Request? (yes/no): ").lower()
    create_pr = create_pr_input == "yes"

    upload_files(hfuser, hfrepo, file_location, file_type, commit_message, create_pr)