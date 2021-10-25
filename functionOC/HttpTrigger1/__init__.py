import logging
from io import BytesIO
import azure.functions as func
import pandas as pd


def main(req: func.HttpRequest, blbarticle: func.InputStream) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    
    if not name:
        try:
            req_body = req.get_json()
            click = pd.read_csv(BytesIO(blbarticle.read()))
            print('vale de click'+click.info())
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        click = pd.read_csv(BytesIO(blbarticle.read()))
        print('vale de click'+click.info())
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
