from flask import Flask
from flask_restplus import Resource, Api
from collections import Counter

app = Flask(__name__)
api = Api(app, title=' String Formatting', version='1.0',
            description='A simple flask API for splitting and counting frequency of string')


@api.route('/split_string/<string:String>/<int:Number>')
class SplitString(Resource):
    def get(self, String, Number):
        String = String[::-1]
        eml = []
        for i in range(0, len(String), Number):
            eml.append((String[i:i+Number])[::-1])
        output = ' '.join(reversed(eml))
        return {'Output Response': output}


@api.route('/string_freq/<string:String>')
class StringFreq(Resource):
    def get(self, String):
        rmspc = String.replace(' ', '')
        spt = rmspc.split(',')
        output = Counter(spt)
        return {'Output Response': output}


if __name__ == '__main__':
    app.run(debug=True)
