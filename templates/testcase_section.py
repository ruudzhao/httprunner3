

def {{ testcase_name }}({{ request_name }}):
    full_message = {{ request_name }}
    testcase_dict = {{ testcase }}
    compare_express = __compose_compare_express(testcase_dict, full_message)
    # ic(compare_express)
    assert eval(compare_express)

