We are in the era of AI.
Most side projects now start with AI-generated ideas — including the file structure.

Instead of manually creating folders and files, just paste the AI-generated structure into a file, and tao will generate the entire project structure for you.

What It Does
Parses a markdown-style project tree
Automatically creates folders and files
Supports dry-run mode
Prevents accidental overwrites (unless --force is used)

Perfect for:
AI-generated project scaffolds
Quick prototyping
Bootstrapping side projects

Installation 
pip install tao

Create a file called structure.md:

my-app/
├── app/
│   ├── main.py
│   └── utils.py
├── tests/
│   └── test_main.py
└── README.md

Generate the structure:
tao structure.md

Dry Run (Preview Without Creating Files):
tao structure.md --dry-run

Overwrite Existing Files:
tao structure.md --force