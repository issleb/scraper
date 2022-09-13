import parser


def test_first():
    DATA = '<P><A HREF="/reviews/reviewsa-d/abyss.htm">The Abyss</A> (1989) **½</P>'
    result =  parser.get_movie(DATA)

    assert result.year == "1989"