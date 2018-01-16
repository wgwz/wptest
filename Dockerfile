FROM grahamdumpleton/mod-wsgi-docker:python-3.5-onbuild
USER $MOD_WSGI_USER:$MOD_WSGI_GROUP
ENV APP_MODE development
CMD [ "/app/backend/wsgi.py" ]
