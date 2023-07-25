import random
from flask import Flask, request, jsonify

app = Flask(__name__)

# Define a route for the hello endpoint
@app.route('/hello', methods=['GET'])
def hello():
  my_input = request.args.get('name')
  lucky_numbers = sorted(random.sample(range(1, 71), 7))
  lucky_numbers_str = ", ".join(str(n) for n in lucky_numbers)
  my_output = f"Hello {my_input}, your lucky numbers are: {lucky_numbers_str}"

  return jsonify({'output': my_output})

# Run the app in debug mode
if __name__ == '__main__':
  app.run(port=12345)
