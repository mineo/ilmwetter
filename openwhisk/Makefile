.PHONY: all clean

ACTION ?= ilmwetter

all: $(ACTION).zip

virtualenv: $(wildcard ../ilmwetter/**/*.py)
	docker run --rm -v "$(CURDIR)/..:/tmp" openwhisk/python2action sh -c "cd tmp; virtualenv openwhisk/$@; source  openwhisk/$@/bin/activate; python setup.py install;"

$(ACTION).zip: virtualenv __main__.py
	zip -r $@ __main__.py $<

create-action: $(ACTION).zip
	wsk action delete $(ACTION)
	wsk action create --kind python:2 $(ACTION) $<

clean:
	rm $(ACTION).zip
	rm -rf virtualenv
