import copy
import random
# Consider using the modules imported above.


class Hat:

    def __init__(self, **colors):
        self.contents = []
        # for color in colors:
        #     for i in range(color):
        #         self.contents.append(f'{color}')

        for key, value in colors.items():
            # print("%s == %s" % (key, value))
            for i in range(value):
                self.contents.append(f'{key}')

    def draw(self, number_of_balls):
        """
            randomly removes a set number of balls
        :param number_of_balls:
        :return:
        """
        drawn_balls = []
        if number_of_balls <= len(self.contents):
            for _ in range(number_of_balls):
                x = random.randint(0, len(self.contents)-1)
                drawn_balls.append(self.contents[x])
                self.contents.remove(drawn_balls[-1])
            return drawn_balls
        else:
            return self.contents


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    """

    :param hat: A hat object containing balls that should be copied inside the function.
    :param expected_balls: An object indicating the exact group of balls to attempt to draw from the hat for the experiment. For example, to determine the probability of drawing 2 blue balls and 1 red ball from the hat, set expected_balls to {"blue":2, "red":1}.
    :param num_balls_drawn: The number of balls to draw out of the hat in each experiment.
    :param num_experiments: The number of experiments to perform.
    :return:
    """
    expected_balls_str = []
    for key, value in expected_balls.items():
        for i in range(value):
            expected_balls_str.append(f'{key}')
    x = 0
    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        temp = hat_copy.draw(num_balls_drawn)
        o = 1
        for ball in expected_balls_str:
            if temp.count(ball) < expected_balls_str.count(ball):
                o = 0
                break
        x += o
    probability = x/num_experiments
    return probability
