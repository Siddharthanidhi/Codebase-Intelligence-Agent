# Architecture


User
 │
 ▼
Repository Input via Streamlit (repo path entered)
 │
 ▼
Repository Scanner ---> display results
 │
 ▼
File Analyzer
 │
 ▼
Repository Knowledge Base
 ├───────────────┐
 │               │
 ▼               ▼
Overview     Structure
Generator    Explorer
 │               │
 └───────┬───────┘
         ▼
 Question Answering
         ▼
        User


Component Responsibilities

1. Streamlit UI
    Allows users to provide a local repository path and interact with the system.
    
2. Repository Scanner
    Traverses folders and files in the repository and builds a structural map.
    Example:
        {
        "src": {
            "components": [
            "ModeCard.jsx",
            "HeroSection.jsx"
            ],
            "pages": [
            "Home.jsx"
            ]
        }
        }

3. File Analyzer
    Extracts useful information from each file.
    Example: This component renders the homepage and coordinates navigation between quiz modes.

4. Repository Knowledge Base
    Stores repository understanding for later retrieval.

5. Overview Generator
    Creates a high-level summary of the repository.

6. Structure Explorer
    Explains folders, modules, and files.

7. Question Answering Engine
    Answers user questions using repository knowledge.