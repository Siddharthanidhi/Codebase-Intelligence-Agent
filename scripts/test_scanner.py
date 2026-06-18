from codebase_intelligence_agent.scanner.scanner import scan_repository

result = scan_repository(
    "examples/sample_repo",
    profile="diagnostic"
)

print(result)