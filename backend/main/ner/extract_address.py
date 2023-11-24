from natasha import (
    MorphVocab,
    AddrExtractor
)

morph_vocab = MorphVocab()
addr_extractor = AddrExtractor(morph_vocab)

priorities = {
    'region': 0,
    'area': 1,
    'settlement': 2,
    'street': 3,
    'building': 4
}

types = {
    'region': ['республика', 'край', 'область', 'автономный округ'],
    'area': ['район'],
    'settlement': ['город', 'деревня', 'село', 'посёлок'],
    'street': ['улица', 'проезд', 'проспект', 'переулок', 'площадь', 'шоссе', 'набережная', 'бульвар'],
    'building': ['дом', 'корпус', 'строение', 'офис', 'квартира']
}

types_reverse = {
    value: key for key, values in types.items() for value in values
}


def extract_addresses(text: str) -> list[dict]:
    
    def _match_dist_type(m1, m2):
        return abs(priorities[types_reverse[m1.fact.type]] - priorities[types_reverse[m2.fact.type]])

    def _match_dist_char(m1, m2):
        if m1.stop < m2.start:
            return m2.start - m1.stop
        elif m2.stop < m1.start:
            return m1.start - m2.stop
        else:
            return 0

    def _dist(m1, m2):
        if _match_dist_type(m1, m2) == 0:
            return float('+inf')
        else:
            return _match_dist_char(m1, m2) * _match_dist_type(m1, m2)

    matches = list(addr_extractor(text))

    clusters = []
    for match in filter(lambda m: m.fact.type in types_reverse, matches):
        for cluster in clusters:
            dist = _dist(match, cluster[0])
            if dist < 40:
                cluster.append(match)
                break
        else:
            clusters.append([match])

    addresses = []
    for cluster in clusters:
        addr = {}
        for match in cluster:
            addr[types_reverse[match.fact.type]] = ' '.join([match.fact.type, match.fact.value])
        addresses.append(addr)

    return addresses


def extract_address_query(text: str) -> dict:
    match = addr_extractor.find(text)

    if match is None:
        return {}

    return {
        types_reverse[fact.type]: ' '.join([fact.type, fact.value])
        for fact in match.fact
        if fact.type in types_reverse
    }
