![Image](https://raw.githubusercontent.com/yukiyuqichen/CHAR/main/img/icon.png)

<p align="center">
<a href="https://pypi.org/project/char-converter">
    <img src="https://img.shields.io/pypi/v/char-converter.svg" /></a>
<a href="http://www.apache.org/licenses/">
    <img src="https://img.shields.io/badge/License-Apache--2.0-green.svg" /></a>
<a href="https://colab.research.google.com/github/yukiyuqichen/CHAR/blob/main/test/test.ipynb">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" /></a>
</p>


<p align="center">
<big><strong>Chinese character variant converter</strong></big>
</p>
<p align="center">
an open-sourced library for converting <u>Chinese character variants</u> to <u>standard simplified or traditional characters</u>.
</p>


## Install
```
pip install char-converter
```

## Usage
### Convert text
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

### Convert file
```
from char_converter import CharConverter

converter = CharConverter('v2s')
converter.convert_file(input_file, output_file)
```

## Data source

**[CBDB Project](https://projects.iq.harvard.edu/cbdb)**
<img src="https://projects.iq.harvard.edu/sites/projects.iq.harvard.edu/files/cbdb/files/logo.png?m=1696407478" width="35">

**[OpenCC](https://github.com/BYVoid/OpenCC)**
<img src="https://c.disquscdn.com/uploads/users/3634/6167/avatar200.jpg?1660808503" width="25">
[![image](https://img.shields.io/badge/License-Apache--2.0-green.svg)](http://www.apache.org/licenses/)

**[Dictionary of Variant Chinese Characters](https://dict.variants.moe.edu.tw/variants/rbt/home.do)**

**[General Standard Chinese Characters Table](http://www.moe.gov.cn/jyb_sjzl/ziliao/A19/201306/t20130601_186002.html)**


## Data filtering
![Image](https://raw.githubusercontent.com/yukiyuqichen/CHAR/main/img/workflow.png)


## Contributor

**Yuqi Chen** (data collection and programing)

**Hongsu Wang** (project manager)

**Yiyi Wang** (proofreading), **Fengyi Ji** (data collection)



