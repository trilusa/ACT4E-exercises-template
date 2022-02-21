all:

DOCKER_REGISTRY ?= reg-z7-prod.zuper.ai

tag=mytag

pull:
	docker pull ${DOCKER_REGISTRY}/act4e/act4e-tests:alphubel

build: pull
	docker build --build-arg DOCKER_REGISTRY=${DOCKER_REGISTRY} -t $(tag) .


check: build
	docker run -it --rm -v $(PWD)/out-results:/ACT4E/out-results $(tag) act4e-tests --module act4e_solutions


check-%: build
	docker run -it --rm -v $(PWD)/out-results:/ACT4E/out-results $(tag) act4e-tests --module act4e_solutions --group $*

