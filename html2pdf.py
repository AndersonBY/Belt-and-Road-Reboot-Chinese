# -*- coding: utf-8 -*-
# @Author: Bi Ying
# @Date:   2023-11-11 17:03:10
# @Last Modified by:   Bi Ying
# @Last Modified time: 2023-11-11 17:28:53
from pathlib import Path

from playwright.sync_api import sync_playwright

proofread_folder = Path("proofread")
# HTML文件夹里的所有HTML文件
for html_file in proofread_folder.glob("*.html"):
    with sync_playwright() as p:
        # iphone_13 = p.devices["iPhone 13 Pro Max landscape"]
        iphone_13 = p.devices["iPhone 13 Pro Max"]
        browser = p.chromium.launch()
        context = browser.new_context(
            **iphone_13,
        )
        page = context.new_page()
        page.goto(html_file.absolute().as_uri())
        pdf_file = proofread_folder / f"{html_file.stem}.pdf"
        page.pdf(path=pdf_file, format="A4", print_background=True)
        browser.close()
