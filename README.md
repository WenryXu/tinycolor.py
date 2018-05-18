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

## 支持的色值形式

### Hex

```plain
#FFF
#FFFFFF
```

### RGB

```plain
rgb(255, 255, 255)
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

将短十六进制色值（三位）转换为长十六进制色值（六位）

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
```

### to_hex

将颜色转换为十六进制色值

```python
color = 'rgb(255, 255, 255)'
to_hex(color) # '#FFFFFF'

color = '#FFF'
to_hex(color) # '#FFFFFF'
```

### to_rgb

将颜色转换为 RGB 格式色值

```python
color = '#FFFFFF'
to_rgb(color) #'rgb(255, 255, 255)'
```

### get_brightness

返回颜色的感知亮度

```python
color = '#000000'
get_brightness(color) # 0

color = 'rgb(255, 255, 255)'
get_brightness(color) # 255
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
