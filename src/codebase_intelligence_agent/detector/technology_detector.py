TECHNOLOGY_SIGNATURES = {
    "requirements.txt": "Python",
    "pyproject.toml": "Python",

    "package.json": "Node.js",

    "vite.config.js": "Vite",

    "pubspec.yaml": "Flutter",

    "Dockerfile": "Docker",
}

def detect_technologies(scanner_result):

    detected = set()
    evidence = {}

    important_files = scanner_result[
        "important_files"
    ]

    for file_path in important_files:

        file_name = file_path.split("/")[-1]

        if file_name in TECHNOLOGY_SIGNATURES:

            technology = TECHNOLOGY_SIGNATURES[
                file_name
            ]

            detected.add(technology)

            if technology not in evidence:
                evidence[technology] = []

            evidence[technology].append(
                file_path
            )

    return {
        "technologies": sorted(
            list(detected)
        ),
        "evidence": evidence
    }