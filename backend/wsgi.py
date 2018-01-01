import os
from backend import create_app

app = create_app(
    config_name=os.environ.get('APP_MODE')
)
