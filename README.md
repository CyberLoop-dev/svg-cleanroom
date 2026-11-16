<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:111827,100:0f766e&height=160&section=header&text=SVG%20Cleanroom&fontSize=38&fontColor=ffffff" width="100%" alt="SVG Cleanroom banner" />
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&duration=2800&pause=700&color=0F766E&center=true&vCenter=true&width=820&lines=Clean+SVG+files+before+you+share+or+embed+them" alt="Animated SVG Cleanroom title" />
<p>A local SVG sanitizer that removes active content, event handlers, and unsafe external references without uploading files.</p>
<p><img src="https://img.shields.io/github/license/CyberLoop-dev/svg-cleanroom?style=for-the-badge" alt="MIT license" /> <img src="https://img.shields.io/github/languages/top/CyberLoop-dev/svg-cleanroom?style=for-the-badge" alt="Top language" /> <img src="https://img.shields.io/github/stars/CyberLoop-dev/svg-cleanroom?style=for-the-badge" alt="Stars" /> <img src="https://img.shields.io/github/last-commit/CyberLoop-dev/svg-cleanroom?style=for-the-badge" alt="Last commit" /></p>
<img src="assets/illustration.svg" width="92%" alt="SVG sanitizer workflow illustration" />
</div>

## 🎯 Overview

SVG files can contain more than shapes and colors. SVG Cleanroom parses files locally and removes active elements, inline event handlers, and unsafe external references before writing a cleaned copy. It never uploads files and never modifies the original.

## ✨ Features

- 🧼 Removes script, foreignObject, iframe, object, and embed elements.
- 🛡️ Strips inline event handlers and non-local href/src references.
- 🔎 Offers a check-only mode for CI or pre-publish reviews.
- 📁 Keeps the original file untouched and writes a separate result.

## 🎬 Demo

<pre><code>python main.py examples/unsafe-demo.svg --output cleaned.svg
python main.py cleaned.svg --check</code></pre>

There is no hosted demo; run the command locally to see the real output.

## 🚀 Quick Start

<pre><code>python main.py examples/unsafe-demo.svg --output cleaned.svg</code></pre>

## 🧰 Tech Stack

- Python 3.10+ standard library
- xml.etree.ElementTree for local XML parsing

## 🗂️ Folder Structure

<pre><code>svg-cleanroom/
├── main.py
├── requirements.txt
├── examples/
│   └── unsafe-demo.svg
└── assets/
    └── illustration.svg</code></pre>

## 🧭 Roadmap

- [ ] Add an optional strict allow-list for SVG elements and attributes.
- [ ] Add a batch-directory mode with a JSON summary.
- [ ] Add focused unit tests for malformed and edge-case SVG files.

## 🤝 Contributing

Issues and pull requests are welcome. Keep changes focused, explain the behavior being changed, and include a reproducible example for bug reports.

## 📄 License

Released under the MIT License. See [LICENSE](LICENSE).

<div align="center"><img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f766e,100:111827&height=110&section=footer" width="100%" alt="Animated wave footer" /></div>
