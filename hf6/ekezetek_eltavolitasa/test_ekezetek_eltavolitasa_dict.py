from ekezetek_eltavolitasa_dict import ekezet_eltavolit


def test_ekezet_eltavolit():
    assert ekezet_eltavolit('áéíóöőúüűÁÉÍÓÖŐÚÜŰ') == 'aeiooouuuAEIOOOUUU'
    assert ekezet_eltavolit('árvíztűrő tükörfúrógép') == 'arvizturo tukorfurogep'
    assert ekezet_eltavolit('alma') == 'alma'
