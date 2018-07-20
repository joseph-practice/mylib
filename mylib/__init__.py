def display(record):
    for k in record.fields_get_keys():
        print('--------', k, '------')
        print(record[k])
        print('\n')

def displays(records, key):
    for record in records:
        print('------', record.id, '------')
        print(record[key])

def get_keys(model):
    return model.fields_get_keys()


def search_name_like(model, name):
    return model.search([('name', 'like', name)])

def get_model(env, name):
    return env.get(name)

def take_first(lst):
    print("i am taking first")
    print("dont mess with me!")
    return lst[0]