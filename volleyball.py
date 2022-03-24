# Simulation of volleyball!
#
# game to 15
# cap at 21
# win by 2 points
# 2 vs 2
# each person is a 50% chance of scoring
#
import random

sausage = Player('sausage', .1)
bratwurst = Player('bratwurst', .2)
hamburger = Player('hamburger', .3)
cheeseburger = Player('cheeseburger', .4)


class Team():
    def __init__(self, team_name):
        self.team_name = team_name


team_a = Team('hotdog', [sausage, bratwurst])
team_b = Team('burger', [hamburger, cheeseburger])



class VolleyballGame():

    def __init__(self, team_a, team_b):
        self.team_a = team_a
        self.team_b = team_b

    def play(self):
        a_score = 0
        b_score = 0
        winner = None

        while True:
            # serving team serves until the other team gets a point
            if random.random() < .5:
                # heads
                a_score += 1
            else:
                # tails
                b_score += 1

            if abs(a_score-b_score) >= 2:

                if a_score == 15 or b_score == 15:
                    if a_score > b_score:
                        winner = self.team_a
                        print(a_score, 'vs.', b_score)
                    else:
                        winner = self.team_b
                        print(b_score, 'vs.', a_score)
                    break
                elif a_score == 21 or b_score == 21:
                    if a_score > b_score:
                        winner = self.team_a
                        print(a_score, 'vs.', b_score)
                    else:
                        winner = self.team_b
                        print(b_score, 'vs.', a_score)
                    break

        print(winner.team_name)


game = VolleyballGame(team_a, team_b)
game.play()
