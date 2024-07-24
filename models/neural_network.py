import os

from flask import Flask, jsonify, request
from flasgger import Swagger, LazyString, LazyJSONEncoder
from flasgger import swag_from

app = Flask(__name__)



class A:
    @staticmethod
    def test():
        return "HEllo WOrld"
    
    def view_all_text(self):
        with app.app_context():
            #conn = sqlite3.connect('data/binar_dsc_gold_challenge.db', check_same_thread=False)

            #cursor = conn.execute("SELECT teks_sebelum, teks_setelah FROM pengolahan_teks")
            #all_text = []

            #for row in cursor:
            #    all_text.append(row)

            #conn.close()

            json_response = {
                'status_code': 200,
                'description': "Menampilkan semua teks",
                'data': 'HALLO APA KABAR',
            }

            response_data = jsonify(json_response)
        return json_response
