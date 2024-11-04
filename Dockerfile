ARG ALPINE_VERSION=latest
ARG WORKDIR_APP=/app

FROM yidoughi/pythopine:${ALPINE_VERSION} AS builder

ARG WORKDIR_APP

ARG VIRTUAL_ENV=${WORKDIR_APP}/venv

ARG APP_ENV=dev

ENV PATH="$VIRTUAL_ENV/bin:$PATH"

WORKDIR ${VIRTUAL_ENV}

COPY --chown=1001:1001 requirement/requirements.txt ${VIRTUAL_ENV}/requirement/requirements.txt 


RUN mkdir ${VIRTUAL_ENV}/src && pip --no-cache-dir install -r requirement/requirements.txt

COPY --chown=1001:1001 env ${VIRTUAL_ENV}/env

COPY --chown=1001:1001 src ${VIRTUAL_ENV}/src

COPY --chown=1001 --chmod=755 scripts/start.sh ${VIRTUAL_ENV}/bin/start.sh

RUN rm requirement/requirements.txt


FROM yidoughi/fastpine:latest

ARG WORKDIR_APP=/app
ARG VIRTUAL_ENV=${WORKDIR_APP}/venv


ENV HOME=${VIRTUAL_ENV}

ENV SQLAPIFY_CLIENT_ENV="dev" \
    SQLAPIFY_ENDPOINT="http://sqlapify:8000 "\
    SQLAPIFY_CLIENT_APP_SECRET="app_secret" \
    SQLAPIFY_CLIENT_HOST="0.0.0.0" \
    SQLAPIFY_CLIENT_PORT="8001" \
    APP_DB_NAME="app_db" \
    APP_DB_USER="app_username" \
    APP_DB_PASSWORD="app_password"

WORKDIR ${HOME}

COPY --from=builder --chown=1001 ${VIRTUAL_ENV} ${VIRTUAL_ENV} 

RUN rm -rf /usr/lib/python**/__pycache__** && \
    find ${VIRTUAL_ENV} -type d -name "tests" -exec rm -rf {} + && \
    find /usr/lib/ -type d -name "tests" -exec rm -rf {} + && \
    find /usr/lib/ -type d -name "docs" -exec rm -rf {} + && \
    find ${VIRTUAL_ENV} -type d -name "__pycache__" -exec rm -rf {} + && \
    rm -rf /var/cache/apk/* /tmp/* /**/.cache/pip

USER 1001
CMD ["start.sh"]
# CMD ["tail", "-f", "/dev/null"]