import json
from flask import Response


def JsonResp(data, status: int):
    return Response(json.dumps(data, default=str), mimetype="application/json", status=status)
