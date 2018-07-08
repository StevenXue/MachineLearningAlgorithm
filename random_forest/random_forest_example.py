from __future__ import division, print_function

from sklearn import datasets

from models.random_forest_model import RandomForest
from utils import Plot, accuracy_score, train_test_split


def main():
    data = datasets.load_digits()
    X = data.data
    y = data.target

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, seed=2)
    print("X_train.shape:", X_train.shape)
    print("Y_train.shape:", y_train.shape)

    clf = RandomForest(n_estimators=100)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)

    print("Accuracy:", accuracy)

    Plot().plot_in_2d(X_test, y_pred, title="Random Forest", accuracy=accuracy, legend_labels=data.target_names)


if __name__ == "__main__":
    main()
