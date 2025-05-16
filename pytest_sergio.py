import pytest
from prova_escrita_05 import llibres_per_categoria, esta_disponible, usuari_te_prestecs, dies_prestec_total

@pytest.mark.parametrize("biblioteca, categoria, expected", [
    ([
        {"llibre": "El Quixot", "categoria": "novel·la", "prestecs": []},
        {"llibre": "1984", "categoria": "ciència-ficció", "prestecs": []}
    ], "novel·la", ["El Quixot"]),
    ([
        {"llibre": "1984", "categoria": "ciència-ficció", "prestecs": []},
        {"llibre": "El Senyor dels Anells", "categoria": "fantasia", "prestecs": []}
    ], "fantasia", ["El Senyor dels Anells"]),
    ([
        {"llibre": "Crim i Càstig", "categoria": "novel·la", "prestecs": []}
    ], "assaig", [])
])
def test_llibres_per_categoria(biblioteca, categoria, expected):
    """
    Test per a la funció llibres_per_categoria.
    Verifica que retorna els llibres de la categoria especificada.
    """
    assert llibres_per_categoria(biblioteca, categoria) == expected

@pytest.mark.parametrize("biblioteca, llibre, expected", [
    ([
        {"llibre": "El Quixot", "prestecs": [{"usuari": "Joan", "retornat": True}]}
    ], "El Quixot", True),
    ([
        {"llibre": "1984", "prestecs": [{"usuari": "Pere", "retornat": False}]}
    ], "1984", False),
    ([
        {"llibre": "El Senyor dels Anells", "prestecs": []}
    ], "El Senyor dels Anells", True)
])
def test_esta_disponible(biblioteca, llibre, expected):
    """
    Test per a la funció esta_disponible.
    Verifica si un llibre està disponible.
    """
    assert esta_disponible(biblioteca, llibre) == expected

@pytest.mark.parametrize("biblioteca, usuari, expected", [
    ([
        {"llibre": "El Quixot", "prestecs": [{"usuari": "Joan", "retornat": False}]}
    ], "Joan", True),
    ([
        {"llibre": "1984", "prestecs": [{"usuari": "Pere", "retornat": True}]}
    ], "Pere", False),
    ([
        {"llibre": "El Senyor dels Anells", "prestecs": []}
    ], "Maria", False)
])
def test_usuari_te_prestecs(biblioteca, usuari, expected):
    """
    Test per a la funció usuari_te_prestecs.
    Verifica si un usuari té llibres pendents de retornar.
    """
    assert usuari_te_prestecs(biblioteca, usuari) == expected

@pytest.mark.parametrize("biblioteca, llibre, expected", [
    ([
        {"llibre": "El Quixot", "prestecs": [{"usuari": "Joan", "dies": 10}, {"usuari": "Maria", "dies": 15}]}
    ], "El Quixot", 25),
    ([
        {"llibre": "1984", "prestecs": [{"usuari": "Pere", "dies": 20}]}
    ], "1984", 20),
    ([
        {"llibre": "El Senyor dels Anells", "prestecs": []}
    ], "El Senyor dels Anells", 0)
])
def test_dies_prestec_total(biblioteca, llibre, expected):
    """
    Test per a la funció dies_prestec_total.
    Verifica el total de dies que un llibre ha estat prestat.
    """
    assert dies_prestec_total(biblioteca, llibre) == expected
