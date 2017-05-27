# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division

from trello import TrelloClient
import os


client = TrelloClient(
    api_key=os.environ.get('TRELLO_API_KEY'),
    api_secret=os.environ.get('TRELLO_SECRET_KEY'),
    token=os.environ.get('TRELLO_OAUTH_TOKEN'),
    token_secret=os.environ.get('TRELLO_TOKEN_SECRET'))


def move_card(card_id, list_id_to):
    """
    """
    card = client.get_card(card_id)
    card.change_list(list_id_to)
