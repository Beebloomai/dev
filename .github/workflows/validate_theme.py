import sys
import argparse
from lxml import etree
import lxml.etree

def validate_xml(file_path):
    try:
        tree = etree.parse(file_path, parser=lxml.etree.XMLParser(resolve_entities=False))
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
                print(f"Warning: Potential broken link at {etree.tostring(link, pretty_print=True)}")

        print("XML validation passed!")
    except Exception as e:
        print(f"Validation failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", required=True, help="Path to XML theme file")
    args = parser.parse_args()
    validate_xml(args.file)
