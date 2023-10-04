![Image](https://raw.githubusercontent.com/yukiyuqichen/CHAR/main/img/icon.png)



**Chinese character variant converter**

[![image](https://img.shields.io/pypi/v/char-converter.svg)](https://pypi.org/project/char-converter)

[![image](https://img.shields.io/badge/License-Apache-green.svg)](http://www.apache.org/licenses/)

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
[Dictionary of Variant Chinese Characters](https://dict.variants.moe.edu.tw/variants/rbt/home.do)

[General Standard Chinese Characters Table](http://www.moe.gov.cn/jyb_sjzl/ziliao/A19/201306/t20130601_186002.html)

[CBDB Team](https://projects.iq.harvard.edu/cbdb)

[OpenCC](https://github.com/BYVoid/OpenCC)


## Data filtering
![Image](https://raw.githubusercontent.com/yukiyuqichen/CHAR/main/img/workflow.png)


## Contributor
Yuqi Chen (data collection and programing)

Hongsu Wang (project manager)

Yiyi Wang (proofreading), Fengyi Ji (data collection)



