from create_action import *
from create_container import *
from create_reducer import *
file_name = 'ComponentName'
component_path = 'actions/' + file_name + '.js'

make_action(file_name)
make_container (file_name, component_path)
make_reducer(file_name)



