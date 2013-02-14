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

import os
import sys


def setup():
    """Call this method to configure your WSGI application.

    Add any of your customs setup calls to this as well.
    """
    setup_lib_path()


def setup_lib_path():
    """Add lib to path."""
    libs_dir = os.path.join(os.path.dirname(__file__), 'lib')
    if libs_dir not in sys.path:
        sys.path.insert(0, libs_dir)

