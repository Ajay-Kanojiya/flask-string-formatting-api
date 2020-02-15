from flask import Flask
from flask_restplus import Resource, Api
from collections import Counter

app = Flask(__name__)
api = Api(app, title=' String Formatting', version='1.0',
            description='A simple flask API for splitting and counting frequency of string')


@api.route('/split_string/<string:String>/<int:Number>')
class SplitString(Resource):
    def get(self, String, Number):
        return {'Output Response': output}


@api.route('/string_freq/<string:String>')
class StringFreq(Resource):
    def get(self, String):
        spt = String.split(',')
        output = Counter(spt)
        print(output)
        return {'Output Response': output}


if __name__ == '__main__':
    app.run(debug=True)
