import ast

def __get_attribute_str(attr: ast.Attribute) -> str:
  stack: list = []
  next = attr
  while not isinstance(next, ast.Name):
    stack.append(next)
    next = next.value
  ret = next.id
  for item in reversed(stack):
    ret = ret + '.' + item.attr
  return ret


def get_decorator_name(decorator: ast.Call) -> str:
  stack: list = []
  return __get_attribute_str(decorator.func)

def get_decorator_keywords(decorator: ast.Call) -> list:
  ret: list[tuple[str, str]] = []
  for keyword in decorator.keywords:
    if type(keyword.value) == ast.Name:
      ret.append((keyword.arg, keyword.value.id))
    elif type(keyword.value) == ast.Constant:
      ret.append((keyword.arg, str(keyword.value.value)))
    elif type(keyword.value) == ast.Attribute:
      ret.append((keyword.arg, __get_attribute_str(keyword.value)))
    else:
      ret.append((keyword.arg, f'{ast.unparse(keyword.value)}(u)'))
  return ret

def get_decorator_arg_call(arg: ast.Call) -> str:
  return __get_attribute_str(arg.func)

def get_decorator_args(decorator: ast.Call) -> list:
  ret = []
  for arg in decorator.args:
    # ret.append(ast.unparse(arg))
    if type(arg) == ast.Call:
      ret.append(get_decorator_arg_call(arg))
    # ret.append({
    #   'name': get_decorator_name(arg),
    #   'args': get_decorator_args(arg)
    # })
    # ret.append(get_decorator_name(arg))
  return ret

def parse_decorator(decorator: ast.Call) -> None:
  # func = decorator.func
  name = get_decorator_name(decorator)
  print(f'decorator name = {name}')
  keywords = get_decorator_keywords(decorator)
  print(f'decorator keywords = {keywords}')
  args = get_decorator_args(decorator)
  print(f'decorator args = {args}')
  # if isinstance(func, ast.Attribute):
  #   get_decorator_func_name(func)
  # elif isinstance(func, ast.Name):
  #   pass

def parse(buffer: bytes) -> None:
  script = ast.parse(buffer)
  print(ast.dump(script, indent=2))
  for func in script.body:
    print(func)
    for decorator in func.decorator_list:
      # print(decorator)
      parse_decorator(decorator)

def load_file(file: str) -> None:
  with open(file, 'rt') as input:
    buffer: bytes = input.read().encode('utf-8')
    parse(buffer=buffer)

if __name__ == '__main__':
  load_file('./example2.py')
