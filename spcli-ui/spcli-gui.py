#!/usr/bin/env python3

import os
import sp_api
from menu import *

def get_id(device_list,name):
    for device in device_list:
        if name in device:
            id = device[0].split('.')[0]
            return id


def main():
    main = main_menu()
    main_menu_exit = main[1]
    
    orchestrator = orchestrator_menu()
    appliance = appliance_menu()
    bgp = bgp_menu()
    flows = flows_menu()
    qos = qos_menu()

    silverpeaks = sp_api.APPLIANCE()._get_appliances_all()
    sp_list = []
    for device in silverpeaks:
        sp_list.append([device['id'],device['hostName']])

    sp_appliance = sp_appliance_menu(sp_list)
    



    while main_menu_exit == False:
        main_sel = main[0].show()
##############################################################################################################################
        if main_sel == 1:
            menu_back = orchestrator[1]
            while menu_back == False:
                orchestrator_select = orchestrator[0].show()

                if orchestrator_select == 0:
                    menu_back = True
                    
                elif orchestrator_select:
                    os.system(f"sp orch {orchestrator[2][orchestrator_select]}")
                    
            menu_back = False
##############################################################################################################################
        if main_sel == 2:
            menu_back = sp_appliance[1]
            while menu_back == False:
                sp_appliance_select = sp_appliance[0].show()

                if sp_appliance_select == 0:
                    menu_back = True
                elif sp_appliance_select:
                    menu_back = appliance[1]
                    while menu_back == False:
                        appliance_select = appliance[0].show()
                        if appliance_select == 0:
                            menu_back = True    
                        elif appliance_select:
                            device_id = get_id(sp_list,sp_list[appliance_select][1])
                            os.system(f"sp appliance {appliance[2][appliance_select]} {device_id}")
                            print(" ")  
                    menu_back = False
            menu_back = False
##############################################################################################################################
        if main_sel == 3:
            menu_back = bgp[1]
            while menu_back == False:
                sp_appliance_select = sp_appliance[0].show()

                if sp_appliance_select == 0:
                    menu_back = True
                elif sp_appliance_select:
                    menu_back = bgp[1]
                    while menu_back == False:
                        bgp_select = bgp[0].show()
                        if bgp_select == 0:
                            menu_back = True    
                        elif bgp_select:
                            device_id = get_id(sp_list,sp_list[bgp_select][1])
                            os.system(f"sp bgp {bgp[2][bgp_select]} {device_id}")
                            print(" ")  
                    menu_back = False
            menu_back = False
##############################################################################################################################
        if main_sel == 4:
            menu_back = flows[1]
            while menu_back == False:
                sp_appliance_select = sp_appliance[0].show()

                if sp_appliance_select == 0:
                    menu_back = True
                elif sp_appliance_select:
                    menu_back = flows[1]
                    while menu_back == False:
                        flows_select = flows[0].show()
                        if flows_select == 0:
                            menu_back = True    
                        elif flows_select:
                            device_id = get_id(sp_list,sp_list[flows_select][1])
                            os.system(f"sp flows {flows[2][flows_select]} -id {device_id}")
                            print(" ")  
                    menu_back = False
            menu_back = False
##############################################################################################################################
        if main_sel == 5:
            menu_back = qos[1]
            while menu_back == False:
                sp_appliance_select = sp_appliance[0].show()

                if sp_appliance_select == 0:
                    menu_back = True
                elif sp_appliance_select:
                    menu_back = qos[1]
                    while menu_back == False:
                        qos_select = qos[0].show()
                        if qos_select == 0:
                            menu_back = True    
                        elif qos_select:
                            device_id = get_id(sp_list,sp_list[qos_select][1])
                            os.system(f"sp qos {qos[2][qos_select]} {device_id}")
                            print(" ")  
                    menu_back = False
            menu_back = False


        elif main_sel == 0:
            main_menu_exit = True
            



if __name__ == "__main__":
    main()