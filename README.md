![Image](https://raw.githubusercontent.com/yukiyuqichen/CHAR/main/icon/icon.png)

# CHAR
 Chinese character variant converter

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
[Dictionary of Variant Chinese Characters, by the Ministry of Education, Taiwan, 2017](https://dict.variants.moe.edu.tw/variants/rbt/home.do)

[CBDB Team](https://projects.iq.harvard.edu/cbdb)

[OpenCC](https://github.com/BYVoid/OpenCC)

## Contributor
Yuqi Chen (data collection and programing), Yiyi Wang (proofreading), Fengyi Ji (data collection)

Hongsu Wang (project manager)

