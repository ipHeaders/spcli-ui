from simple_term_menu import TerminalMenu
cursor = ">> "
menu_cursor_style = ("fg_red", "bold")
menu_style = ("bg_red", "fg_yellow")


def main_menu():
    title = "  Main Menu\n"
    items = ["-quit","-orchestrator", "-appliance","-bgp","-flows","-qos","-ospf"]


    menu_exit = False

    menu = TerminalMenu(
        menu_entries=items,
        title=title,
        menu_cursor=cursor,
        menu_cursor_style=menu_cursor_style,
        menu_highlight_style=menu_style,
        cycle_cursor=True,
        clear_screen=True,
        show_search_hint=True,
    )
    return (menu,menu_exit)




def orchestrator_menu():
    title = "  orchestrator\n"
    items = ["-back","-info", "-allowedip", "-users" ,"-sessions", "-backup"]
    menu_back = False
    menu = TerminalMenu(
        menu_entries=items,
        title=title,
        menu_cursor=cursor,
        menu_cursor_style=menu_cursor_style,
        menu_highlight_style=menu_style,
        cycle_cursor=True,
        clear_screen=False,
        show_search_hint=True
    )
    return (menu,menu_back,items)


def sp_appliance_menu(device_list:list):
    title = "  select edge connect\n"
    items = ["-back"]

    for d in device_list:
        items.append(d[1])

    menu_back = False
    menu = TerminalMenu(
        menu_entries=items,
        title=title,
        menu_cursor=cursor,
        menu_cursor_style=menu_cursor_style,
        menu_highlight_style=menu_style,
        cycle_cursor=True,
        clear_screen=False,
        show_search_hint=True
    )
    return (menu,menu_back,items)

def appliance_menu(name):
    title = f"  edge-device: {name}\n"
    items = ["-back", "-info", "-interfaces" ,"-stat_config", "-os_version","-banner","-dns","-syslog"]
    menu_back = False
    menu = TerminalMenu(
        menu_entries=items,
        title=title,
        menu_cursor=cursor,
        menu_cursor_style=menu_cursor_style,
        menu_highlight_style=menu_style,
        cycle_cursor=True,
        clear_screen=False,
        show_search_hint=True
    )
    return (menu,menu_back,items)


def bgp_menu(name):
    title = f"  bgp: {name}\n"
    items = ["-back","-config","-neighbors", "-summary"]
    menu_back = False
    menu = TerminalMenu(
        menu_entries=items,
        title=title,
        menu_cursor=cursor,
        menu_cursor_style=menu_cursor_style,
        menu_highlight_style=menu_style,
        cycle_cursor=True,
        clear_screen=False,
        show_search_hint=True
    )
    return (menu,menu_back,items)

def flows_menu(name):
    title = f"  flows: {name}\n"
    items = ["-back","-all","-active","-inactive","-ip", "-port","-app","-dscp"]
    menu_back = False
    menu = TerminalMenu(
        menu_entries=items,
        title=title,
        menu_cursor=cursor,
        menu_cursor_style=menu_cursor_style,
        menu_highlight_style=menu_style,
        cycle_cursor=True,
        clear_screen=False,
        show_search_hint=True
    )
    return (menu,menu_back,items)

def qos_menu(name):
    title = f"  qos {name}\n"
    items = ["-back","-inbound_shaper"]
    menu_back = False
    menu = TerminalMenu(
        menu_entries=items,
        title=title,
        menu_cursor=cursor,
        menu_cursor_style=menu_cursor_style,
        menu_highlight_style=menu_style,
        cycle_cursor=True,
        clear_screen=False,
        show_search_hint=True
    )
    return (menu,menu_back,items)

def ospf_menu(name):
    title = f"  ospf {name}\n"
    items = ["-back","-config","-state"]
    menu_back = False
    menu = TerminalMenu(
        menu_entries=items,
        title=title,
        menu_cursor=cursor,
        menu_cursor_style=menu_cursor_style,
        menu_highlight_style=menu_style,
        cycle_cursor=True,
        clear_screen=False,
        show_search_hint=True
    )
    return (menu,menu_back,items)