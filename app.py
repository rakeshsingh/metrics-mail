from chalice import Chalice
from chalice import BadRequestError
from chalice import UnauthorizedError
from chalice import NotFoundError

app = Chalice(app_name='metrics-mail')
app.debug = True


OBJECTS = {
}

@app.route('/objects/{key}', methods=['GET', 'PUT'])
def myobject(key):
    request = app.current_request
    if request.method == 'PUT':
        OBJECTS[key] = request.json_body
    elif request.method == 'GET':
        try:
            return {key: OBJECTS[key]}
        except KeyError:
            raise NotFoundError(key)


