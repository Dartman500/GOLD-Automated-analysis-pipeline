import numpy as np
from sklearn.ensemble import RandomForestClassifier

def train_model(X, y):
    model = RandomForestClassifier()
    model.fit(X, y)
    return model

def example():
    X = np.random.rand(100, 3)
    y = (X[:,0] + X[:,1] > 1).astype(int)
    model = train_model(X, y)
    print("Model trained for EIA crest detection example")

if __name__ == "__main__":
    example()
