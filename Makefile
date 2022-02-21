all:

tag=mytag

build: 
	docker build --build-arg DOCKER_REGISTRY=${DOCKER_REGISTRY} -t $(tag) .


check: build
	docker run -it --rm -v $(PWD)/out-results:/ACT4E/out-results $(tag) \
		act4e-test --collections act4e_checks --module act4e_solutions


check-%: build
	docker run -it --rm -v $(PWD)/out-results:/ACT4E/out-results $(tag) \
		act4e-test --collections act4e_checks --module act4e_solutions --group $*

