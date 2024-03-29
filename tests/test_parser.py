import scraper.parser

def test_1():
    DATA = '<P><A HREF="/reviews/reviewsa-d/abyss.htm">The Abyss</A> (1989) **½</P>'
    result =  scraper.parser.get_movie(DATA)

    assert result.title == "The Abyss"
    assert result.link == "/reviews/reviewsa-d/abyss.htm"
    assert result.year == "1989"
    assert result.rating == "**½"
    assert result.name == "abyss"

def test_2():
    DATA = '<P><A HREF="/reviews/reviewsa-d/agent69jenseninthesignofscorpio.htm">Agent 69 Jensen: In the Sign of Scorpio/Emmanuelle in Denmark/Agent 69 Jensen: I Skorpionens Tegn</A> (1977) -**</P>'
    result =  scraper.parser.get_movie(DATA)

    assert result.title == "Agent 69 Jensen: In the Sign of Scorpio/Emmanuelle in Denmark/Agent 69 Jensen: I Skorpionens Tegn"
    assert result.link == "/reviews/reviewsa-d/agent69jenseninthesignofscorpio.htm"
    assert result.year == "1977"
    assert result.rating == "-**"
    assert result.name == "agent69jenseninthesignofscorpio"

def test_3():
    DATA = '<P><A HREF="/reviews/reviewsa-d/bloodypitofhorror.htm">Bloody Pit of Horror/Crimson Executioner/The Scarlet Executioner/The Scarlet Hangman/The Red Hangman/Virgins for the Hangman/Some Virgins for the Hangman/A Tale of Torture/The Castle of Artena/Il Castello di Artena/Il Boia Scarlatto</A> (1965) -****</P>'
    result =  scraper.parser.get_movie(DATA)

    assert result.title == "Bloody Pit of Horror/Crimson Executioner/The Scarlet Executioner/The Scarlet Hangman/The Red Hangman/Virgins for the Hangman/Some Virgins for the Hangman/A Tale of Torture/The Castle of Artena/Il Castello di Artena/Il Boia Scarlatto"
    assert result.link == "/reviews/reviewsa-d/bloodypitofhorror.htm"
    assert result.year == "1965"
    assert result.rating == "-****"
    assert result.name == "bloodypitofhorror"

def test_bigp():
    DATA = '<P><TABLE WIDTH="100%"><TR><TD WIDTH="5%"></TD><TD WIDTH="95%"><P><A HREF="/reviews/reviewsa-d/aliens.htm">Aliens</A> (1986) *****</P>'
    result =  scraper.parser.get_movie(DATA)

    assert result.title is None
    assert result.link is None
    assert result.year is None
    assert result.rating is None
    assert result.name is None

def test_doubleyear():
    DATA = '<P><A HREF="/reviews/reviewsa-d/afterdeath.htm">After Death/Zombie 4: After Death/Zombie Flesh Eaters 3/Oltre la Morte</A> (1988/1990) -**</P>'
    result =  scraper.parser.get_movie(DATA)

    assert result.title == "After Death/Zombie 4: After Death/Zombie Flesh Eaters 3/Oltre la Morte"
    assert result.link == "/reviews/reviewsa-d/afterdeath.htm"
    assert result.year == "1988/1990"
    assert result.rating == "-**"
    assert result.name == "afterdeath"

def test_encoding():
    DATA = '<P><A HREF="/reviews/reviewse-g/georgesmeliestrickfilms1900.htm">Addition and Subtraction/Tom Whiskey, ou L’Illusioniste Toqué</A> (1900) [unratable]</P>'
    result =  scraper.parser.get_movie(DATA)

    assert result.title == "Addition and Subtraction/Tom Whiskey, ou L’Illusioniste Toqué"
    assert result.link == "/reviews/reviewse-g/georgesmeliestrickfilms1900.htm"
    assert result.year == "1900"
    assert result.rating == "[unratable]"
    assert result.name == "georgesmeliestrickfilms1900"    

    