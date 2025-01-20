# script to import nb3 files.

import sqlalchemy
import json

ROOT_PATH: str = 'D:\\Jie\\database\\dst\\'

engine = sqlalchemy.create_engine(
    "mysql://root:123456@localhost:3306/test",
    pool_size=10,
    max_overflow=20
)

def load_meta_list(file: str) -> list[dict]:
  with open(file) as input:
    content = json.load(input)
    ret = content['Objects']
    return ret
  
def recovery_table_data(meta) -> None:
  global engine

  meta_file = f'{ROOT_PATH}{meta['UUID']}.meta.json'
  with open(meta_file, 'r', encoding='utf-8') as input:
    meta_json = json.load(input)
    table_name = meta['Name']
    ddl = meta_json['DDL']
    # print(ddl)
    with engine.connect() as conn:
      results = conn.execute(sqlalchemy.text(ddl))
      # print(results.rowcount)
      conn.commit()

    data = meta_json['Data']
    for d in data:
      # print(d)
      data_file = f'{ROOT_PATH}{d['Filename'][:-3]}'
      with engine.connect() as conn:
        with open(data_file, 'r', encoding='utf-8') as file:
          lines = file.readlines()
          for line in lines:
            sql = f'INSERT INTO {table_name} VALUES {line}'
            # print(sql)
            conn.execute(sqlalchemy.text(sql))
        conn.commit()
      if meta['UUID'] == '65158d15-9c3e-42a3-92d9-4e3dc8e033df' \
        or meta['UUID'] == '49c020df-cc09-454d-a617-8aa490423cda' \
        or meta['UUID'] == '9e117498-5cd9-45f7-962d-df5e93c5268a':
        print('log or record table, only import one data file, skip others..')
        break

def recovery_view(meta) -> None:
  global engin

  meta_file = f'{ROOT_PATH}{meta['UUID']}.meta.json'
  meta_json = json.load(meta_file)
  ddl = meta_json['DDL']
  # print(ddl)
  with engine.connect() as conn:
    results = conn.execute(sqlalchemy.text(ddl))
    print(results.rowcount)
    conn.commit()


def load_meta_file(meta) -> None:
  print(meta['UUID'])
  
  if meta['Type'] == 'Table':
    recovery_table_data(meta)
  elif meta['Type'] == 'View':
    recovery_view(meta)
  else:
    print('Unknown type - ' + meta['Type'])

def main():
  with engine.connect() as conn:
    conn.execute(sqlalchemy.text('SET FOREIGN_KEY_CHECKS=0'))

  meta_file = 'D:\\Jie\\database\\dst\\meta.json'
  metas = load_meta_list(meta_file)

  for meta in metas:
    load_meta_file(meta)

  with engine.connect() as conn:
    conn.execute(sqlalchemy.text('SET FOREIGN_KEY_CHECKS=1'))

main()
