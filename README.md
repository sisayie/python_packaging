Python packaging

# Directory Structure
├── LICENSE
├── README.md
├── client
│   └── test.html
├── requirements.txt
├── server
│   ├── __init__.py
│   ├── application.py
├── wsgi.ini
└── wsgi.py

# Installing requirements
pip install -r requirements.txt

# Run the test server
flask run

# Test from browser
http://127.0.0.1:5000/user/Anie

# Test from cli clients. If you get error when running it on Windows prompt, use curl -g to turn off globbing like curl -g --header ...
curl --header "Content-Type: application/json" --request POST --data '{"name":"Anie","age":56, "occupation":"Programmer"}' http://127.0.0.1:5000/user

curl --request POST \
  --url http://127.0.0.1:5000/user/ \
  --header 'age: 22' \
  --header 'name: Anie' \
  --header 'occupation: Engineer'
  
curl --header "Content-Type: application/json" --request DELETE http://127.0.0.1:5000/user/Anie
