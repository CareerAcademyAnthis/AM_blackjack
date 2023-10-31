def build(values, suites):
    deck = []
    for suite in suites:
        for value in values:
            deck.append([value, suite])
    return deck
