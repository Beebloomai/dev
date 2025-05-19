import sys
from lxml import etree

def validate_xml(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            etree.parse(f)
        print("✅ XML validation passed.")
    except Exception as e:
        print(f"❌ XML validation failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="Path to XML file")
    args = parser.parse_args()
    validate_xml(args.file)