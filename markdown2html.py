# -*- coding: utf-8 -*-
# @Author: Bi Ying
# @Date:   2023-11-10 18:14:40
# @Last Modified by:   Bi Ying
# @Last Modified time: 2023-11-11 18:11:24
from pathlib import Path

import markdown


proofread_folder = Path("proofread")
html_template_folder = Path("html_template")
for file in proofread_folder.glob("*.md"):
    with open(file, "r", encoding="utf8") as f:
        markdown_text = f.read()
    with open(html_template_folder / "template.html", "r", encoding="utf8") as f:
        template = f.read()
    with open(file.with_suffix(".html"), "w", encoding="utf8") as f:
        html_content = template.replace(
            "{{content}}",
            markdown.markdown(
                markdown_text,
                extensions=["fenced_code", "tables"],
            ),
        )
        f.write(html_content)
