PYTHON_PREFIX="python/lib/python3.8/site-packages"

build:
	@pip install -t ./build/${PYTHON_PREFIX} -r requirements.txt

clean:
	@rm -rf ./build

deploy:
	@serverless deploy -c serverless.yml --verbose

remove:
	@serverless remove -c serverless.yml --verbose
