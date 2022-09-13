import parser


def test_first():
    DATA = '<P><A HREF="/reviews/reviewsa-d/abyss.htm">The Abyss</A> (1989) **½</P>'
    result =  parser.get_movie(DATA)

    print(result)

    assert result.title == "The Abyss"
    assert result.year == "1989"