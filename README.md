📂 Smart File Organizer (Python CLI Tool)

Organize your files automatically using a clean, command-line based Python tool.
This project sorts files into folders based on their extensions and includes production-style features like dry-run mode, structured logging, and duplicate handling.

✨ Features

📁 Organizes files by extension

🛑 Dry-run mode (preview changes safely)
📝 Structured logging (organizer.log)
🔁 Automatic duplicate filename handling
💻 CLI support using argparse
🧱 Clean OOP architecture
⚠ Exception handling for stability

🛠 Tech Stack

1.Python 3             
2.pathlib              
3.shutil               
4.argparse           
5.logging            

📦 Project Structure
File_Organizer/          
│                  
├── main.py                
├── README.md           
├── .gitignore               
└── organizer.log (auto-generated)

⚙️ Installation:-

Clone the repository:

git clone https://github.com/your-username/File_Organizer.git

cd File_Organizer

Create a virtual environment:

python -m venv venv

source venv/bin/activate      # Linux / Mac                          
venv\Scripts\activate         # Windows

▶️ Usage:-

🔹 Basic Run
python main.py /path/to/folder

🔹 Dry Run (Safe Preview)
python main.py /path/to/folder --dry-run

🔹 Disable Logging
python main.py /path/to/folder --no-log

🔹 Combined Example
python main.py /path/to/folder --dry-run --no-log


🛡 Safety & Reliability:-

1.Dry-run mode prevents accidental file movement

2.Duplicate detection prevents overwriting

3.Logging provides traceability

4.Error handling ensures stable execution


🧠 How It Works:-

1.Accepts folder path via CLI.

2.Scans files inside the directory.

3.Matches file extensions to predefined categories.

4.Creates folders if they do not exist.

5.Moves files safely while handling duplicates.

6.Logs operations (unless disabled).


👨‍💻 Author

Kavyapal Singh                 
B.Tech IT Student             
Python Automation Project                   
