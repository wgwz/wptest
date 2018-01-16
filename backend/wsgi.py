import os
from backend import create_app

application = create_app(
    config_name=os.environ.get('APP_MODE')
)
