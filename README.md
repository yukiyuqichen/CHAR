![Image](https://raw.githubusercontent.com/yukiyuqichen/CHAR/main/img/icon.png)

<p align="center">
<a href="https://pypi.org/project/char-converter">
    <img src="https://img.shields.io/pypi/v/char-converter.svg" /></a>
<a href="http://www.apache.org/licenses/">
    <img src="https://img.shields.io/badge/License-MIT-green.svg" /></a>
<a href="https://colab.research.google.com/github/yukiyuqichen/CHAR/blob/main/test/test.ipynb">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" /></a>
</p>


<p align="center">
<big><strong>Chinese Character Variant Converter,</strong></big>
</p>
<p align="center">
<strong>an open-source library for converting Chinese character variants to standard simplified or traditional characters.</strong>
</p>
<p align="center">
* About the project's name and logo: "CHAR" comes from "Chinese character variant" and also refers to a type of beautiful fish with a gradient of red color (Arctic Char).
</p>

# Online Demo
<p align="center">
  <a href="https://yukiyuqichen.github.io/CHAR/">Char Converter Demo</a>
</p>

<p align="center">
<img src="https://raw.githubusercontent.com/yukiyuqichen/CHAR/main/img/demo.png" />
</p>

# Python

## Install
```
pip install char-converter
```
**Important Note:** We have been checking and updating the data from time to time. Please run the following command to ensure the package is the latest version.

## Upgrade
```
pip install char-converter -U
```

## Usage
### Convert text
1. Mode: one2one
```
from char_converter import CharConverter

text = '苟馀情其訫姱㠯练要兮，镸顑頷亦何伤。'

converter = CharConverter('v2t')
converted_text = converter.convert(text)
# 苟餘情其信姱以練要兮，長顑頷亦何傷。

converter = CharConverter('v2s')
converted_text = converter.convert(text)
# 苟余情其信姱以练要兮，长顑颔亦何伤。
```
2. Mode: one2many
```
from char_converter import CharConverter

text = '鈡𩄇毓秀'

converter = CharConverter('v2t')
converter.set_mode('one2many')
converted_text = converter.convert(text)
# 【鍾|鐘】靈毓秀
```

### Convert file
```
from char_converter import CharConverter

converter = CharConverter('v2s')
converter.convert_file(input_file, output_file)
```

# Data source

**[CBDB Project](https://projects.iq.harvard.edu/cbdb)**
<img src="https://projects.iq.harvard.edu/sites/projects.iq.harvard.edu/files/cbdb/files/logo.png?m=1696407478" width="35">

**[OpenCC](https://github.com/BYVoid/OpenCC)**
<img src="https://c.disquscdn.com/uploads/users/3634/6167/avatar200.jpg?1660808503" width="25">
[![image](https://img.shields.io/badge/License-Apache--2.0-green.svg)](http://www.apache.org/licenses/)

**[Dictionary of Variant Chinese Characters](https://dict.variants.moe.edu.tw/variants/rbt/home.do)**

**[General Standard Chinese Characters Table](http://www.moe.gov.cn/jyb_sjzl/ziliao/A19/201306/t20130601_186002.html)**


# Data filtering
![Image](https://raw.githubusercontent.com/yukiyuqichen/CHAR/main/img/workflow.png)


# Contributors

**Yuqi Chen** (data collection and programming)

**Hongsu Wang** (project manager)

**Yiyi Wang** (proofreading)

**Fengyi Ji** (data collection)

**Kaini Xiong** (proofreading)


## License

[![License: CC BY-SA 4.0](https://licensebuttons.net/l/by-sa/4.0/88x31.png)](https://creativecommons.org/licenses/by-sa/4.0/)




