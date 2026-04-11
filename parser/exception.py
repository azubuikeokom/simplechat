class ParseError(Exception):
    """A Parse Error Type"""
    def __repr__(self) -> str:
        return f'ParseError: Parsing failed. Check Headers and their values'
    def __str__(self) -> str:
        return f'ParseError: Parsing failed. Check Headers and their values'