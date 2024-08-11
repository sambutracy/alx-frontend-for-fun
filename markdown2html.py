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
        lines = md_file.readlines()

    html_content = ""

    for line in lines:
        line = line.strip()
        
        # Check for headers
        if line.startswith("#"):
            header_level = line.count("#", 0, 6)  # count number of # at the start of the line
            header_text = line[header_level:].strip()  # remove the heading hashes and strip any leading spaces
            html_content += f"<h{header_level}>{header_text}</h{header_level}>\n"
        else:
            html_content += f"<p>{line}</p>\n"
    
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
