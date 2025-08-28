from ClassBraggModel import BraggModel

if __name__ == '__main__':
    ## Brag model calculations
    theta = 0
    d = 550
    m = 4
    bm1 = BraggModel(theta, d, m)

    lamb_min = 200.
    lamb_max = 800.
    amount = 1000
    bm1.plot_intensity_interval(lamb_min, lamb_max, amount)