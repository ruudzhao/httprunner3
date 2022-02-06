import pytest
import time
import requests
from icecream import ic
import jmespath
from string import Template


class HttpRequests:
    def __init__(self):
        self.base_url = "{{ base_url }}"
        self.s = requests.session()

    def act(self, _method, _url, _data, _headers):
        _url = f"{self.base_url}{_url}"
        start = time.time()
        if _method == "GET":
            r = self.s.request(method=_method, url=_url, params=_data, headers=_headers)
        else:
            r = self.s.request(method=_method, url=_url, data=_data, headers=_headers)
        # ic(r.url)
        end = time.time()
        time_span_seconds = round(end - start, 3)
        full_data = {"status_code": r.status_code, "time_span": time_span_seconds, "headers": r.headers,
                     "body": r.json(),
                     "content_length": r.headers.get('content-length', -1),
                     "request_headers": r.request.headers}
        return full_data


class ModuleLevelObject:
    def __init__(self):
        self.http = HttpRequests()
        self.data = {}


@pytest.fixture(scope="module")
def config_module():
    return ModuleLevelObject()


def __replace_parameters(parameters_dict, module_object_dict):
    for parameter_key in parameters_dict:
        if parameters_dict[parameter_key]:
            val_type = type(parameters_dict[parameter_key])
            value = str(parameters_dict[parameter_key])
            # ic(parameter_key, value)
            template = Template(value)
            value = template.safe_substitute(module_object_dict)
            parameters_dict[parameter_key] = value
            # ic(parameter_key, value)


def __compose_compare_express(testcase_dict, full_message):
    compare_operator, compare_values = testcase_dict.popitem()
    compare_operator = compare_operator.lower()
    fact_express = compare_values[0]
    fact_value = jmespath.search(fact_express, full_message)
    excepted_value = compare_values[1]
    """
        lt：less than 小于
        le：less than or equal to 小于等于
        eq：equal to 等于
        ne：not equal to 不等于
        ge：greater than or equal to 大于等于
        gt：greater than 大于
    """
    operator_dict = {"eq": "==", "lt": "<", "gt": ">", "le": "<=", "ge": ">=", "ne": "!="}
    if compare_operator in operator_dict:
        if isinstance(excepted_value, str):
            return f"'{fact_value}' {operator_dict[compare_operator]} '{excepted_value}'"
        else:
            return f"{fact_value} {operator_dict[compare_operator]} {excepted_value}"
    else:
        raise KeyError(f"{compare_operator} is not supported")

