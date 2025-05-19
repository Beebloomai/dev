import sys
import argparse
from lxml import etree

def validate_xml(file_path):
    try:
        # Secure parser with XXE protection
        safe_parser = etree.XMLParser(resolve_entities=False, no_network=True, dtd_validation=False)
        
        tree = etree.parse(file_path, parser=safe_parser)
        root = tree.getroot()

        # Example checks
        if root.tag != 'html':
            print("Error: Root tag is not <html>")
            sys.exit(1)

        # Check meta tags exist
        metas = root.findall(".//meta")
        if not metas:
            print("Warning: No <meta> tags found.")

        # Check internal links are not broken (example)
        links = root.findall(".//a")
        for link in links:
            href = link.get('href', '')
            if href == '' or href == '/':
                print(f"Warning: Potential broken link at {etree.tostring(link, pretty_print=True).decode()}")

        print("✅ XML validation passed!")
    except Exception as e:
        print(f"❌ Validation failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", required=True, help="Path to XML theme file")
    args = parser.parse_args()
    validate_xml(args.file)
