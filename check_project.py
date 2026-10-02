from pathlib import Path
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
required = [
    ROOT / "settings.gradle.kts",
    ROOT / "build.gradle.kts",
    ROOT / "app" / "build.gradle.kts",
    ROOT / "app" / "src" / "main" / "AndroidManifest.xml",
    ROOT / "app" / "src" / "main" / "java" / "com" / "mishkat" / "app" / "MainActivity.kt",
]
for p in required:
    assert p.exists() and p.stat().st_size > 0, f"Missing: {p}"
ET.parse(ROOT / "app" / "src" / "main" / "AndroidManifest.xml")
text = (ROOT / "app" / "src" / "main" / "java" / "com" / "mishkat" / "app" / "MainActivity.kt").read_text(encoding="utf-8")
for token in ["مِشكاة", "نورٌ لقلبك.. في كل حين", "HomeScreen", "QuranScreen", "AdhkarScreen", "QiblaScreen", "TasbeehScreen"]:
    assert token in text, f"Expected token missing: {token}"
print("Static project checks: PASS")
