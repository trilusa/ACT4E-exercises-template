all:

tag=mytag

pull:
	docker pull andreacensi/act4e:spring2021

build: pull
	docker build  -t $(tag) .


check: build
	docker run -it --rm -v $(PWD)/out-results:/ACT4E/out-results $(tag) act4e-tests --module act4e_solutions


check-%: build
	docker run -it --rm -v $(PWD)/out-results:/ACT4E/out-results $(tag) act4e-tests --module act4e_solutions --group $*

