# Copyright (c) 2017 UFCG-LSD.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from application_manager.plugins import base


class TestProvider(base.PluginInterface):

    def get_title(self):
        return 'OpenStack Sahara'

    def get_description(self):
        return 'Plugin that allows utilization of Sahara to run jobs'

    def to_dict(self):
        return {
            'name': self.name,
            'title': self.get_title(),
            'description': self.get_description(),
        }
    def execute(self, data, user, password, project_id, auth_ip, domain,
                public_key, net_id):
        return True