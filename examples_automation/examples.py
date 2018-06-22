# ------------------------------------------------------------------------------------------------------------------------
# import random
# import string
#
# def get_random_string(range=6):
#     return ''.join([random.choice(string.lowercase) for i in xrange(range)])        # chose random string of 6 digits
#
#
# site_name = 'site_{}'.format(get_random_string())                                   # create random site name
#
# group_name = 'group_{}'.format(get_random_string())                                 # create random group name
#
# ------------------------------------------------------------------------------------------------------------------------
# print site_name
# print group_name
# 
#
# def pick_the_site(driver, site_name):                                        # Pick site accotrding to the entered name
#     with STEP('Pick the Site'):
#         MainPage(driver).sites_drop_down.search_input.click()
#         MainPage(driver).sites_drop_down.search_input.enter_text(site_name)
#         MainPage(driver).sites_drop_down.search_btn.click()
#         MainPage(driver).sites_drop_down.select_by_text(site_name)
#
#
# def pick_the_group(driver, group_name):                                      # Pick group accotrding to the entered name
#     with STEP('Pick the Group'):
#         MainPage(driver).left_side_tabs.network_tab.click()
#         GroupsDropDown(driver).search_input.click()
#         GroupsDropDown(driver).search_input.enter_text(group_name)
#         GroupsDropDown(driver).search_btn.click()
#         GroupsDropDown(driver).select_static_by_text(group_name)
#
# ------------------------------------------------------------------------------------------------------------------------
#
#     with STEP("Verify the 'File type' exclusion sent to all agents"):     # ToDo Gosha
#          pass
#
# ------------------------------------------------------------------------------------------------------------------------
#
#     site_name = 'site1_{}'.format(get_random_string())
#     site_name = 'site2_{}'.format(get_random_string())
#     group_name = 'group1_{}'.format(get_random_string())
#     group_name = 'group2_{}'.format(get_random_string())
#
# ------------------------------------------------------------------------------------------------------------------------
#
#     def pick_the_site(driver, site1_name):
#         with STEP('Pick the Site'):
#             MainPage(driver).sites_drop_down.search_input.click()
#             MainPage(driver).sites_drop_down.search_input.enter_text(site1_name)
#             MainPage(driver).sites_drop_down.search_btn.click()
#             MainPage(driver).sites_drop_down.select_by_text(site1_name)
#
# ------------------------------------------------------------------------------------------------------------------------
