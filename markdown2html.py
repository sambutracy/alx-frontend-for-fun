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

    html_content = "<html><body>\n"

    for line in lines:
        line = line.strip()

        # Check for headers
        if line.startswith("# "):
            html_content += f"<h1>{line[2:]}</h1>\n"
        elif line.startswith("## "):
            html_content += f"<h2>{line[3:]}</h2>\n"
        elif line.startswith("### "):
            html_content += f"<h3>{line[4:]}</h3>\n"
        elif line.startswith("#### "):
            html_content += f"<h4>{line[5:]}</h4>\n"
        elif line.startswith("##### "):
            html_content += f"<h5>{line[6:]}</h5>\n"
        elif line.startswith("###### "):
            html_content += f"<h6>{line[7:]}</h6>\n"
        else:
            html_content += f"<p>{line}</p>\n"

    html_content += "</body></html>\n"

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
