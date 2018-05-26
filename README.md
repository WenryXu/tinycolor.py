# tinycolor.py

## Python color tooling

tinycolor.py 是一个用于 Python 的颜色操作和转换的库。它支持多种形式的输入，同时提供颜色转换和一些其他的实用功能。

## 安装

### 通过 pip 安装（推荐）

```bash
$ pip3 install tinycolor.py
```

### 源码安装

```bash
$ [sudo] python3 setup.py install
```

## 使用

### import

```python
import tinycolor

print(tinycolor.is_valid('#FFFFFF'))
```

### from ... import

```python
from tinycolor import *

print(is_valid('#FFFFFF'))
```

## 支持的色值形式

### Hex、8-digit Hex

```plain
#FFF
#FFFFFF
#FFFC
#FFFFFFCC
```

### RGB、RGBA

```plain
rgb(255, 255, 255)
rgba(255, 255, 255, .8)
```

## 方法

### get_format

获取颜色的格式，如果获取不到格式，则抛出一个 RuntimeError

```python
color = '#FFFFFF'
get_format(color) # 'Hex'

color = 'rgb(255, 255, 255)'
get_format(color) # 'RGB'

color = 'ABCDEF123'
get_format(color) # RuntimeError('Not a color!')
```

### is_valid

判断颜色格式是否合法

```python
color = '#FFFFFF'
is_valid(color) # True

color = 'rgb(255, 255, 255)'
is_valid(color) # True

color = 'ABCDEF123'
is_valid(color) # False
```

### short_hex_to_long

将短 Hex 或 8-digit Hex 格式色值转换为长 Hex 或 8-digit Hex 格式色值

```python
color = '#FFF'
short_hex_to_long(color) # '#FFFFFF'

color = '#FFFFFF'
short_hex_to_long(color) # '#FFFFFF'

color = 'rgb(255, 255, 255)'
short_hex_to_long(color) # RuntimeError('Not a hex color!')
```

### to_r_g_b

分别获取颜色 R、G、B 三通道的十进制色值

```python
color = '#FFFFFF'
to_r_g_b(color) # 255, 255, 255

color = 'rgb(255, 255, 255)'
to_r_g_b(color) # 255, 255, 255

color = '#FFFFFFCC'
to_r_g_b(color) # 255, 255, 255

color = 'rgba(255, 255, 255, .5)'
to_r_g_b(color) # 255, 255, 255
```

### to_r_g_b_a

分别获取颜色 R、G、B、Alpha 四通道的十进制色值

```python
color = '#FFFFFFCC'
to_r_g_b_a(color) # 255, 255, 255, 0.8

color = 'rgba(255, 255, 255, .5)'
to_r_g_b_a(color) # 255, 255, 255, 0.5

color = '#FFFFFF'
to_r_g_b_a(color) # 255, 255, 255, 1

color = 'rgb(255, 255, 255)'
to_r_g_b_a(color) # 255, 255, 255, 1
```

### to_hex

将颜色转换为 Hex 格式色值

```python
color = 'rgb(255, 255, 255)'
to_hex(color) # '#FFFFFF'

color = '#FFF'
to_hex(color) # '#FFFFFF'

color = 'rgb(255, 255, 255, .8)'
to_hex(color) # '#FFFFFF'

color = '#FFFC'
to_hex(color) # '#FFFFFF'
```

### to_hex8

将颜色转换为 8-digit Hex 格式色值

```python
color = 'rgb(255, 255, 255, .8)'
to_hex8(color) # '#FFFFFFCC'

color = '#FFFC'
to_hex8(color) # '#FFFFFFCC'

color = 'rgb(255, 255, 255)'
to_hex8(color) # '#FFFFFFFF'

color = '#FFF'
to_hex8(color) # '#FFFFFFFF'
```

### to_rgb

将颜色转换为 RGB 格式色值

```python
color = '#FFFFFF'
to_rgb(color) # 'rgb(255, 255, 255)'
```

### to_rgba

将颜色转换为 RGBA 格式色值

```python
color = 'rgba(255, 255, 255, .5)'
to_rgba(color) # 'rgba(255, 255, 255, 0.5)'

color = '#FFFFFFCC'
to_rgba(color) # 'rgba(255, 255, 255, 0.8)'
```

### get_brightness

返回颜色的感知亮度，基于 [Web Content Accessibility Guidelines (Version 1.0)](https://www.w3.org/TR/AERT/#color-contrast) 的定义

```python
color = '#000000'
get_brightness(color) # 0

color = 'rgb(255, 255, 255)'
get_brightness(color) # 255
```

### get_luminance

返回颜色的感知亮度，基于 [Web Content Accessibility Guidelines (Version 2.0)](https://www.w3.org/TR/2008/REC-WCAG20-20081211/#contrast-ratiodef) 的定义

```python
color = '#000000'
get_luminance(color) # 0

color = 'rgb(255, 255, 255)'
get_luminance(color) # 1
```

### is_dark

返回颜色的感知亮度是否为暗

```python
color = '#000000'
is_dark(color) # True

color = 'rgb(255, 255, 255)'
is_dark(color) # False
```

### is_light

返回颜色的感知亮度是否为亮

```python
color = '#000000'
is_light(color) # False

color = 'rgb(255, 255, 255)'
is_light(color) # True
```
