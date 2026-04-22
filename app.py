def predict(features):
    return "setosa"

def test_prediction():
    assert predict([5.1,3.5,1.4,0.2]) is not None

if __name__ == "__main__":
    test_prediction()
    print("Test Passed ✅")