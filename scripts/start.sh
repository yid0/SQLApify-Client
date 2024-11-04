#!/bin/sh

set -e
echo "*************** Main Process - SQLApify client starting ..... ************ "

if [ "$SQLAPIFY_CLIENT_ENV" = "dev" ]; then
    echo "*************** Loading $SQLAPIFY_CLIENT_ENV env file ************ "
    uvicorn src.main:app --host $SQLAPIFY_CLIENT_HOST --port $SQLAPIFY_CLIENT_PORT --env-file  $VIRTUAL_ENV/env/.env.$SQLAPIFY_CLIENT_ENV
else
    uvicorn src.main:app --host $SQLAPIFY_CLIENT_HOST --port $SQLAPIFY_CLIENT_PORT
fi