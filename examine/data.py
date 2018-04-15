import json
import time

def get_data():
    with open("data/squad/train-v1.1.json", "r") as f:
        json_content = json.load(f)
        return json_content

if __name__ == "__main__":
    start_time = time.time()

    data = get_data()

    print(len(data["data"]))
    #  data["data"][0]['paragraphs'][0]
        



    print("Program execution time")
    print(time.time() - start_time)