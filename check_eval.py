import pickle
import gzip

if __name__ == "__main__":
    with gzip.open("out/basic/18/eval/dev-001000.pklz", "rb") as f:
        p = pickle.load(f)
        print(p)
        print(type(p))
