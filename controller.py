import view, import_data, export_data

def start():
    action = view.menu_action()
    if action == 1:
        import_data.add_data()
    #if action == 4:
        #export_data.print_name()
    if action == 5:
        export_data.print_data()
    if action == 6:
        export_data.print_name()
    if action == 7:
        export_data.sort_name()
    if action == 8:
        export_data.sort_id()
        
    
    
    

