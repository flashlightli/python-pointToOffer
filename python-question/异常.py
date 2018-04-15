def div(a, b):
    try:
      raise NameError("aaaaaaaaaaaaaa")
    except NameError as e:#e就是抛出的错误
        #return return 的话仍然会执行finally的语句
        raise# Exception("abbbbbbb") #如果except报错 就会抛出该错误 NameError
    finally:
        print('Always run into finally block.')

div(2, 0)