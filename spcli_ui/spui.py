#!/usr/bin/env python3

import os
from .sp_api import APPLIANCE
from .menu import *

def get_id(device_list,name):
    for device in device_list:
        if name in device:
            id = device[0].split('.')[0]
            return id

def get_name(device_list,name):
    for device in device_list:
        if name in device:
            id = device[1]
            return id

def main():
    main = main_menu()
    main_menu_exit = main[1]
    

    silverpeaks = APPLIANCE()._get_appliances_all()
    sp_list = []
    for device in silverpeaks:
        sp_list.append([device['id'],device['hostName']])

    sp_appliance = sp_appliance_menu(sp_list)
    



    while main_menu_exit == False:
        main_sel = main[0].show()
##########################################################################
#                              orchestrator
##########################################################################
        if main_sel == 1:
            orchestrator = orchestrator_menu()
            menu_back = orchestrator[1]
            while menu_back == False:
                orchestrator_select = orchestrator[0].show()

                if orchestrator_select == 0:
                    menu_back = True
                    
                elif orchestrator_select:
                    os.system(f"sp orch {orchestrator[2][orchestrator_select]}")
                    
            menu_back = False
##########################################################################
#                              appliance
##########################################################################

        if main_sel == 2:
            menu_back = sp_appliance[1]
            while menu_back == False:
                sp_appliance_select = sp_appliance[0].show()

                if sp_appliance_select == 0:
                    menu_back = True
                elif sp_appliance_select:
                    
                    index = sp_appliance_select - 1
                    appliance = appliance_menu(sp_list[index])

                    menu_back = appliance[1]   #
                    while menu_back == False:
                        appliance_select = appliance[0].show()
                        if appliance_select == 0:
                            menu_back = True    
                        elif appliance_select:
                            device_id = get_id(sp_list,sp_list[index][1])
                            os.system(f"sp appliance {appliance[2][appliance_select]} {device_id}")
                            print(" ")  
                    menu_back = False
            menu_back = False
##########################################################################
#                              bgp
##########################################################################
        if main_sel == 3:

            menu_back = sp_appliance[1]
            while menu_back == False:
                sp_appliance_select = sp_appliance[0].show()

                if sp_appliance_select == 0:
                    menu_back = True
                elif sp_appliance_select:

                    index = sp_appliance_select - 1
                    bgp = bgp_menu(sp_list[index])

                    menu_back = bgp[1]
                    while menu_back == False:
                        bgp_select = bgp[0].show()
                        if bgp_select == 0:
                            menu_back = True    
                        elif bgp_select:
                            device_id = get_id(sp_list,sp_list[index][1])
                            os.system(f"sp bgp {bgp[2][bgp_select]} {device_id}")
                            print(" ")  
                    menu_back = False
            menu_back = False
##########################################################################
#                              flows
##########################################################################
        if main_sel == 4:
            menu_back = sp_appliance[1]
            while menu_back == False:
                sp_appliance_select = sp_appliance[0].show()

                if sp_appliance_select == 0:
                    menu_back = True
                elif sp_appliance_select:

                    index = sp_appliance_select - 1
                    flows = flows_menu(sp_list[index])

                    menu_back = flows[1]
                    while menu_back == False:
                        flows_select = flows[0].show()
                        if flows_select == 0:
                            menu_back = True    
                        elif flows_select <= 3:
                            device_id = get_id(sp_list,sp_list[index][1])
                            os.system(f"sp flows {flows[2][flows_select]} -id {device_id}")
                            print(" ")  
                        elif flows_select >= 4:
                            device_id = get_id(sp_list,sp_list[index][1])
                            user_input = input(f'please provide {flows[2][flows_select]}: ')
                            os.system(f"sp flows {flows[2][flows_select]} {user_input} -id {device_id}")
                            print(" ")
                    menu_back = False
            menu_back = False
##########################################################################
#                              qos
##########################################################################
        if main_sel == 5:
            menu_back = sp_appliance[1]
            while menu_back == False:
                sp_appliance_select = sp_appliance[0].show()

                if sp_appliance_select == 0:
                    menu_back = True
                elif sp_appliance_select:
                    index = sp_appliance_select - 1
                    qos = qos_menu(sp_list[index])

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
##########################################################################
#                              ospf
##########################################################################
        if main_sel == 6:
            menu_back = sp_appliance[1]
            while menu_back == False:
                sp_appliance_select = sp_appliance[0].show()

                if sp_appliance_select == 0:
                    menu_back = True
                elif sp_appliance_select:
                    index = sp_appliance_select - 1
                    ospf = ospf_menu(sp_list[index])

                    menu_back = ospf[1]
                    while menu_back == False:
                        ospf_select = ospf[0].show()
                        if ospf_select == 0:
                            menu_back = True    
                        elif ospf_select:
                            device_id = get_id(sp_list,sp_list[ospf_select][1])
                            os.system(f"sp ospf {ospf[2][ospf_select]} {device_id}")
                            print(" ")  
                    menu_back = False
            menu_back = False

        elif main_sel == 0:
            main_menu_exit = True
            



if __name__ == "__main__":
    main()