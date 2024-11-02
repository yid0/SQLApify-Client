SQLAPIFY_CLIENT_VERSION ?=1.0.0
IMAGE_NAME ?=sqlapify-client
ALPINE_VERSION ?=3.20
OPTIONS ?=
TAG ?=${SQLAPIFY_CLIENT_VERSION}-alpine${ALPINE_VERSION}

.PHONY:	build
build:
	docker buildx build -t yidoughi/${IMAGE_NAME}:${TAG} . --progress=plain ${OPTIONS}
	docker tag yidoughi/${IMAGE_NAME}:${TAG} yidoughi/${IMAGE_NAME}:latest

push:
	docker push yidoughi/${IMAGE_NAME}:${TAG}
	docker push yidoughi/${IMAGE_NAME}:latest

.PHONY:	run
run:
	docker rm -f ${IMAGE_NAME} 
	docker run  --rm --name ${IMAGE_NAME} -d --network host yidoughi/${IMAGE_NAME}:latest

.PHONY:	exec
exec:
	docker exec -it ${IMAGE_NAME} sh

.PHONY:	run-all
run-all:
	make build
	make run
	make exec

.PHONY:	local
local:
	uvicorn src.main:app --host 0.0.0.0 --port 8001 --reload --env-file env/.env.dev