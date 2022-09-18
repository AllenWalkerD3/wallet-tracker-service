env_dir = $(CURDUR)/$(ENV_NAME)
bin_dir = $(env_dir)/bin
activate_env = . $(bin_dir)/activate_env
dotenv_file = .env

ENV_NAME = env
PYTHON_COMMAND ?= python3
STAGE ?= local

make_env = $(PYTHON_COMMAND) -m venv env


define create-env 
	@echo Creating $@....
	$(make_env)
	$(bin_dir)/pip install --upgrade pip
	$(bin_dir)/pip install pip-tools
endef

.PHONY: env
env:
	$(create)

.PHONY: wsgi_serve
wsgi_serve:
	sls wsgi serve -p 4499