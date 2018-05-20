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
        如果颜色为 16 进制格式色值，则返回 'Hex'
        如果颜色为 RGB 格式色值，则返回 'RGB'

    Notes
    -----
    关心 Alpha 通道

    Raise
    -----
    RuntimeError: Not a color!
    """
    color = _color_strip(color)

    if re.match(r'(^#[a-f0-9]{6}$)|(^#[a-f0-9]{3}$)', color, re.I) != None:
        return 'Hex'
    elif re.match(r'(^rgb\((25[0-5]|2[0-4][0-9]|[0-1]?[0-9]?[0-9]),(25[0-5]|2[0-4][0-9]|[0-1]?[0-9]?[0-9]),(25[0-5]|2[0-4][0-9]|[0-1]?[0-9]?[0-9])\))', color, re.I) != None:
        return 'RGB'
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
    """ 将短十六进制色值（三位）转换为长十六进制色值（六位）

    如果参数不是十六进制色值，则抛出一个 RuntimeError

    Parameters
    ----------
    color : str

    Returns
    -------
    str
        返回转换后的十六进制色值，字母为大写字母

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

def to_hex(color):
    """ 将颜色转换为十六进制色值

    Parameters
    ----------
    color : str

    Returns
    -------
    str
        返回转换后的十六进制色值，字母为大写字母

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
