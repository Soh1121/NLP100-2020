import pandas as pd
import optuna
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


def logistic_objective(trial):
    C = trial.suggest_loguniform("C", 1e-4, 1e4)
    lr = LogisticRegression(
        penalty="l2",
        random_state=0,
        solver="sag",
        max_iter=10000,
        C=C
    )
    lr.fit(X_train, y_train)
    valid_pred = lr.predict(X_valid)
    valid_accuracy = accuracy_score(y_valid, valid_pred)

    return valid_accuracy


def randomforrest_objective(trial):
    max_depth = trial.suggest_int("max_depth", 1, 20)
    rf = RandomForestClassifier(max_depth=max_depth, random_state=0)
    rf.fit(X_train, y_train)
    valid_pred = rf.predict(X_valid)
    valid_accuracy = accuracy_score(y_valid, valid_pred)

    return valid_accuracy


X_train = pd.read_table("./output/train.feature.txt", header=None)
X_valid = pd.read_table("./output/valid.feature.txt", header=None)
X_test = pd.read_table("./output/test.feature.txt", header=None)
y_train = pd.read_table("./output/train.txt", header=None)[1]
y_valid = pd.read_table("./output/valid.txt", header=None)[1]
y_test = pd.read_table("./output/test.txt", header=None)[1]

logistic_study = optuna.create_study(direction="maximize")
logistic_study.optimize(logistic_objective, timeout=3600)
randomforest_study = optuna.create_study(direction="maximize")
randomforest_study.optimize(randomforrest_objective, timeout=3600)

print("【ロジスティック回帰】")
print("最良結果")
logistic_trial = logistic_study.best_trial
print("Value:", logistic_trial.value)
print("params:")
for key, value in logistic_trial.params.items():
    print("     {}: {}".format(key, value))

print("【ランダムフォレスト】")
print("最良結果")
randomforest_trial = randomforest_study.best_trial
print("Value:", randomforest_trial.value)
print("params:")
for key, value in randomforest_trial.params.items():
    print("     {}: {}".format(key, value))
