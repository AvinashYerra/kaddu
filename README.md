We are in the era of AI.
Most side projects now start with AI-generated ideas — including the file structure.

Instead of manually creating folders and files, just paste the AI-generated structure into a file, and tao will generate the entire project structure for you.

What It Does
1. Parses a markdown-style project tree
2. Automatically creates folders and files
3. Supports dry-run mode
4. Prevents accidental overwrites (unless --force is used)

Perfect for:
1. AI-generated project scaffolds
2. Quick prototyping
3. Bootstrapping side projects

Installation:
```
pip install kaddu
```

Create a file called structure.md:

my-app/
├── app/
│   ├── main.py
│   └── utils.py
├── tests/
│   └── test_main.py
└── README.md

Generate the structure:
```
kaddu structure.md
```

Dry Run (Preview Without Creating Files):
```
kaddu structure.md --dry-run
```
Overwrite Existing Files:
```
kaddu structure.md --force
```
