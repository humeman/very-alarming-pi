from enum import IntEnum

class Colors:
    # Primary colors
    RED = 0xFF0000
    GREEN = 0x00FF00
    BLUE = 0x0000FF

    # Secondary colors (mixing primary)
    YELLOW = 0xFFFF00
    CYAN = 0x00FFFF
    MAGENTA = 0xFF00FF

    # Tertiary colors (mixing primary and secondary)
    ORANGE = 0xFFA500
    LIME = 0x33FF33
    TEAL = 0x008080
    VIOLET = 0xEE82EE
    INDIGO = 0x4B0082
    PURPLE = 0x800080

    # Grayscale
    WHITE = 0xFFFFFF
    BLACK = 0x000000
    GRAY = 0x808080
    LIGHT_GRAY = 0xD3D3D3
    DARK_GRAY = 0xA9A9A9

    # Shades of Red
    DARK_RED = 0x8B0000
    MAROON = 0x800000
    CRIMSON = 0xDC143C
    FIREBRICK = 0xB22222
    INDIAN_RED = 0xCD5C5C

    # Shades of Green
    DARK_GREEN = 0x006400
    FOREST_GREEN = 0x228B22
    SEA_GREEN = 0x2E8B57
    OLIVE = 0x808000
    DARK_OLIVE_GREEN = 0x556B2F

    # Shades of Blue
    DARK_BLUE = 0x00008B
    NAVY = 0x000080
    MIDNIGHT_BLUE = 0x191970
    ROYAL_BLUE = 0x4169E1
    CORNFLOWER_BLUE = 0x6495ED

    # Shades of Yellow
    GOLD = 0xFFD700
    KHAKI = 0xF0E68C
    DARK_KHAKI = 0xBDB76B
    GOLDENROD = 0xDAA520

    # Shades of Cyan
    AQUA = 0x00FFFF  # Same as CYAN
    AQUAMARINE = 0x7FFFD4
    TURQUOISE = 0x40E0D0
    LIGHT_CYAN = 0xE0FFFF

    # Shades of Magenta
    PINK = 0xFFC0CB
    HOT_PINK = 0xFF69B4
    DEEP_PINK = 0xFF1493
    ORCHID = 0xDA70D6
    THISTLE = 0xD8BFD8

    # Browns
    BROWN = 0xA52A2A
    SADDLE_BROWN = 0x8B4513
    SIENNA = 0xA0522D
    CHOCOLATE = 0xD2691E
    PERU = 0xCD853F

    # Pastels
    LIGHT_PINK = 0xFFB6C1
    LIGHT_YELLOW = 0xFFFFE0
    LIGHT_BLUE = 0xADD8E6
    LIGHT_GREEN = 0x90EE90
    LIGHT_CORAL = 0xF08080

    # Additional colors
    SALMON = 0xFA8072
    TOMATO = 0xFF6347
    LAVENDER = 0xE6E6FA
    SLATE_GRAY = 0x708090
    STEEL_BLUE = 0x4682B4