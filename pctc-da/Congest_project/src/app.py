from flask import Flask, render_template, jsonify, request

from DA import randomForest_predict
import json
import requests
from flask_cors import CORS
import pandas as pd
app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

    
@app.route('/api/r_predict', methods=['GET', 'POST'])
def r_prediction():
    if request.method == 'POST':
        # new_data = request.get_json()
        # print('json 전달 받은 데이터', new_data)
        # new_data_df = pd.DataFrame(new_data)
        
        grouped_df = randomForest_predict.operate()
        grouped_df_json = grouped_df.to_json(date_format='iso', orient='records')
        grouped_df_parsed = json.loads(grouped_df_json)
        grouped_df_clean = json.dumps(grouped_df_parsed, ensure_ascii=False)
        return jsonify({'grouped_df_json': grouped_df_clean})
    else:
        return 'error'

if __name__ == '__main__':
    # host, port를 설정하고 여기로 요청을 하게 하면 됨
    app.run(host='10.125.121.220', port=5001, debug=True)