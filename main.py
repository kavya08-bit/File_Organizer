from pathlib import Path
import shutil

class FileOrganiser:

    File_Type = {
        "Images": [".jpg", ".jpeg", ".png", ".gif","webp"],
        "Documents": [".pdf", ".docx", ".txt"],
        "Videos": [".mp4", ".mov", ".avi"],
        "Audio": [".mp3", ".wav"],
        "Archives": [".zip", ".rar"]
    }

    def __init__(self, folder_path, file_types=None):
        self.folder = Path(folder_path)
        self.file_types = file_types or self.File_Type


    def unique_name(self ,destination,file_name):
        counter = 1
        new_path = destination / file_name

        while new_path.exists():
            name = new_path.stem
            suffix = new_path.suffix
            new_path = destination / f"{name}_{counter}{suffix}"
            counter +=1
        return new_path


    def organize_folder(self):
        folder = self.folder

        for file in folder.iterdir():
            if file.is_file():
                extension = file.suffix.lower()

                for folder_name,extensions in self.File_Type.items():
                    if extension in extensions:
                        destination = folder / folder_name
                        destination.mkdir(exist_ok=True)
                        new_file_path = self.unique_name(destination,file.name)
                        shutil.move(str(file),str(new_file_path))
                        break


if __name__ == "__main__":
    organiser= FileOrganiser("/home/spongebob/Desktop/File_Organizer/Example")
    organiser.organize_folder()
