import pytest
from fountain import fountain


def ftext2test(charname):
    '''Fountain text with a Character name for testing
    '''
    text = '\n'.join([
        'INT. CASINO - NIGHT',
        '',
        'THE DEALER eyes the new player warily.',
        '',
        charname,
        'Where is that pit boss?'
    ])
    return text


def test_normal():
    '''Normal parse process should not be broken
    '''
    text = ftext2test('JOHN')
    fobj = fountain.Fountain(text)

    el = fobj.elements[0]
    assert el.element_type == 'Scene Heading'

    el = fobj.elements[2]
    assert el.element_type == 'Action'


charnames2test = [
    'JANE DOE',
    '@naomi',
    'BILL (O.S.)',
    'C-3PO',
    'GROUPIE #1',
    "SARAH'S FRIEND",
    'BILL / THE MONSTER',
    'MICHAEL (as DOROTHY)',
]


@pytest.mark.parametrize('charname', charnames2test)
def test_charname(charname: str):
    '''Test various Character names (issue #9)
    '''
    text = ftext2test(charname)
    fobj = fountain.Fountain(text)

    el = fobj.elements[4]
    assert el.element_type == 'Character'
    assert el.element_text == charname.removeprefix('@')
