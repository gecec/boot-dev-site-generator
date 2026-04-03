from ast import Return


class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.props_to_html()}, {self.children})"

    def __eq__(self, obj):
        if obj.tag != self.tag:
            return False

        if obj.value != self.value:
            return False

        if obj.children != self.children:
            return False

        if obj.props != self.props:
            return False

        return True

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props is None:
            return ""

        result = " "
        for k, v in self.props.items():
            result = result + f'{k}="{v}" '

        return result
