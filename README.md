# 孙烨 · Ye Sun

基于 [al-folio](https://github.com/alshedivat/al-folio) 的个人学术与求职网站。保留 Jekyll 和 gem 提供的布局，使用中文内容与轻量页面样式。原始资料在相邻 `../info/`，不进入站点或发布产物。

## 页面

- `/`：简洁履历，教育、代表研究、主要工程经历与奖励。
- `/research/`：详细研究经历；eXpath 属于研究，GeneticPrism 聚焦层次图与布局算法，CueIR 仅简述在研状态。
- `/experience/`：工程实践，包括 GeneticFlow、MaterAgent、数据分类分级与商汤。
- `/publications/`：论文列表及状态，不将投稿稿件计为录用。
- `/cv/`：完整履历。
- `/assets/pdf/Ye-Sun-Resume-ZH.pdf`：唯一固定简历 PDF（2 页 A4）。

顶栏提供博客、Google Scholar、哔哩哔哩、下载简历、语言和主题切换。首页包含研究、工程、技术与语言和论文列表，正文不重复放置这些外部主页链接。

## 内容维护

中文内容在 `_data/profile.json`，对应英文译稿在 `_data/profile.en.json`。更新事实时同步两个文件；相同条目保留同一 ID。研究和工程分别组织，不单列技能栏。

```sh
python bin/build_profile.py --pages-only
```

脚本生成 `_pages/`。请编辑数据文件后重新生成，不直接修改生成的页面。CSS 在 `assets/css/profile.css`，导航使用 `_includes/header.liquid` 本地覆盖，支持按页面语言筛选导航及同页语言切换；已记录到 `.al-folio-overrides.yml`，其余布局沿用 gem。

合作论文的状态、技术分工和平台统计依据本人提供；尚未提供的作者或 DOI 不臆补。MaterAgent 暂列进行中，待补起始年月和具体交付。未上传匿名投稿全文、内部设计文档、成绩单或证件。

## 本地构建与预览

需要现代 Ruby（本次验证为 Ruby 4.0.7）、Bundler 和 Node.js。macOS 若系统 Ruby 太旧，可使用 Homebrew Ruby，并把 `/opt/homebrew/opt/ruby/bin` 加入当前 shell 的 PATH。

```sh
bundle config set --local path vendor/bundle
bundle install
npm ci
python bin/build_profile.py --pages-only
bundle exec jekyll serve --host 127.0.0.1
```

打开 `http://127.0.0.1:4000/`。默认 `baseurl` 为空，适用于个人域名根路径。部署到子目录时同时设置 `url` 和 `baseurl`。

## 更新固定 PDF

PDF 在本地生成并检查后随网站发布；网页无在线生成接口。已提交的 PDF 可以直接下载，普通 Jekyll 构建不依赖 PDF 生成工具。

```sh
python -m pip install -r requirements-pdf.txt
python bin/build_profile.py
```

默认使用 macOS 的 Arial Unicode TrueType 字体。其他系统通过 `CV_FONT=/path/to/chinese-font.ttf` 指定支持中文的 TrueType 字体；字体缺失会明确失败。生成后检查全部页面的中文、分页与链接，再发布。网页与 PDF 共用内容数据，但独立排版。

## 自有服务器部署

1. 在 `_config.yml` 设置实际 `url`（例如 `https://cv.example.com`）；根域名部署保持 `baseurl: ""`。
2. 运行 `JEKYLL_ENV=production bundle exec jekyll build`。
3. 将 `_site/` 内容上传到服务器静态目录，由 Nginx 或 Caddy 提供服务。**只发布 `_site/`，不发布仓库根目录或 `../info/`。**
4. 在 Web 服务器配置中使用 `try_files $uri $uri/ =404`（Nginx），并将 404 指向 `/404.html`。

`.github/workflows/build.yml` 只构建并上传静态产物，不自动部署到 GitHub Pages 或个人服务器。上游示例工作流保留在 `.github/upstream-workflows/`，不会执行。服务器地址、博客地址和域名确定后再配置实际发布。

## 检查

```sh
npm run lint:prettier
bundle exec al-folio upgrade audit --no-fail
bundle exec al-folio upgrade overrides audit
bundle exec jekyll build
```

上游主题说明见 `docs/`；LICENSE 保留上游 MIT 授权。示例论文、文章、项目、音视频和 CV 数据已清理，避免发布成个人成果。

## 中英文与个人信息

中文页面位于 `/`、`/research/` 等路径，对应英文位于 `/en/`、`/en/research/`。每页导航支持对应页面的中英文切换，HTML lang 随页面语言设置。英文采用独立译稿，不调用在线翻译或加载第三方资源。固定 PDF 当前为中文版，英文页面按钮已明确标注 Chinese。

首页及完整履历包含证件照、微信／手机、常用邮箱、学校邮箱、导师及副导师链接。博客、Google Scholar 和哔哩哔哩统一放在顶栏。照片来自 `../info/证件照.jpg`，网站副本缩至 600px 以减少下载量，原始文件不变。

此仓库是个人站点而非上游 starter。`_includes/header.liquid` 是经审计确认的导航覆盖，因此上游禁止任何 `_includes/` 的 `lint:style-contract` 不再适用于此定制站点；用 `al-folio upgrade overrides audit` 检查覆盖漂移，并检查双语路径和导航。
