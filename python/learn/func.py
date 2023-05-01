from parliament import Context
from flask import Request
import numpy as np
from werkzeug.exceptions import MethodNotAllowed, BadRequest, InternalServerError, HTTPException





def main(context: Context):
    """
    Hello world
    """
    print("Received request")
    print(f"Req={context}")

    return {'a':'b'}
    #return context.cloud_event.data
