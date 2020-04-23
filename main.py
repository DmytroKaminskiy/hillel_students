from flask import Flask, request, Response, redirect
from utils import generate_password
from parsers import parse_length

app = Flask(__name__)


@app.route('/random/')
def hello_world():  # вью функция, эндпоинт

    # return redirect('https://pythonworld.ru/')
    length = parse_length(request.args.get('length', '10'))

    if type(length) is str:
        return Response(length, status=400)

    response = Response(generate_password(length) + '\n')

    return response


if __name__ == '__main__':
    app.run(port=5050)

# BR (Client) -> request (http://127.0.0.1:5050/hello-world/) -> Flask (PATH) ->
# /w/ (hello) | /hello-world/ (hello_world) -> response -> Client

#  IPV4 0-255.0-255.0-255.0-255
# 8.10.4.2
# 127.12.34.0
# 127.0.1.277 - WRONG

# 127.0.0.1
# 443
# 104.17.33.82:443
#  IPV6

# IP - PORT -> socket

# 127.0.0.1:5000
# 0 - 65,500
# 0 - 1000
# 1000 - 5000
# 5000

# PROTOCOL / IP   / PORT / PATH / query_params
# http://127.0.0.1:5050/hello-world/?hello=world&a=10

# http:// - protocol
# 127.0.0.1 - IPV4
# 5050 - PORT
# /hello-world/ - PATH

'''
1xx - info
2xx - 200 OK
3xx - redirects
4xx - 404 Not Found (Client Error), 400 - Bad request
5xx - 500 (Server Error)

https://ru.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D0%BA%D0%BE%D0%B4%D0%BE%D0%B2_%D1%81%D0%BE%D1%81%D1%82%D0%BE%D1%8F%D0%BD%D0%B8%D1%8F_HTTP
'''






