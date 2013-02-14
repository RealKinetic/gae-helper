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

# TODO:  Be sure to include boot and call setup in all your WSGI apps.
import boot
boot.setup()

import webapp2


class HelloWorldHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write('Hello world!')


# Setup your jinja path.
config = {
    'webapp2_extras.jinja2': {
        'template_path': 'templates'
    }
}

app = webapp2.WSGIApplication(
    [('/', HelloWorldHandler)],
    config=config
)

