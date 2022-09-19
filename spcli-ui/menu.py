from simple_term_menu import TerminalMenu
cursor = ">> "
menu_cursor_style = ("fg_red", "bold")
menu_style = ("bg_red", "fg_yellow")


def main_menu():
    title = "  Main Menu\n"
    items = ["-quit","-orchestrator", "-appliance","-bgp","-flows","-qos"]


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
    title = "  appliances\n"
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

def appliance_menu():
    title = "  appliance\n"
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


def bgp_menu():
    title = "  bgp\n"
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

def flows_menu():
    title = "  flows\n"
    items = ["-back","-all","-ip", "-port","-app","-dscp","-active","-inactive"]
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

def qos_menu():
    title = "  qos\n"
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