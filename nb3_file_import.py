import sqlalchemy
import json

ROOT_PATH: str = 'D:\\Jie\\database\\dst\\'


done_list: list[str] = [
# 'dbee7274-2fd5-4c58-946f-87ad884b1d43',
# '095bd7c0-7079-458a-9204-816f45a948a9',
# '586b120d-02e1-4c71-8de3-4659190a7b08',
# 'a8c5b3c3-dce8-43d8-a1da-15050f36e58b',
# 'ca8b622e-39c7-45f3-a1f4-ad71613a4119',
# 'ae42fe65-68b3-48f6-86f7-2cf92c6996d7',
# '28184385-ff3e-4aeb-bfca-00799f6c042c',
# 'f0170b4f-7b40-4aab-a178-7ad45304d059',
# 'c0741025-240c-4e02-9c3a-f42ecfb3df8b',
# '9f2b2746-caed-43b1-828d-21fee78bce61',
# '92b58124-2ac5-478c-8df5-b97712f9c962',
# 'e6d94ea0-91e1-482d-bdfe-27d7cc1cd315',
# 'e655d56c-f787-4dd8-aca9-e8acc9cf05fe',
# '5cb04504-ece8-4731-948b-2fba819e12ef',
# '20433662-742e-4d8c-829c-63b9150decb3',
# '3b3e3797-359d-4178-8011-8be575b61fef',
# '7ccb37fd-abc6-443a-b49c-fb808e3ee2e2',
# '70f79499-02e9-4483-aeae-3b3c2f6fbaa5',
# '21d0e99e-f5e8-462b-bc61-49938631736e',
# '02662471-b650-4319-950e-435ddc045fb9',
# '415b43c5-ab74-4785-acbb-f0f1a5aa0a7f',
# 'a72e2f38-932a-4340-9be9-c518aea8b14a',
# 'cfb723d6-717b-4a62-9df1-b9509d8c4951',
# '1c1d73a6-b0b6-4595-ad2e-431a65ffab62',
# '736edaba-8596-4848-a46f-186030e1ed69',
# '3f4eff27-2b68-4570-b72c-ce2c0a5c1d65',
# 'd0731b4e-d363-46f2-8393-0873a5b47741',
# '515e6283-1e96-4ad5-b684-198fd1028899',
# 'cf24898b-f30c-49b7-8f3c-af5a0b0f405b',
# '0d5cb683-0c46-4518-987a-5ecfcba5c0c8',
# '3a962864-c4f3-4659-82ad-ab5d2c035206',
# 'fbbdf212-b4f7-430f-bc0f-d0e20d222655',
# '5204d276-1d0f-4717-8bc8-0177a868b9d8',
# '672d464c-d935-4378-84c7-6579a53a23cd',
# 'bbbb2365-1429-46ee-81c9-9a720e6d6c06',
# '7707218a-7740-4f2f-95f8-52050136771d',
# '82a48044-4665-440f-98cc-8c74674eb7c2',
# 'd15ad9fd-1a49-4b58-85ea-8724ee7bd632',
# '253c776b-7107-4249-b7c2-2f5e8c4bf56b',
# 'bd4a6fd9-d6b5-4803-98ce-efee87bfe1cd',
# '1963617b-8545-49c8-b8be-32a4de3c8378',
# '65158d15-9c3e-42a3-92d9-4e3dc8e033df',
# '4187e802-a3f1-4aae-9acd-7d1996360b06',
# 'dd5a55e4-941f-44dc-a9aa-55f345f8ed80',
# '72419057-a034-4d64-b139-20cd17510e7b',
# '6d2c97ce-8bb6-437a-8490-5302f65a345d',
# '9242e388-6d79-479d-b7fc-a2b2859271f2',
# '49c020df-cc09-454d-a617-8aa490423cda',
# 'bb22115f-147c-4ba3-8b19-dd87ecacfe37',
# '7750d85d-68a0-4c26-8fa3-c3852b6f1796',
# '167d2c1c-1b05-4669-bbaf-ce2321c09f7d',
# 'bb998fc1-1c94-49fb-97c2-adf459c6c82d',
# 'e7c9bb71-e8d6-43b6-9657-f04d46828eeb',
# 'd9ee2534-5647-456f-88a0-9df874a95d78',
# '40c5ffd0-3baa-4060-83ec-d02aed6e2eae',
# '4fe3dfa2-0d98-4a5d-b391-2dd59af36067',
# '9e117498-5cd9-45f7-962d-df5e93c5268a',
# '9b68552a-5ec6-4ebf-8e9f-5994a2d345ce',
# 'ee1834e8-27ca-4a77-b69e-a89a7e93574c',
# '2cd2bfe8-1d08-477f-9bd1-dab8c8ae96cd',
# '58f6de32-7e31-49ec-89d4-f16d1336721f',
# 'de5ef058-3014-4bbb-885b-4579d83a651a',
# 'ce3c4e5a-4eb9-45ce-b3ce-ac5cef13fdd0',
# 'bb7da5be-39bb-493b-bd40-77929da532e3',
# 'a89afc31-578f-4179-96f5-9341e906bee5',
# 'ea94f193-958c-4d24-923b-4a339ecfc659',
# '1d021a79-6b68-4532-b41a-8f88198cbc27',
# 'd43732a4-4682-441c-8e44-fa6827f9caf8',
# '6ca9a771-6bae-4561-bb74-49db40e798ca',
# 'e55f253c-1d5f-47bb-8d9e-59c9b768e2f3',
# '0c9d3a7c-dd0b-4983-b290-843e4004c31b',
# 'b1809a25-9560-451f-83a5-17822c78eaa4',
# '11489e6e-ed7e-425d-8210-c4e8386b0cc4',
# '3f440116-0062-4045-b569-dee432465f95',
# 'a0c84b75-d582-4001-8751-958e7f13f2c1',
# '29263ff5-b5eb-4015-8098-476c3fef853f',
# '9cdf37e2-345d-4bd7-8c08-a979ed4b069b',
# '43d5f042-3607-4010-946a-5b3abb8c9e24',
# '4d078de2-dae2-43af-8612-19c792099e3d',
# '75235779-ec39-4645-a3b3-f2636bef8ab7',
# '63b3fc07-1416-4215-9311-3b98034cc962',
# 'fde23fe1-8a0c-4628-ba98-c05369a36207',
# '2791fb27-6ad9-479c-a8e0-9511532436b7',
# '6d17c340-fe1b-403a-bbb7-50c8dd6a5f5e',
# '8e3ccfe8-5fa8-4d3d-9e0f-94c63c7ef1d5',
# 'b2f36638-e750-4b07-ad5a-2e26ebf6d9ef',
# '5f09ea3e-7aec-42ec-97d1-c54a758560de',
# '3a1e93e1-5f44-4131-871e-401a5ced49dc',
# 'bbf6330e-1c37-409c-a709-fca4d983de6c',
# 'ae104e5d-897a-45e7-887c-5c9ce10dbbff',
# '27b8be54-f550-4e97-8c36-afc6e33aea85',
# 'de4c230c-8ee8-4415-8fff-7f84aa6ccd09',
# '2f382dad-9b66-46a6-b040-0eec22cd8cd6',
# '3dec9d10-a93e-447e-8f22-3d000c739756',
# '0cdad417-3184-48b1-8771-0b2ca2c5c35d',
# '647f230b-baa6-4eee-828d-24a317ded061',
# '6ae56a8e-39de-4624-ad93-b1567e41d7bc',
# '544c8204-419d-4f57-9527-8e19279585aa',
# 'e0d0b838-d5e0-4be6-a665-ea32b20aa36e',
# '54e450fa-4591-48c0-9941-b56110133e90',
# 'b7dd0912-e6e6-4fdc-b65a-420f8db7db07',
# 'bdcdd1e0-192d-4a52-aa9f-a44b26787a59',
# '19e85330-e59c-4276-b19c-8bda0332f5cc',
# 'd790d753-4bff-4817-9b5a-724727b75aec',
# '0ecb35b7-93ff-4323-87e7-83b64f5f01b6',
# '74e84ba3-7464-477e-b2e6-fddaa6629833',
# 'a351be5e-db63-4142-88af-a6d996327614',
# 'd0990848-0d4c-46c5-9be6-5edf53885b8e',
# '5aa8f196-d1b4-4b01-b180-cf90f09f447e',
# '22d0d5de-981c-4e3d-acd5-72427fa23f0a',
# '0ceaf49b-43f4-46cf-aa51-2acf63ee1cc3',
# 'ea658bc3-9eed-46fd-abf3-26f283f858ac',
# 'e3bdab62-4302-4f7b-8758-4f9c567160e1',
# '09d08d96-5a34-431a-b020-6175abff7553',
# '66eef510-5503-4141-96fb-75b039d32306',
# '5cf3361b-f253-4481-aff8-e0bf4074dc22',
# 'eed17479-2203-4770-b695-e7126679d533',
# '5c35bece-89e5-4cf1-af33-be13db7255de',
# '0a1c93a6-2ab3-454b-84f3-f841c999f7a3',
# 'e411bbac-77a9-4c46-bd74-88f8262c4e07',
# 'a1751fbf-2ca9-41ed-90e2-420de7f92fee',
# '20228a31-443f-48be-80d4-2f886f32f466',
# '1abc6e13-7ce0-4b76-95d3-fb3d03b6a975',
# 'f0c1dd79-d623-4668-a116-fd51ef36787f',
# 'e8557321-283c-4969-949d-fd8080523c11',
# 'b701bb32-341e-484b-b7f0-e84554614d7a',
# 'bf0ab342-43ac-4cef-a65c-1a20d6835fd1',
# '93876b34-2779-4911-ab7c-d59128c5914d',
# 'c2ebd242-234b-4b1b-bad1-138bb4464c41',
# 'dd5974bc-3ac9-471c-8e49-68b2b5efdfa9',
# '14901b60-d823-4ec4-8eb9-7d6b1c657ce7',
# '2543c51a-e112-4a5a-b12f-4a71b998f450'
]

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
            line = line.replace(':', r'\:')
            sql = f'INSERT INTO {table_name} VALUES {line}'
            # print(sql)
            conn.execute(sqlalchemy.text(sql))
        conn.commit()
      if meta['UUID'] == '65158d15-9c3e-42a3-92d9-4e3dc8e033df' \
        or meta['UUID'] == '49c020df-cc09-454d-a617-8aa490423cda' \
        or meta['UUID'] == '9e117498-5cd9-45f7-962d-df5e93c5268a' \
        or meta['UUID'] == 'ea94f193-958c-4d24-923b-4a339ecfc659' \
        or meta['UUID'] == '544c8204-419d-4f57-9527-8e19279585aa':
        print('log or record table, only import one data file, skip others..')
        break

def recovery_view(meta) -> None:
  global engine

  meta_file = f'{ROOT_PATH}{meta['UUID']}.meta.json'
  with open(meta_file, 'r', encoding='utf-8') as input:
    meta_json = json.load(input)
    ddl = meta_json['DDL']
    # print(ddl)
    with engine.connect() as conn:
      conn.execute(sqlalchemy.text(ddl))
      conn.commit()


def load_meta_file(meta) -> None:
  if any(meta['UUID'] in x for x in done_list):
    return
  
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
