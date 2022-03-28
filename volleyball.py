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

    def get_player_rating(self):
        return self.rating

sausage = Player('sausage', .1)
bratwurst = Player('bratwurst', .2)
hamburger = Player('hamburger', .3)
cheeseburger = Player('cheeseburger', .4)


class Team:
    def __init__(self, team_name, players):
        self.team_name = team_name
        self.players = players

    def get_players(self):
        return self.players


team_a = Team('hotdog', [sausage, bratwurst])
team_b = Team('burger', [hamburger, cheeseburger])



class VolleyballGame:

    def __init__(self, team_a, team_b):
        self.team_a = team_a
        self.team_b = team_b
        self.service_order = []

    def get_service_order(self):
        # determine first serving player and subsequent service order
        for index in range(len(self.team_a)):
            self.service_order.append(self.team_a.players[index])
            self.service_order.append(self.team_b.players[index])

    def play(self):
        a_score = 0
        b_score = 0
        server_index = 0
        winner = None

        self.get_service_order()

        # serving team serves until the other team gets a point

        # determine first server
        # determine index at which the serving player sits in service order
        server_index = random.choice(range(len(self.service_order)))


        # need to get the rating of the serving player, player.rating
        player_rating = 0


        '''
        for player in team_a.get_players():
            print(player.get_player_rating())
            '''

        for a_player in self.service_order:
            team = None

            if a_player.name in self.team_a.players:
                team = self.team_a

            else:
                team = self.team_b

        while True:

            if random.random() < player_rating:
                # heads - team a gets ball
                a_score += 1

            else:
                # tails - team b gets ball
                b_score += 1

            if a_score == 15 or b_score == 15:
                if abs(a_score - b_score) >= 2:
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


#game = VolleyballGame(team_a, team_b)
#game.play()

