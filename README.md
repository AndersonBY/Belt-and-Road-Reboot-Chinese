# 自动格式化整理及渲染《一带一路重启：北京为降低全球基础设施倡议的风险努力》报告

## 报告来源

[Belt and Road Reboot: Beijing’s Bid to De-Risk Its Global Infrastructure Initiative](https://www.aiddata.org/publications/belt-and-road-reboot)

## 格式化整理及渲染流程

1. 下载原始报告 PDF 文件（分章节下载，方便后其处理）。
2. 使用 [Adobe Acrobat](https://www.adobe.com/sg/acrobat/online/pdf-to-word.html) 将 PDF 文件转换为 Word 文档。
3. 安装 [PDM](https://pdm-project.org/latest/) 包管理器。
4. 在项目路径下运行 `pdm install` 安装依赖。
   1. 如果需要渲染图片以及 PDF 文件，则使用该指令安装 `pdm install -G playwright` 然后运行 `.venv/Scripts/playwright.exe install`。
5. 在项目路径下运行 `pdm run format`
6. 手动校对 `proofread/formatted` 下的 Markdown 文件，修正格式错误及补充漏掉的图片。
7. 使用我分享的 [向量脉络](https://vectorvein.com) 工作流 [Markdown 保留格式翻译](https://vectorvein.com/workspace/workflow/template/2fe3e8c0e0ee4aa2909e142d484e1750) 依次将 Markdown 文件翻译为中文。
8. 将翻译后的 Markdown 文件放入 `proofread` 文件夹下。
9.  在项目路径下运行 `pdm run html` 将 Markdown 文件转换为 HTML 文件。
10. （可选）在项目路径下运行 `pdm run pdf` 将 HTML 文件转换为 PDF 文件。
11. （可选）在项目路径下运行 `pdm run image` 将 HTML 文件转换为适合手机阅读的长图。