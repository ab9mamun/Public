import random_generator as gen

'''
Let's consider a circle with its center at (0,0) and radius being 0.5 unit. This circle is inscribed in a square.
Each side of the square is parallel to either X axis or Y axis.
_________
|       |
|       |
|       |
---------
We'll generate some random points inside the square.
Then pi = 4 * Number of points inside the circle / Number of points inside the square
'''


class State:
    def __init__(self):
        self.inside = 0
        self.total = 0
        self.pi = 0

    def update(self, x, y):
        print('Point:(%0.3lf, %0.3lf)' % (x, y), end='')
        self.total += 1
        d2 = distance2_from_center(x, y)
        if d2 < 0.5*0.5:
            self.inside += 1
            print(' | inside', end='')
        else:
            print(' | outside', end='')
        print()

    def finish(self):
        if self.total != 0:
            self.pi = 4*self.inside/self.total

    def printResults(self):
        print('\n============================================')
        print('SimulatedPi Results:')
        print('============================================')
        print('Total points:', self.total, 'Inside circle:', self.inside)
        print('Value of pi:', self.pi)


# returns square of the distance between the points
def distance2(x1, y1, x2, y2):
    return (x1-x2)*(x1-x2) + (y1-y2)*(y1-y2)


def distance2_from_center(x, y):
    return x*x + y*y


def run_experiment(iterations):
    state = State()
    for i in range(iterations):
        x = gen.uniform() - 0.5
        y = gen.uniform() - 0.5
        state.update(x, y)
    state.finish()
    state.printResults()


def main():
    run_experiment(25000)
    print('Simulation Complete')


if __name__ == "__main__":
    main()
