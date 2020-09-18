import nltk
nltk.download('punkt')
from flask import Flask, request, jsonify
from nltk import word_tokenize, pos_tag, ne_chunk
from nltk.corpus import wordnet

app = Flask(__name__)

@app.route('/translate',methods =["GET"])
def analyze():
    d = {}
    text = str(request.args.get('text'))
    sentence = text
    tokens = word_tokenize(sentence)
    tags = pos_tag(tokens)
    
    res = ""
    for tag in tags:
        if tag[1] not in ['JJ','JJR','JJS']:
            res = res + " " + tag[0]
        else:
            syns = wordnet.synsets(tag[0])
            x = syns[0].lemmas()[0].name()
            for syn in syns:
                for l in syn.lemmas():
                    if l.antonyms():
                        x = l.antonyms()[0].name()
                        break
            res = res + " " + x


    d['text'] = text
    d['result'] = str(res)

    return jsonify(d)


if __name__ == '__main__':
    app.run()