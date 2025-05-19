import sys
from pathlib import Path
import defusedxml.ElementTree as ET

def validate_xml_file(file_path):
    try:
        tree = ET.parse(file_path)
        print(f"✅ XML parsed successfully: {file_path}")
    except ET.ParseError as e:
        print(f"❌ XML parsing failed: {file_path}\nError: {e}")
        sys.exit(1)
    except FileNotFoundError:
        print(f"❌ File not found: {file_path}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python validate_xml.py <path_to_xml_file>")
        sys.exit(1)

    file_to_check = Path(sys.argv[1])
    validate_xml_file(file_to_check)
