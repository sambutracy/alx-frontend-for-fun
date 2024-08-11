#!/usr/bin/python3
"""
markdown2html.py: A script to convert Markdown files to HTML.
"""

import sys
import os

def markdown_to_html(markdown_file, output_file):
    """
    Converts a Markdown file to HTML and writes it to the output file.
    
    Args:
        markdown_file (str): Path to the Markdown file.
        output_file (str): Path to the output HTML file.
    """
    with open(markdown_file, 'r') as md_file:
        content = md_file.read()

    html_content = "<html><body>\n" + content + "\n</body></html>"

    with open(output_file, 'w') as html_file:
        html_file.write(html_content)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        sys.exit(1)

    markdown_file = sys.argv[1]
    output_file = sys.argv[2]

    if not os.path.isfile(markdown_file):
        sys.stderr.write(f"Missing {markdown_file}\n")
        sys.exit(1)

    markdown_to_html(markdown_file, output_file)
    sys.exit(0)
