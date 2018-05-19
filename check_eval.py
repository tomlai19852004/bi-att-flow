import pickle
import gzip

if __name__ == "__main__":
    with gzip.open("out/basic/01/eval/dev-001000.pklz", "rb") as f:
        p = pickle.load(f)
        # print(p)
        # print(type(p))

        for key, items in p.items():
            print(key)
            print(type(items))