# 设置excel列常量

class global_var:
    test_name = '0'
    url = '1'
    method = '2'
    header = '3'
    dep_id = '4'
    dep_data = '5'
    dep_field = '6'
    request_data = '7'
    expect_data = '8'
    run = '9'

def get_test_name():
    return global_var.test_name

def get_url():
    return global_var.url

def get_method():
    return global_var.method

def get_header():
    return global_var.header

def get_dep_id():
    return global_var.dep_id

def get_dep_data():
    return global_var.dep_data

def get_dep_field():
    return global_var.dep_field

def get_request_data():
    return global_var.request_data

def get_expect_data():
    return global_var.expect_data

def get_run():
    return global_var.run

def get_header_value():
    header = {
        'header':'1234',
        'cookie':'I like you'
    }
    return header