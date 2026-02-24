from pathlib import Path
import shutil

File_Type = {
    "Images": [".jpg", ".jpeg", ".png", ".gif","webp"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mov", ".avi"],
    "Audio": [".mp3", ".wav"],
    "Archives": [".zip", ".rar"]
}

def unique_name(destination,file_name):
    counter = 1
    new_path = destination / file_name

    while new_path.exists():
        name = new_path.stem
        suffix = new_path.suffix
        new_path = destination / f"{name}_{counter}{suffix}"
        counter +=1
    return new_path


def organize_folder(folder_path):
    folder = Path(folder_path)

    for file in folder.iterdir():
        if file.is_file():
            extension = file.suffix.lower()

            for folder_name,extensions in File_Type.items():
                if extension in extensions:
                    destination = folder / folder_name
                    destination.mkdir(exist_ok=True)
                    new_file_path = unique_name(destination,file.name)
                    shutil.move(str(file),str(new_file_path))
                    break


if __name__ == "__main__":
    organize_folder("/home/spongebob/Desktop/File_Organizer/Example")