<img src="https://github.com/yukiyuqichen/CHAR/blob/main/icon/icon.png" width="300" />

# CHAR
 Chinese character variant converter
 
## Usage
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
## Contributor
Yuqi Chen (data collection and programing), Yiyi Wang (proofreading), Fengyi Ji (data collection)

Hongsu Wang (project manager)

