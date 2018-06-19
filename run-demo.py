from flask import Flask, render_template, redirect, request, jsonify
from squad.demo_prepro import prepro
from basic.demo_cli import Demo
import json
import pymongo
import requests
import os
from dotenv import load_dotenv, find_dotenv

mongo_url = os.environ['MONGO_URL']
paraphrase_url = os.environ['PARAPHRASE_BASE_URL']

app = Flask(__name__)
shared = json.load(open("data/squad/shared_test.json", "r"))
contextss = [""]
context_questions = [[]]
for i in range(len(shared['contextss'])):
    j = 1 if i==0 else 0
    contextss.append(shared["contextss"][i][j])
    context_questions.append(shared['context_questions'][i][j:j+10])
titles = ["Write own paragraph"]+shared["titles"]

demo = Demo()

def getTitle(ai):
    return titles[ai]

def getPara(rxi):
    return contextss[rxi[0]][rxi[1]]

def getAnswer(paragraph, question):
    pq_prepro = prepro(paragraph, question)
    if len(pq_prepro['x'])>1000:
        return "[Error] Sorry, the number of words in paragraph cannot be more than 1000." 
    if len(pq_prepro['q'])>100:
        return "[Error] Sorry, the number of words in question cannot be more than 100."
    return demo.run(pq_prepro)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/select', methods=['GET', 'POST'])
def select():
    #paragraph_id = request.args.get('paragraph_id', type=int)
    #rxi = [paragraph_id, 0]
    #paragraph = getPara(rxi)
    #return jsonify(result=paragraph)
    return jsonify(result={"titles" : titles, "contextss" : contextss, "context_questions" : context_questions})

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    paragraph = request.args.get('paragraph')
    question = request.args.get('question')
    answer = getAnswer(paragraph, question)
    return jsonify(result=answer)

@app.route('/submit1', methods=['POST'])
def submit1():
    req = request.json
    paragraph = req.get('paragraph')
    question = req.get('question')

    db = pymongo.MongoClient(mongo_url)['demo']
    collection = db['KnowledgeBase']

    document_cursor = collection.find({})
    documents = [d['context'] for d in document_cursor]

    matched = requests.post(
        paraphrase_url + "/msg-similarity",
        data= json.dumps({
            "msg": question,
            "msgs": documents,
            "headers":{"Content-Type": "application/json"}
        })
    )

    print(matched[0])

    answer = getAnswer(paragraph, question)
    return jsonify(result=answer)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, threaded=True, debug=True)
