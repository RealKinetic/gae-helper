#
# Copyright 2013 Real Kinetic
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

SHELL := /bin/bash
PYTHON := python
PIP := pip

BUILD_DIR := .build
TOOLS_DIR := .tools

clean:
	find . -name "*.py[co]" -delete

distclean: clean
	rm -rf $(BUILD_DIR)

run: deps
	dev_appserver.py . --use_sqlite

deps: py_deploy_deps py_dev_deps

py_deploy_deps: $(BUILD_DIR)/pip-deploy.log

py_dev_deps: $(BUILD_DIR)/pip-dev.log

$(BUILD_DIR)/pip-deploy.log: requirements.txt
	@mkdir -p .build
	$(PIP) install -Ur requirements.txt | tee $(BUILD_DIR)/pip-deploy.log
	$(PYTHON) $(TOOLS_DIR)/link_libs.py

$(BUILD_DIR)/pip-dev.log: requirements_dev.txt
	@mkdir -p .build
	$(PIP) install -Ur requirements_dev.txt | tee $(BUILD_DIR)/pip-dev.log

test_py:
	nosetests

test: test_py

