# -*- coding: utf-8 -*-

import pytest

from src.tennis import TennisGame1, TennisGame2, TennisGame3
from tests.conftest import test_cases

pytestmark = pytest.mark.tennis


@pytest.mark.parametrize('p1Points p2Points score p1Name p2Name'.split(), test_cases)
def test_get_score_game1(p1Points, p2Points, score, p1Name, p2Name):
    game = play_game(TennisGame1, p1Points, p2Points, p1Name, p2Name)
    assert score == game.score()

@pytest.mark.parametrize('p1Points p2Points score p1Name p2Name'.split(), test_cases)
def test_get_score_game2(p1Points, p2Points, score, p1Name, p2Name):
    game = play_game(TennisGame2, p1Points, p2Points, p1Name, p2Name)
    assert score == game.score()

@pytest.mark.parametrize('p1Points p2Points score p1Name p2Name'.split(), test_cases)
def test_get_score_game3(p1Points, p2Points, score, p1Name, p2Name):
    game = play_game(TennisGame3, p1Points, p2Points, p1Name, p2Name)
    assert score == game.score()

def play_game(TennisGame, p1Points, p2Points, p1Name, p2Name):
    game = TennisGame(p1Name, p2Name)
    for i in range(max(p1Points, p2Points)):
        if i < p1Points:
            game.won_point(p1Name)
        if i < p2Points:
            game.won_point(p2Name)
    return game

#

#
# def test_Score_Game1():
#     for testcase in test_cases:
#         (p1Points, p2Points, score, p1Name, p2Name) = testcase
#         game = play_game(TennisGame1, p1Points, p2Points, p1Name, p2Name)
#         assert score == game.score()
#
# def test_Score_Game2():
#     for testcase in test_cases:
#         (p1Points, p2Points, score, p1Name, p2Name) = testcase
#         game = play_game(TennisGame2, p1Points, p2Points, p1Name, p2Name)
#         assert score == game.score()
#
# def test_Score_Game3():
#     for testcase in test_cases:
#         (p1Points, p2Points, score, p1Name, p2Name) = testcase
#         game = play_game(TennisGame3, p1Points, p2Points, p1Name, p2Name)
#         assert score == game.score()