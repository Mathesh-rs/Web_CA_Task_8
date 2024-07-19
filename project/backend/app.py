from flask import Flask, request, jsonify, send_file
import pandas as pd
from allocate import allocate_rooms, save_allocation_to_csv

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to the Hospitality Digitalization API"

@app.route('/upload', methods=['POST'])
def upload_files():
    group_file = request.files['group_file']
    hostel_file = request.files['hostel_file']
    
    groups = pd.read_csv(group_file)
    hostels = pd.read_csv(hostel_file)
    
    allocation = allocate_rooms(groups, hostels)
    save_allocation_to_csv(allocation, 'allocation.csv')
    
    return send_file('allocation.csv', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
