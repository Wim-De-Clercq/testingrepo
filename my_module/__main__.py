from pathlib import Path

dist_file = Path(__file__).parent.parent / "frontend" / "dist" / "compiled.js"
dist_file.parent.mkdir(parents=True, exist_ok=True)
dist_file.touch()

print(f"Created {dist_file}")
