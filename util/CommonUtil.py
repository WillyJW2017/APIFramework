class CommonUtil:

    '''
    判断一个字符串是否包含在另一个字符串中
    str_one : 要查找的字符串
    str_two : 被查找的字符串
    '''
    def is_contain(self, str_one, str_two):
        flag = None
        if str_one in str_two:
            flag = True
        else:
            flag = False
        return flag