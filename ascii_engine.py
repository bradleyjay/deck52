def ascii_printer(self, selection):

    ace_clubs = r'''
    .-------.
    |A      |
    |       |
    |   ♣   |
    |       |
    |      A|
    `-------´
    '''

    two_clubs = r'''
    .-------.
    |2      |
    |   ♣   |
    |       |
    |   ♣   |
    |      2|
    `-------´
    '''

    three_clubs = r'''
    .-------.
    |3      |
    |   ♣   |
    |   ♣   |
    |   ♣   |
    |      3|
    `-------´
    '''

    four_clubs = r'''
    .-------.
    |4      |
    |  ♣ ♣  |
    |       |
    |  ♣ ♣  |
    |      4|
    `-------´
    '''

    five_clubs = r'''
    .-------.
    |5      |
    |  ♣ ♣  |
    |   ♣   |
    |  ♣ ♣  |
    |      5|
    `-------´
    '''

    six_clubs = r'''
    .-------.
    |6      |
    |  ♣ ♣  |
    |  ♣ ♣  |
    |  ♣ ♣  |
    |      6|
    `-------´
    '''

    two_diamonds = r'''
    .-------.
    |2      |
    |   ♦   |
    |       |
    |   ♦   |
    |      2|
    `-------´
    '''

    # cards = ace_clubs, two_clubs, three_clubs, four_clubs

    spacer = ' ' * 5  # Space between cards.
    card_images = []
    
    # for card in selection:
        
    

    for chunks in zip(*(card.splitlines() for card_image in card_images)):
        print(spacer.join(chunks))

# ____________

card_dict ={
    "ace_clubs": r'''
    .-------.
    |A      |
    |       |
    |   ♣   |
    |       |
    |      A|
    `-------´
    ''',

    "two_clubs": r'''
    .-------.
    |2      |
    |   ♣   |
    |       |
    |   ♣   |
    |      2|
    `-------´
    '''
}

spacer = ' ' * 5  # Space between cards.
card_images = [card_dict["ace_clubs"], card_dict["two_clubs"]]

for chunks in zip(*(card_image.splitlines() for card_image in card_images)):
        print(spacer.join(chunks))

