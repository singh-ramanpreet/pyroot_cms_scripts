# ROOT Canvas CMS Styling with Python

### Usage
---------
First import the functions,
```python
from CMS_style import CMS_style
from CMS_text import CMS_text
```
then after creating the `TCanvas` instance `canvas = ROOT.TCanvas()`,

1. For CMS styling,
add `CMS_style("1D")` or `CMS_style("2D")`.

2. For CMS text in upper left outside frame, use `CMS_text(canvas)`. Change the text in `CMS_text.py` file manually.

### Using it in multiple places
----------
Clone this repository somewhere in your working area,
```bash
cd /path/to/workingDir
git clone https://github.com/singh-ramanpreet/pyroot-cms-scripts.git
```

then in the your python script,
```python
import sys
sys.path.append("/path/to/workingDir/pyroot-cms-scripts")
```

Now you can proceed with steps described in Usage.
