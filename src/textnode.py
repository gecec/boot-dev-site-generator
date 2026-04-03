from enum import Enum


class Bender(Enum):
    AIR_BENDER = "air"
    WATER_BENDER = "water"
    EARTH_BENDER = "earth"
    FIRE_BENDER = "fire"


class TextType(Enum):
    BOLD = "bold"


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, obj):
        if self.text != obj.text:
            return False
        if self.text_type != obj.text_type:
            return False
        if self.url != obj.url:
            return False
        return True

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
