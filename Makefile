all:

tag=act4e-image

build: 
	docker build -f .devcontainer/Dockerfile --build-arg DOCKER_REGISTRY=${DOCKER_REGISTRY} -t $(tag) .

docker-check: build
	docker run -it --rm -v $(PWD)/out-results:/ACT4E/out-results $(tag) \
		act4e-test --collections act4e_checks --module act4e_solutions


docker-check-%: build
	docker run -it --rm -v $(PWD)/out-results:/ACT4E/out-results $(tag) \
		act4e-test --collections act4e_checks --module act4e_solutions --group $*

# check:
# 	act4e-test --collections act4e_checks --module act4e_solutions

# check-%:
# 	act4e-test --collections act4e_checks --module act4e_solutions --group $*