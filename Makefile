clean:
	find ./ -name .DS_Store | xargs rm

virtualenv:
	test -d venv || virtualenv venv
	. venv/bin/activate; STATIC_DEPS=true pip install lxml requests cssselect python-slugify