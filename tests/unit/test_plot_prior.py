
import numpy as np
import matplotlib.pyplot as plt
from probflow import *

PLOT = False
epochs = 1
N = 10


def test_plot_prior_scalar():
    """Tests Parameter.plot_prior and BaseDistribution.plot_prior"""

    # Linear regression w/ 2 scalar variables
    weight = Parameter(name='the_weight', estimator='flipout')
    bias = Parameter(name='the_bias', estimator='flipout')
    model = Normal(Input()*weight + bias, 1.0)

    true_weight = 0.5
    true_bias = -1.0

    x = np.linspace(-5, 5, N)
    y = true_weight*x + true_bias + np.random.randn(N)

    model.fit(x, y, epochs=epochs)

    # Plot just the weight's prior w/ a teensy bandwidth
    weight.plot_prior(style='fill')
    if PLOT:
        plt.show()

    # Plot just the bias' prior w/ a yuge bandwidth
    bias.plot_prior(style='fill', ci=0.95)
    if PLOT:
        plt.show()

    # Plot all the model's priors w/ [hist, 1col, no_ci]
    model.plot_prior(style='hist')
    if PLOT:
        plt.show()

    # Plot all the model's priors w/ [hist, 2cols, no_ci]
    model.plot_prior(style='hist', cols=2)
    if PLOT:
        plt.show()

    # Plot all the model's priors w/ [hist, 1col, ci]
    model.plot_prior(style='hist', ci=0.9)
    if PLOT:
        plt.show()

    # Plot all the model's priors w/ [hist, 2cols, ci]
    model.plot_prior(style='hist', cols=2, ci=0.9)
    if PLOT:
        plt.show()

    # Plot all the model's priors w/ [line, 1col, no_ci]
    model.plot_prior(style='line')
    if PLOT:
        plt.show()

    # Plot all the model's priors w/ [line, 1col, ci]
    model.plot_prior(style='line', ci=0.95)
    if PLOT:
        plt.show()

    # Plot all the model's priors w/ [fill, 1col, no_ci]
    model.plot_prior(style='fill')
    if PLOT:
        plt.show()

    # Plot all the model's priors w/ [fill, 1col, ci]
    model.plot_prior(style='fill', ci=0.95)
    if PLOT:
        plt.show()

    # Default should be fill, 1col, no ci
    model.plot_prior()
    if PLOT:
        plt.show()


def test_plot_prior_vector():
    """Tests Parameter.plot_prior and BaseDistribution.plot_prior"""

    # Multivariate linear regression
    Nd = 3
    weight = Parameter(shape=Nd, estimator=None)
    bias = Parameter(estimator=None)
    std_dev = ScaleParameter()
    model = Normal(Dot(Input(), weight) + bias, std_dev)

    # Generate data
    true_weight = np.array([0.5, -0.25, 0.0])
    true_bias = -1.0
    noise = np.random.randn(N, 1)
    x = np.random.randn(N, Nd)
    y = np.expand_dims(np.sum(true_weight*x, axis=1) + true_bias, 1) + noise

    model.fit(x, y, epochs=epochs)

    # Plot all the model's priors w/ [hist, 1col, no_ci]
    model.plot_prior(style='line')
    if PLOT:
        plt.show()

    # Plot all the model's priors w/ [hist, 2col, no_ci]
    model.plot_prior(style='fill', ci=0.95, cols=2)
    if PLOT:
        plt.show()


if __name__ == "__main__":
    PLOT = True
    epochs = 1000
    N = 1000
    test_plot_prior_scalar()
    test_plot_prior_vector()
