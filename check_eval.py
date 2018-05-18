import pickle


if __name__ == "__main__":
    with open("out/basic/18/eval/dev-001000.pklz", "r") as f:
        p = pickle.load(f)
        print(p)
        print(type(p))