![Image](https://raw.githubusercontent.com/yukiyuqichen/CHAR/main/img/icon.png)


# Chinese character variant converter

[![image](https://img.shields.io/pypi/v/char-converter.svg)](https://pypi.org/project/char-converter)
[![image](https://img.shields.io/badge/License-Apache--2.0-green.svg)](http://www.apache.org/licenses/)
[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/yukiyuqichen/CHAR/blob/main/test/test.ipynb)


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
<a href="https://projects.iq.harvard.edu/cbdb">   <img src="https://projects.iq.harvard.edu/sites/projects.iq.harvard.edu/files/cbdb/files/logo.png?m=1696407478" width="85">
</a> **CBDB Project**

 <a href="https://github.com/BYVoid/OpenCC">   <img src="https://c.disquscdn.com/uploads/users/3634/6167/avatar200.jpg?1660808503" width="66">
</a>  **OpenCC**  [![image](https://img.shields.io/badge/License-Apache--2.0-green.svg)](http://www.apache.org/licenses/)

**<a href="https://dict.variants.moe.edu.tw/variants/rbt/home.do" style="color: black;">Dictionary of Variant Chinese Characters</a>**

**<a href="http://www.moe.gov.cn/jyb_sjzl/ziliao/A19/201306/t20130601_186002.html" style="color: black;">General Standard Chinese Characters Table</a>**


## Data filtering
![Image](https://raw.githubusercontent.com/yukiyuqichen/CHAR/main/img/workflow.png)


## Contributor
Yuqi Chen (data collection and programing)

Hongsu Wang (project manager)

Yiyi Wang (proofreading), Fengyi Ji (data collection)



