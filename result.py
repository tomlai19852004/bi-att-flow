import json
import time

def get_result(version="020000"):
    with open('out/basic/00/answer/test-'+version+".json", 'r') as f:
        json_content = json.load(f)
        return json_content

if __name__ == "__main__":
    start_time = time.time()
    
    result = get_result()

    result_scores = result["scores"]
    print(len(list(result_scores.keys())))
    print(len(list(result.keys())))

    counter = 0
    for key, val in result.items():
        if key != "scores":
            print(key)
            print(val)
            print(result_scores[key])
            print("\n\n")
            counter += 1
        
        if counter > 3:
            break

    print("Program execution time")
    print(time.time() - start_time)