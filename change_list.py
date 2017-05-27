# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division

from trello import TrelloClient


client = TrelloClient(
    api_key='e73a05be99e7d4462a4caff44e45a4e6',
    api_secret='3530b222957946ecd3be0f331702f22668fe347ce3bce102b7bee83eb5dc4f63',
    token='bc5436395a522050be1d3e3512fa0412a9c03912fa819667f447ba217103384f',
    token_secret='9cea40a007ba33269b2f7cc3fb3148be')

list_id_to = ''
card_id = ''


def move_card(card_id, list_id_from, list_id_to):
    """
    """
    card = client.get_card(card_id)
    card.change_list(list_id_to)
