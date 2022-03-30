# Simulation of volleyball!
#
# game to 15
# cap at 21
# win by 2 points
# 2 vs 2
# each person is a 50% chance of scoring
#
import random


class Player:
    def __init__(self, name, rating):
        self.name = name
        self.rating = rating


sausage = Player('sausage', .1)
bratwurst = Player('bratwurst', .2)
hamburger = Player('hamburger', .3)
cheeseburger = Player('cheeseburger', .4)


class Team:
    def __init__(self, name, players):
        self.name = name
        self.players = players
        self.score = 0


team_a = Team('hotdog', [sausage, bratwurst])
team_b = Team('burger', [hamburger, cheeseburger])


class VolleyballGame:
    def __init__(self, team_a, team_b):
        self.team_a = team_a
        self.team_b = team_b

    def play(self):
        winner = None

        playing_team = random.choice([self.team_a, self.team_b])

        while True:
            # The volley logic
            # Pick the player (find the rating)
            playing_player = random.choice(playing_team.players)
            if playing_player.rating > random.random():
                # the player just scored for their team
                playing_team.score += 1
            else:
                # the player just bungled it for their team
                # do 2 things:
                # 1: give the other team a point
                # 2: need to swap the playing_team
                opponent = None
                if playing_team.name == self.team_a.name:
                    opponent = self.team_b
                else:
                    opponent = self.team_a

                opponent.score += 1
                playing_team = opponent

            # The scoring logic?
            # LEAVE THIS ALONE
            if self.team_a.score == 15 or self.team_b.score == 15:
                if abs(self.team_a.score - self.team_b.score) >= 2:
                    if self.team_a.score > self.team_b.score:
                        winner = self.team_a
                        print(self.team_a.score, 'vs.', self.team_b.score)
                    else:
                        winner = self.team_b
                        print(self.team_b.score, 'vs.', self.team_a.score)
                    break
            elif self.team_a.score == 21 or self.team_b.score == 21:
                if self.team_a.score > self.team_b.score:
                    winner = self.team_a
                    print(self.team_a.score, 'vs.', self.team_b.score)
                else:
                    winner = self.team_b
                    print(self.team_b.score, 'vs.', self.team_a.score)
                break

        print(winner.name)


game = VolleyballGame(team_a, team_b)
game.play()
