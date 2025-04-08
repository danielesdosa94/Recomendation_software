from welcome import *
from data import * 
from linkedlist import LinkedList

print_waveform()

def insert_plugin_type():
    # Crear una lista enlazada para almacenar los plugins
    plugin_type_list = LinkedList()
    
    # Insertar cada plugin en la lista enlazada
    for plugin in types:
        plugin_type_list.insert_beginning(plugin)
    
    return plugin_type_list

def insert_plugin_data():
    # Crear una lista enlazada para almacenar los plugins
    plugin_data_list = LinkedList()
    
    # Insertar cada plugin en la lista enlazada
    for plugin_type in types:
        plugin_sub_list = LinkedList()
        for plugin in plugins_data:
            if plugin[0] == plugin_type:
                plugin_sub_list.insert_beginning(plugin)
        plugin_data_list.insert_beginning(plugin_sub_list)
        
    return plugin_data_list

my_plugin_type_list = insert_plugin_type()
my_plugin_data_list = insert_plugin_data()

selected_plugin_type = ""

#User input to select plugin type

while len(selected_plugin_type) == 0:
    print("Por favor, selecciona un tipo de plugin:")
    print(my_plugin_type_list.stringify_list())
    selected_plugin_type = input("Escribe el tipo de plugin que deseas: ").strip().lower()
    if selected_plugin_type not in types:
        print("Tipo de plugin no válido. Por favor, intenta de nuevo.")
        selected_plugin_type = ""
    
    # Search for user_input in food types data structure here
    matching_plugin_types = []
    type_list_head = my_plugin_type_list.get_head_node()
    while type_list_head:
        if type_list_head.get_value() == selected_plugin_type:
            matching_plugin_types.append(type_list_head.get_value())
        type_list_head = type_list_head.get_next_node()

    #Print list of matching plugin types
    if matching_plugin_types:
        print(f"Encontrado: {matching_plugin_types[0]}")
    else:
        print("No se encontró el tipo de plugin seleccionado.") 

    # Check if only one type of plugin was found, ask user if they would like to select this type
    if len(matching_plugin_types) == 1:
        select_type = str(input(
            "\nThe only matching type for the specified input is " + matching_plugin_types[0] + ". \nQuieres mirarlo en " +
            matching_types[0] + " plugins? Aplasta s para si y n para no\n")).lower()
        # After finding plugin type write code for retrieving plugin data here
        if select_type == 's':
            selected_plugin_type = matching_plugin_types[0]
            print("Seleccionaste " + matching_plugin_types[0] + " plugins.")
            plugin_list_head = my_plugin_data_list.get_head_node()
            while plugin_list_head.get_next_node() is not None:
                sublist_head = plugin_list_head.get_value().get_head_node()
                if sublist_head.get_value()[0] == selected_plugin_type:
                    while sublist_head.get_next_node() is not None:
                        print(f"Plugin: {sublist_head.get_value()[1]}, Licencia: {sublist_head.get_value()[2]}")
                        sublist_head = sublist_head.get_next_node()
                plugin_list_head = plugin_list_head.get_next_node() 
                
        else:
            print("Entrada no válida. Por favor aplasta s o n.")

    # Ask user if they would like to search for other types of plugins
    search_other = str(input(
        "\nQuieres buscar otro tipo de plugins? Aplasta s para si o n para no\n")).lower()
    if search_other == 's':
        selected_plugin_type = ""
    elif search_other == 'n':
        print("Gracias por usar el sistema de recomendacion de plugins!")
        break
    