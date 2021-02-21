all:

tag=mytag

pull:
	docker pull andreacensi/act4e:spring2021

build:
	docker build  -t $(tag) .


check: build
	docker run --rm $(tag) act4e-tests --module act4e_solutions


check-%: build
	docker run --rm $(tag) act4e-tests --module act4e_solutions --group $*

#
#check:
#	docker run -it --rm -v $(PWD):$(PWD):ro -w $(PWD) andreacensi/act4e:spring2021 act4e-tests --module act4e_solutions
