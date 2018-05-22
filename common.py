import attr

@attr.s
class Item:
    title = attr.ib()
    text = attr.ib()
