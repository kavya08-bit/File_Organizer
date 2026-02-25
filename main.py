from pathlib import Path
import shutil
import logging
import argparse
 
class FileOrganiser:   # class

    File_Type = {      # types of file we can store
        "Images": [".jpg", ".jpeg", ".png", ".gif","webp"],
        "Documents": [".pdf", ".docx", ".txt"],
        "Videos": [".mp4", ".mov", ".avi"],
        "Audio": [".mp3", ".wav"],
        "Archives": [".zip", ".rar"]
    }

    def __init__(self, folder_path,dry_run=False,enable_logging=True, file_types=None):  # this is the constructor of the class
        self.folder = Path(folder_path)
        self.dry_run= dry_run
        self.file_types = file_types or self.File_Type
        if enable_logging:
            self._setup_logging()

    def _setup_logging(self): # this function creates the syntax of looging 
        logging.basicConfig(
            filename="organizer.log",
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s"
        )
        
    def organize_folder(self):      #this function is like main logic it compliers all the function 
        if not self.folder.exists():
            print("Folder does not exist.")
            self.logging.error("Folder does not exist.")
            return

        for file in self.folder.iterdir():
            if not file.is_file():
                continue

            try:                                        # using try & except for exception handling 
                extension = file.suffix.lower()
                category = None

                for folder_name,extensions in self.File_Type.items():
                    if extension in extensions:
                        category = folder_name
                        break
                if category is None:
                    category = "others"
                
                self.move_file(file,category)

            except Exception as e:
                logging.error(f"Error processing {file.name}: {e}")


    def move_file(self,file,category):        # this function moves the file from one folder to another folder
        destination = self.folder / category
        destination.mkdir(exist_ok=True)
        new_file_path = self.unique_name(destination,file.name)

        if self.dry_run:
            print(f"[DRY RUN] Would move {file.name} → {category}")
            logging.info(f"[DRY RUN] Would move {file.name} → {category}")
        else:
            shutil.move(str(file), str(new_file_path))
            print(f"Moved {file.name} → {category}")
            logging.info(f"Moved {file.name} → {category}")

    def unique_name(self ,destination,file_name):    # this function makes unquie name for files is same name file is allready present
        counter = 1
        new_path = destination / file_name

        while new_path.exists():
            name = new_path.stem
            suffix = new_path.suffix
            new_path = destination / f"{name}_{counter}{suffix}"
            counter +=1
        return new_path



# if __name__ == "__main__":
#     organiser= FileOrganiser("/home/spongebob/Desktop/File_Organizer/Example",
#     dry_run=False    #make dry run false for acutally running the program 
#     )
#     organiser.organize_folder()

if __name__ == "__main__":     #making CLI 

    parser = argparse.ArgumentParser(description="Smart File Organizer")

    parser.add_argument(
        "folder",
        help="Path to the folder you want to organize"
    )

    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview changes without moving files"
    )

    parser.add_argument(
        "--no-log",
        action="store_true",
        help="Disable logging"
    )

    args = parser.parse_args()

    organiser = FileOrganiser(
        folder_path=args.folder,
        dry_run=args.dry_run,
        enable_logging=not args.no_log
    )

    organiser.organize_folder()