import joblib


lr = joblib.load("./output/model.joblib")
vocabulary = joblib.load("./output/vocabulary_.joblib")
coefs = lr.coef_

for coef in coefs:
    d = dict(zip(vocabulary, coef))
    d_sorted = sorted(d.items(), key=lambda x: x[1], reverse=True)
    d_height = d_sorted[:10]
    d_low = d_sorted[-10:]
    print(d_height)
    print(d_low)
