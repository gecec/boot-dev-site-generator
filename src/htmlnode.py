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

        result = ""
        for k, v in self.props.items():
            result = result + f' {k}="{v}"'

        return result


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super(LeafNode, self).__init__(self, tag, value, props)
        self.tag = tag
        self.value = value
        self.props = props

    def to_html(self):
        if self.value is None:
            raise ValueError("Value is not set")

        if self.tag is None:
            return self.value

        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props_to_html()})"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super(ParentNode, self).__init__(self, tag, children, props)
        self.tag = tag
        self.children = children
        self.props = props

    def to_html(self):
        if self.tag is None:
            raise ValueError("Tag is not set")
        if self.children is None:
            raise ValueError("Children are not set")

        result = f"<{self.tag}{self.props_to_html()}>"
        for child in self.children:
            result = result + child.to_html()

        result = result + f"</{self.tag}>"
        return result
