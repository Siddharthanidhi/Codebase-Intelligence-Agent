from pathlib import Path

IMPORTANT_FILES = {
    "README.md",
    "requirements.txt",
    "pyproject.toml",
    "package.json",
    "Dockerfile",
    "docker-compose.yml",
    "vite.config.js",
}

DEFAULT_IGNORED_DIRS = {
    "node_modules",
    ".git",
    ".venv",
    "__pycache__",
    "dist",
    "build",
    }

SCAN_PROFILES = {
    "understanding": {
        "ignored_dirs": DEFAULT_IGNORED_DIRS
    },
    "diagnostic": {
        "ignored_dirs": set()
    }
}

def walk_repository(
    current_path: Path,
    root_path: Path,
    profile: str,
    ignored_dirs: set,
):

    folders = []
    files = []
    skipped_dirs = []

    for item in current_path.iterdir():

        if item.is_dir():

            if (
                profile == "understanding"
                and item.name in ignored_dirs
            ):
                skipped_dirs.append(item.name)
                continue

            folders.append(
                item.relative_to(root_path).as_posix()
            )
            
            child_result = walk_repository(
                item,
                root_path,
                profile,
                ignored_dirs,
            )
            
            folders.extend(child_result["folders"])
            files.extend(child_result["files"])
            skipped_dirs.extend(
                child_result["ignored_dirs"]
            )

        elif item.is_file():

            files.append(
                item.relative_to(root_path).as_posix()
            )

    return {
        "folders": folders,
        "files": files,
        "ignored_dirs": skipped_dirs,
    }

def scan_repository(repo_path: str, profile: str = "understanding"):
    
    """
    Scan a repository and return basic inventory information.
    """

    important_files = []    
    
    repo = Path(repo_path)
    
    profile_config = SCAN_PROFILES[profile]

    traversal_result = walk_repository(
        repo,
        repo,
        profile,
        profile_config["ignored_dirs"]
    )
    
    folders = traversal_result["folders"]
    files = traversal_result["files"]
    ignored_dirs = traversal_result["ignored_dirs"]
    
    if not repo.exists():
        raise FileNotFoundError(
            f"Repository not found: {repo_path}"
        )
    
    for file_path in files:

        file_name = Path(file_path).name

        if file_name in IMPORTANT_FILES:
            important_files.append(file_path)
            
    stats = {
        "total_files": len(files),
        "total_folders": len(folders),
        "ignored_directories": len(ignored_dirs),
    }
                
    return {
    "repository_name": repo.name,
    "root_path": str(repo.resolve()),
    "folders": folders,
    "files": files,
    "important_files": important_files,
    "ignored_dirs": ignored_dirs,
    "stats": stats,
    }
