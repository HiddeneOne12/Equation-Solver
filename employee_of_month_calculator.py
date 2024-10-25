from flask import Flask, request, jsonify
import pandas as pd
import numpy as np
import os
    
app = Flask(__name__)


def calculate_employee_of_the_month(file_path):
    # Read the Excel file
    df = pd.read_excel(file_path)

    # Check if the expected columns exist
    required_columns = ['Name', 'Performance Score', 'Behaviour', 'Timing', 'Post']
    if not all(column in df.columns for column in required_columns):
        return None

    # Sort the DataFrame by 'Performance Score' in descending order
    sorted_df = df.sort_values(by='Performance Score', ascending=False)

    # Iterate through the sorted DataFrame to find the first employee meeting all conditions
    for index, row in sorted_df.iterrows():
        if row['Behaviour'] == 'good' and row['Timing'] == 'punctual':
            return {
                'employee_name': str(row['Name']),
                'employee_behaviour': str(row['Behaviour']),
                'employee_timing': str(row['Timing']),
                'performance_score': int(row['Performance Score']),
                'employee_post': str(row['Post'])
            }

    # If no employee meets the criteria, return None
    return None

@app.route('/employee_of_the_month', methods=['POST'])
def employee_of_the_month():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    try:
        file_path = os.path.join('./', file.filename)
        file.save(file_path)

        # Calculate employee of the month
        result = calculate_employee_of_the_month(file_path)

        if result is None:
            return jsonify({"error": "Invalid file format"}), 400

        return jsonify(result)
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
