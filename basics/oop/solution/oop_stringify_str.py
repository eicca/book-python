DATA = [
    (4.7, 3.2, 1.3, 0.2, 'setosa'),
    (7.0, 3.2, 4.7, 1.4, 'versicolor'),
    (7.6, 3.0, 6.6, 2.1, 'virginica'),
]


class Iris:
    def __init__(self, features, label):
        self.features = features
        self.label = label

    def total(self):
        return sum(features)

    def __str__(self):
        return f'{self.label} {self.total():.1f}'


for *features, label in DATA:
    iris = Iris(features, label)
    print(iris)

# setosa 9.4
# versicolor 16.3
# virginica 19.3
