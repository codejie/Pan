import ast

def make_arg_attr(arg: ast.arg) -> str | None:
  if arg.annotation:
    value = arg.annotation
    ret = ''
    while hasattr(value, 'attr'):
      ret = value.attr + ('.' + ret if ret else ret)
      value = value.value
    ret = value.id + ('.' + ret if ret else ret)
    return ret
  else:
    return None
  
def make_decorator_attr(decorator: ast.Call) -> str | None:
  if decorator.func:
    value = decorator.func
    ret = ''
    while hasattr(value, 'attr'):
      ret = value.attr + ('.' + ret if ret else ret)
      value = value.value
    ret = value.id + ('.' + ret if ret else ret)
    return ret
  else:
    return None

def make_decorator_keywords(decorator: ast.Call) -> list:
  ret: list[tuple[str, str]] = []
  if decorator.keywords and len(decorator.keywords) > 0:
    for keyword in decorator.keywords:
      ret.append((keyword.arg, keyword.value.id if type(keyword.value) == ast.Name else keyword.value.value))
  return ret

def make_decorator_call(call: ast.Call) -> str | None:
  func = call.func
  ret = func.value.id
  print(ret)
  # keywords
  if hasattr(func, 'keywords'):
    print(make_decorator_keywords(call))
  # args
  if hasattr(func, 'args'):
    make_decorator_args(func.args)
  # value/next
  if hasattr(call, 'value'):
    value = call.value
    make_decorator_call(value)

  # ret = ''
  # if hasattr(call, 'func'):
  #   func = call.func
  #   ret = func.attr
  #   print(ret)
  #   if hasattr(func, 'value'):
  #     make_decorator_call(func.value)
  # else:
  #   ret = call.id + ('.' + ret if ret else ret)
  #   print(ret)
    # print(make_decorator_keywords(func.kewords))

def make_decorator_args(args: list[ast.Call]) -> list:
  ret: list[str] = []
  for arg in args:
    make_decorator_call(arg)


# ##################################
def get_attribute_str(attr: ast.Attribute) -> str:
  ret = attr.attr
  # value
  if hasattr(attr, 'value'):
    if hasattr(attr.value, 'id'):
      ret = attr.value.id + ('.' + ret if ret else ret)
    elif type(attr.value) == ast.Call:
      get_decorator_arg_call(attr.value)
    elif type(attr.value) == ast.Attribute:
      ret = get_attribute_str(attr.value)
    else:
      print(f'======unknown attribute value = {attr.value}')
  return ret

def get_decorator_func_attr(decorator: ast.Call) -> str | None:
  if decorator.func:
    value = decorator.func
    ret = ''
    while hasattr(value, 'attr'):
      ret = value.attr + ('.' + ret if ret else ret)
      value = value.value
    ret = value.id + ('.' + ret if ret else ret)
    return ret
  else:
    return None  

def get_decorator_keywords(decorator: ast.Call) -> list:
  ret: list[tuple[str, str]] = []
  if decorator.keywords and len(decorator.keywords) > 0:
    for keyword in decorator.keywords:
      if type(keyword.value) == ast.Name:
        ret.append((keyword.arg, keyword.value.id))
      elif type(keyword.value) == ast.Constant:
        ret.append((keyword.arg, keyword.value.value))
      elif type(keyword.value) == ast.Attribute:
        ret.append((keyword.arg, get_attribute_str(keyword.value)))
      else:
        print(f'======unknown keyword value = {keyword.value}')
  return ret

def get_decorator_arg_call(arg: ast.Call) -> None:
  func = arg.func
  if type(func) == ast.Attribute:
    print(f'call arg attr = {get_attribute_str(func)}')
    # print(f'call arg attr = {func.attr}')
    # # func value
    # if hasattr(func, 'value'):
    #   if hasattr(func.value, 'id'):
    #     print(f'call arg value id = {func.value.id}')
    #   elif type(func.value) == ast.Call:
    #     get_decorator_arg_call(func.value)
    #   else:
    #     print(f'======unknown func value = {func.value}')
  # kweywords
  if hasattr(arg, 'keywords'):
    ret = get_decorator_keywords(arg)
    print(f'call arg keywords = {ret}')
  # args
  if hasattr(arg, 'args'):
    for arg in arg.args:
      if type(arg) == ast.Call:
        get_decorator_arg_call(arg)
      elif type(arg) == ast.Constant:
        print(f'arg value = {arg.value}')
      elif type(arg) == ast.Attribute:
        print(f'arg attr = {get_attribute_str(func)}')
      else:
        print(f'======unknown arg = {arg}')

def get_decorator_args(decorator: ast.Call) -> list:
  ret = []
  for arg in decorator.args:
    ret.append(get_decorator_arg_call(arg))
  return ret

def parse_decorator(decorator: ast.Call) -> None:
  # attr / func
  attr = get_decorator_func_attr(decorator)
  print(f'decorator attr = {attr}') if attr else print('decorator attr is None')
  # keywords
  keywards = get_decorator_keywords(decorator)
  print(f'decorator keywords = {keywards}') if keywards else print('decorator keywords is None')
  # args
  args = get_decorator_args(decorator)
  print(args)



def parse(buffer: bytes) -> None:
  script = ast.parse(buffer)
  print(ast.dump(script))
  funcs = [node for node in script.body if isinstance(node, ast.FunctionDef)]
  for func in funcs:
    # name
    print(func.name)
    # argument
    for arg in func.args.args:
      print(f'{arg.arg}: {make_arg_attr(arg)}')
    # decorator
    if hasattr(func, 'decorator_list'):
      for decorator in func.decorator_list:
        parse_decorator(decorator)

        # # decorator name
        # print(make_decorator_attr(decorator))
        # # decorator args(keywords)
        # if hasattr(decorator, 'keywords'):
        #   print(make_decorator_keywords(decorator))
        # # decorator args
        # if hasattr(decorator, 'args'):
        #   make_decorator_args(decorator.args)
      

  #   if func.decorator_list and len(func.decorator_list) > 0:
  #     for d in func.decorator_list:
  #       print(d.func.attr)

def load_file(file: str) -> None:
  with open(file, 'rt') as input:
    buffer: bytes = input.read().encode('utf-8')
    parse(buffer=buffer)

if __name__ == '__main__':
  load_file('./example2.py')
