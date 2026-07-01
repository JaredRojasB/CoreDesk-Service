#!/usr/bin/env python3
"""
Vantyx - Static Site Builder v3
Run: python build.py
Output: index.html (ready for GitHub Pages)
"""

HTML_TEMPLATE = open("template.html", encoding="utf-8").read()


def build():
    output_path = "index.html"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(HTML_TEMPLATE)
    print("Vantyx v3 generado: index.html")


if __name__ == "__main__":
    build()
