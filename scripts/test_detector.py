from codebase_intelligence_agent.scanner.scanner import scan_repository
from codebase_intelligence_agent.detector.technology_detector import detect_technologies

scanner_result = scan_repository(
    "examples/sample_repo"
)

result = detect_technologies(
    scanner_result
)

print(result)