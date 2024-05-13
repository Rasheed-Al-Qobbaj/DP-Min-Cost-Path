from flask import Flask, request, render_template
from Util import read_data, generate_dp_table, find_optimal_path, find_alternate_paths
import os

app = Flask(__name__)



@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        file_path = os.path.join('uploads', file.filename)
        file.save(file_path)
        num_cities, start_city, end_city, city_data = read_data(file_path)
        os.remove(file_path)  # delete the file after reading
        dp_table = generate_dp_table(city_data)
        min_cost, path = find_optimal_path(dp_table, start_city, end_city)
        alternate_paths = find_alternate_paths(dp_table, start_city, end_city)
        return render_template('result.html', num_cities=num_cities, start_city=start_city, end_city=end_city, dp_table=dp_table, min_cost=min_cost, path=path, alternate_paths=alternate_paths, float=float)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)