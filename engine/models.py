"""
Daksha
Copyright (C) 2021 myKaarma.
opensource@mykaarma.com
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.
You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
import copy

from django.db import models


# Create your models here.
class TestExecutor:
    def __init__(self, index, test_id, variable_dict, test_yml, web_driver):
        self.index = index
        self.test_id = test_id
        self.variable_dictionary = copy.deepcopy(variable_dict)
        self.test_yml = test_yml
        self.web_driver = web_driver


class TestResult:
    def __init__(self, name, test_status, step, failure_reason):
        self.test_name = name
        self.test_status = test_status
        self.failed_step = step
        self.failure_cause = failure_reason
