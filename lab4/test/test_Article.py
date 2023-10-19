import pytest

from lab4.Article import Article


@pytest.mark.parametrize("theme, length, oththeme, othlength, res", [
    ("qwe", 12, "qwe", 12, True), ("qwe", 12, "qwe", 15, False),
    ("qwe", 12, "qwer", 12, False)
])
def test_eq(theme,length,oththeme,othlength, res):
    Ar = Article(theme,length)
    Aroth = Article(oththeme,othlength)
    assert (Ar.__eq__(Aroth)) == res


@pytest.mark.parametrize("theme, length, error", [
    ("qwe", -1, ValueError), ("qwe", "qw", TypeError), ("qwe", "12", TypeError)])
def test_error_Article_Init(theme, length, error):
    with pytest.raises(error):
        Article(theme, length)
