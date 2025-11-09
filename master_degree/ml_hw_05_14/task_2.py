class ParseError(Exception):
    """ Error while parsing file """

    line_no: int | None
    text: str | None

    def __init__(self, *args, line_no: int | None = None, text: str | None = None):
        super().__init__(*args)
        self.line_no = line_no
        self.text = text

    def __str__(self):
        if self.line_no is None and self.text is None:
            return super().__str__()
        elif self.line_no is not None and self.text is not None:
            return f"cannot parse text on line {self.line_no}: {repr(self.text)}"
        elif not self.line_no == None:
            return f"cannot parse text on line {self.line_no}"
        else:
            return f"cannot parse text: {repr(self.text)}"


if __name__ == "__main__":
    # raise ParseError('some standard message')
    # raise ParseError(line_no=10)
    raise ParseError(text='abc')
    # raise ParseError(line_no=10, text='...')
