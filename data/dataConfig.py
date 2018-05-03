# 设置excel列常量

class global_var:
    test_name = '1'
    url = '2'
    method = '3'
    header = '4'
    dep_case_id = '5'
    dep_response_data = '6'
    dep_field = '7'
    request_data = '8'
    expect_result = '9'
    actual_result = '10'
    run = '11'

def get_test_name():
    return global_var.test_name

def get_url():
    return global_var.url

def get_method():
    return global_var.method

def get_header():
    return global_var.header

def get_dep_case_id():
    return global_var.dep_case_id

def get_dep_response_data():
    return global_var.dep_response_data

def get_dep_field():
    return global_var.dep_field

def get_request_data():
    return global_var.request_data

def get_expect_data():
    return global_var.expect_result

def get_actual_result():
    return global_var.actual_result

def get_run():
    return global_var.run

def get_header_value():
    header = {
        'header':'1234',
        'cookie':'I like you'
    }
    return header