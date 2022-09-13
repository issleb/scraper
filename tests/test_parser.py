import parser


def test_first():
    DATA = '<P><A HREF="/reviews/reviewsa-d/abyss.htm">The Abyss</A> (1989) **½</P>'
    result =  parser.get_movie(DATA)

    print(result)

    assert result.title == "The Abyss"
    assert result.link == "/reviews/reviewsa-d/abyss.htm"
    assert result.year == "1989"
    assert result.rating == "**½"

def test_second():
    DATA = '<P><A HREF="/reviews/reviewsa-d/agent69jenseninthesignofscorpio.htm">Agent 69 Jensen: In the Sign of Scorpio/Emmanuelle in Denmark/Agent 69 Jensen: I Skorpionens Tegn</A> (1977) -**</P>'
    result =  parser.get_movie(DATA)

    print(result)

    assert result.title == "Agent 69 Jensen: In the Sign of Scorpio/Emmanuelle in Denmark/Agent 69 Jensen: I Skorpionens Tegn"
    assert result.link == "/reviews/reviewsa-d/agent69jenseninthesignofscorpio.htm"
    assert result.year == "1977"
    assert result.rating == "-**"

def test_test_thirdfirst():
    DATA = '<P><A HREF="/reviews/reviewsa-d/bloodypitofhorror.htm">Bloody Pit of Horror/Crimson Executioner/The Scarlet Executioner/The Scarlet Hangman/The Red Hangman/Virgins for the Hangman/Some Virgins for the Hangman/A Tale of Torture/The Castle of Artena/Il Castello di Artena/Il Boia Scarlatto</A> (1965) -****</P>'
    result =  parser.get_movie(DATA)

    print(result)

    assert result.title == "Bloody Pit of Horror/Crimson Executioner/The Scarlet Executioner/The Scarlet Hangman/The Red Hangman/Virgins for the Hangman/Some Virgins for the Hangman/A Tale of Torture/The Castle of Artena/Il Castello di Artena/Il Boia Scarlatto"
    assert result.link == "/reviews/reviewsa-d/bloodypitofhorror.htm"
    assert result.year == "1965"
    assert result.rating == "-****"    