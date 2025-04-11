"""Train test split"""

from sklearn.model_selection import train_test_split


def make_train_test_split(x, y):

    (x_train, x_test, y_train, y_test) = train_test_split(
        x,
        y,
        test_size=0.25,
        random_state=123456,
    )
    return x_train, x_test, y_train, y_test
