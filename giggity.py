import flask
import src.config.routes as routes
from src.temp_db import TempDB
from src.entity.Item import Item
import json

app = None
temp_store = None

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route(routes.HOME_ROUTE, methods=['GET'])
def get_home():
    return json.dumps(temp_store.find_all())


if __name__ == '__main__':
    temp_store = TempDB()

    item1 = Item(1, 'Name1', 'Title1')
    item2 = Item(2, 'Name2', 'Title2')
    item3 = Item(3, 'Name3', 'Title3')

    temp_store.save(item1)
    temp_store.save(item2)
    temp_store.save(item3)

    print('TU ESTILO TU FLOW MAMI MUY CRIMINAL')

    app.run(port=8080)
