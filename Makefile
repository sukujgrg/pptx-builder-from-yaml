.PHONY: clean release 

clean:
	rm -rf pptx_builder_from_yaml.egg-info dist build generated-pptx
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

release:
	python3 setup.py sdist bdist_wheel 

