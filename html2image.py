# -*- coding: utf-8 -*-
# @Author: Bi Ying
# @Date:   2023-11-11 17:03:10
# @Last Modified by:   Bi Ying
# @Last Modified time: 2023-11-11 17:22:00
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
        screenshot_file = proofread_folder / f"{html_file.stem}.png"
        page.screenshot(path=screenshot_file, full_page=True, timeout=0)
        browser.close()
