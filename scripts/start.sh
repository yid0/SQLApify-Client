#!/bin/sh

set -e
echo "*************** Main Process - SQLApify client starting ..... ************ "
exec uvicorn src.main:app --host SQLAPIFY_CLIENT_HOST --port $SQLAPIFY_CLIENT_PORT --env-file env/.env.$SQLAPIFY_CLIENT_ENV