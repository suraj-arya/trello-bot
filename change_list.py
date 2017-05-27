# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division

from trello import TrelloClient


client = TrelloClient(
    api_key='',
    api_secret='',
    token='',
    token_secret='')

list_id_to = ''
card_id = ''


def move_card(card_id, list_id_from, list_id_to):
    """
    """
    card = client.get_card(card_id)
    card.change_list(list_id_to)
