# ROOT Canvas CMS Styling with Python

### Installation
----------------
Clone this repository, then navigate to the directory and install using `pip`.
```bash
git clone https://github.com/singh-ramanpreet/pyroot_cms_scripts.git
cd pyroot_cms_scripts
pip install --user .
```

### Usage
---------
First import the functions,
```python
from pyroot_cms_scripts import CMS_style, CMS_text
```
then after creating the `TCanvas` instance `canvas = ROOT.TCanvas()`,

1. For CMS styling,
add `CMS_style("1D")` or `CMS_style("2D")`.

2. For CMS text in upper left outside frame, use `CMS_text(canvas)`. Change the text in `CMS_text.py` file manually.
