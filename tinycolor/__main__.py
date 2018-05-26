#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re
import sys
import math

def _color_strip(color):
    """ 去除字符串中的多余空格

    Parameters
    ----------
    color : str

    Returns
    -------
    str
        返回去除了空格的颜色字符串
    """
    return color.strip().replace(' ', '')

def get_format(color):
    """ 获取颜色的格式

    如果获取不到格式，则抛出一个 RuntimeError

    Parameters
    ----------
    color : str

    Returns
    -------
    str
        如果颜色为 Hex 格式色值，则返回 'Hex'
        如果颜色为 8-digit Hex 格式色值，则返回 'Hex8'
        如果颜色为 RGB 格式色值，则返回 'RGB'
        如果颜色为 RGBA 格式色值，则返回 'RGBA'

    Notes
    -----
    关心 Alpha 通道

    Raise
    -----
    RuntimeError: Not a color!
    """
    color = _color_strip(color)

    regex_integer = "[-\\+]?\\d+%?"
    regex_number = "[-\\+]?\\d*\\.\\d+%?"
    regex_unit = "(?:" + regex_number + ")|(?:" + regex_integer + ")"

    regex_match3 = "[\\s|\\(]+(" + regex_unit + ")[,|\\s]+(" + regex_unit + ")[,|\\s]+(" + regex_unit + ")\\s*\\)?"
    regex_match4 = "[\\s|\\(]+(" + regex_unit + ")[,|\\s]+(" + regex_unit + ")[,|\\s]+(" + regex_unit + ")[,|\\s]+(" + regex_unit + ")\\s*\\)?"

    if re.match(r'^#?([0-9a-fA-F]{1})([0-9a-fA-F]{1})([0-9a-fA-F]{1})$', color, re.I) != None: # Hex3
        return 'Hex'
    elif re.match(r'^#?([0-9a-fA-F]{2})([0-9a-fA-F]{2})([0-9a-fA-F]{2})$', color, re.I) != None: # Hex6
        return 'Hex'
    elif re.match(r'^#?([0-9a-fA-F]{1})([0-9a-fA-F]{1})([0-9a-fA-F]{1})([0-9a-fA-F]{1})$', color, re.I) != None: # Hex4
        return 'Hex8'
    elif re.match(r'^#?([0-9a-fA-F]{2})([0-9a-fA-F]{2})([0-9a-fA-F]{2})([0-9a-fA-F]{2})$', color, re.I) != None: # Hex8
        return 'Hex8'
    elif re.match(r'rgb' + regex_match3, color, re.I) != None:
        return 'RGB'
    elif re.match(r'rgba' + regex_match4, color, re.I) != None:
        return 'RGBA'
    else:
        raise RuntimeError('Not a color!')

def is_valid(color):
    """ 判断颜色格式是否合法

    Parameters
    ----------
    color : str

    Returns
    -------
    bool
        合法则返回 True，否则返回 False

    See Also
    --------
    get_format

    Notes
    -----
    不关心 Alpha 通道
    """
    try:
       get_format(color)
    except RuntimeError:
        return False
    else:
        return True

def short_hex_to_long(color):
    """ 将短 Hex 或 8-digit Hex 格式色值转换为长 Hex 或 8-digit Hex 格式色值

    如果参数不是 Hex 或 8-digit Hex 格式色值，则抛出一个 RuntimeError

    Parameters
    ----------
    color : str

    Returns
    -------
    str
        返回转换后的 Hex 或 8-digit Hex 格式色值，字母为大写字母

    See Also
    --------
    get_format

    Notes
    -----
    关心 Alpha 通道

    Raise
    -----
    RuntimeError: Not a hex color!
    """
    color = _color_strip(color)

    if get_format(color) is 'Hex':
        if len(color) is 4:
            r = color[1] * 2
            g = color[2] * 2
            b = color[3] * 2
            return ('#' + r + g + b).upper()
        else:
            return color.upper()
    elif get_format(color) is 'Hex8':
        if len(color) is 5:
            r = color[1] * 2
            g = color[2] * 2
            b = color[3] * 2
            a = color[4] * 2
            return ('#' + r + g + b + a).upper()
        else:
            return color.upper()
    else:
        raise RuntimeError('Not a hex color!')

def to_r_g_b(color):
    """ 分别获取颜色 R、G、B 三通道的十进制色值

    Parameters
    ----------
    color : str

    Returns
    -------
    r : int
    g : int
    b : int

    See Also
    --------
    get_format, short_hex_to_long

    Notes
    -----
    不关心 Alpha 通道
    """
    color = _color_strip(color)

    if get_format(color) is 'Hex':
        color = short_hex_to_long(color)
        r = int(color[1:3], 16)
        g = int(color[3:5], 16)
        b = int(color[5:7], 16)
    elif get_format(color) is 'RGB':
        r, g, b = color[4:-1].split(',')

    return int(r), int(g), int(b)

def to_r_g_b_a(color):
    """ 分别获取颜色 R、G、B 三通道与 Alpha 通道的十进制色值

    Parameters
    ----------
    color : str

    Returns
    -------
    r : int
    g : int
    b : int
    a : float

    See Also
    --------
    get_format, short_hex_to_long

    Notes
    -----
    关心 Alpha 通道
    """
    color = _color_strip(color)

    if get_format(color) is 'Hex':
        color = short_hex_to_long(color)
        r = int(color[1:3], 16)
        g = int(color[3:5], 16)
        b = int(color[5:7], 16)
        a = 1
    elif get_format(color) is 'Hex8':
        color = short_hex_to_long(color)
        r = int(color[1:3], 16)
        g = int(color[3:5], 16)
        b = int(color[5:7], 16)
        if color[8] is '0':
            a = color[7]
        else:
            a = color[7:9]
        a = round(int(a, 16) / 255, 2)
    elif get_format(color) is 'RGB':
        r, g, b = color[4:-1].split(',')
        a = 1
    elif get_format(color) is 'RGBA':
        r, g, b, a = color[5:-1].split(',')
        try:
            int(a)
        except ValueError:
            a = float(a)
        else:
            a = int(a)

    if float(a) >= 1:
        a = 1
    elif float(a) < 0:
        a = 0

    if int(a) != 0:
        if math.fmod(a, int(a)) is 0:
            a = int(a)

    if a == 0:
        a = 0

    return int(r), int(g), int(b), a

def to_hex(color):
    """ 将颜色转换为 Hex 格式色值

    Parameters
    ----------
    color : str

    Returns
    -------
    str
        返回转换后的 Hex 格式色值，字母为大写字母

    See Also
    --------
    get_format, short_hex_to_long, to_r_g_b

    Notes
    -----
    不关心 Alpha 通道
    """
    if get_format(color) is 'Hex':
        return short_hex_to_long(color)
    else:
        r, g, b = to_r_g_b(color)
        r = str(hex(r)).replace('0x', '')
        g = str(hex(g)).replace('0x', '')
        b = str(hex(b)).replace('0x', '')
        r = '0' + r if len(r) is 1 else r
        g = '0' + g if len(g) is 1 else g
        b = '0' + b if len(b) is 1 else b
        return ('#' + r + g + b).upper()

def to_hex8(color):
    """ 将颜色转换为 8-digit Hex 格式色值

    Parameters
    ----------
    color : str

    Returns
    -------
    str
        返回转换后的 8-digit Hex 格式色值，字母为大写字母

    See Also
    --------
    get_format, short_hex_to_long, to_r_g_b_a

    Notes
    -----
    关心 Alpha 通道
    """
    if get_format(color) is 'Hex8':
        return short_hex_to_long(color)
    else:
        r, g, b, a = to_r_g_b_a(color)
        r = str(hex(r)).replace('0x', '')
        g = str(hex(g)).replace('0x', '')
        b = str(hex(b)).replace('0x', '')
        r = '0' + r if len(r) is 1 else r
        g = '0' + g if len(g) is 1 else g
        b = '0' + b if len(b) is 1 else b

        if a == 0:
            a = '00'
        elif a == 1:
            a = 'FF'
        else:
            a = str(hex(int(round(255 * a / 100, 2) * 100))).replace('0x', '')
            a = a + '0' if len(a) is 1 else a

        return ('#' + r + g + b + a).upper()

def to_rgb(color):
    """ 将颜色转换为 RGB 格式色值

    Parameters
    ----------
    color : str

    Returns
    -------
    str
        返回转换后的 RGB 格式色值

    See Also
    --------
    to_r_g_b

    Notes
    -----
    不关心 Alpha 通道
    """
    r, g, b = to_r_g_b(color)
    return 'rgb(' + str(r) + ', ' + str(g) + ', ' + str(b) + ')'

def to_rgba(color):
    """ 将颜色转换为 RGBA 格式色值

    Parameters
    ----------
    color : str

    Returns
    -------
    str
        返回转换后的 RGBA 格式色值

    See Also
    --------
    to_r_g_b_a

    Notes
    -----
    关心 Alpha 通道
    """
    r, g, b, a = to_r_g_b_a(color)
    return 'rgb(' + str(r) + ', ' + str(g) + ', ' + str(b) + ', ' + str(a) + ')'

def get_brightness(color):
    """ 返回颜色的感知亮度

    https://www.w3.org/TR/AERT/#color-contrast

    Parameters
    ----------
    color : str

    Returns
    -------
    float
        返回颜色的感知亮度，范围在 0 - 255 之间

    See Also
    --------
    to_r_g_b

    Notes
    -----
    不关心 Alpha 通道
    """
    r, g, b = to_r_g_b(color)
    return (r * 299 + g * 587 + b * 114) / 1000

def get_luminance(color):
    """ 返回颜色的感知亮度

    https://www.w3.org/TR/2008/REC-WCAG20-20081211/#contrast-ratiodef

    Parameters
    ----------
    color : str

    Returns
    -------
    float
        返回颜色的感知亮度，范围在 0 - 1 之间

    See Also
    --------
    to_r_g_b

    Notes
    -----
    不关心 Alpha 通道
    """
    r, g, b = to_r_g_b(color)
    Rs = r / 255
    Gs = g / 255
    Bs = b / 255
    if Rs <= 0.03928:
        R = Rs / 12.92
    else:
        R = math.pow(((Rs + 0.055) / 1.055), 2.4)
    if Gs <= 0.03928:
        G = Gs / 12.92
    else:
        G = math.pow(((Gs + 0.055) / 1.055), 2.4)
    if Bs <= 0.03928:
        B = Bs / 12.92
    else:
        B = math.pow(((Bs + 0.055) / 1.055), 2.4)

    return (0.2126 * R) + (0.7152 * G) + (0.0722 * B)

def is_dark(color):
    """ 返回颜色的感知亮度是否为暗

    Parameters
    ----------
    color : str

    Returns
    -------
    bool

    See Also
    --------
    get_brightness

    Notes
    -----
    不关心 Alpha 通道
    """
    return True if get_brightness(color) < 128 else False

def is_light(color):
    """ 返回颜色的感知亮度是否为亮

    Parameters
    ----------
    color : str

    Returns
    -------
    bool

    See Also
    --------
    is_dark

    Notes
    -----
    不关心 Alpha 通道
    """
    return not is_dark(color)

def main():
    pass

if __name__ == '__main__':
    main()
