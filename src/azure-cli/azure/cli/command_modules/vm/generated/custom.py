# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=line-too-long
# pylint: disable=too-many-lines

from azure.cli.core.util import sdk_no_wait


def vm_ssh_public_key_list(client,
                           resource_group_name=None):
    if resource_group_name:
        return client.list_by_resource_group(resource_group_name=resource_group_name)
    return client.list_by_subscription()


def vm_ssh_public_key_show(client,
                           resource_group_name,
                           ssh_public_key_name):
    return client.get(resource_group_name=resource_group_name,
                      ssh_public_key_name=ssh_public_key_name)


def vm_ssh_public_key_create(client,
                             resource_group_name,
                             ssh_public_key_name,
                             location,
                             tags=None,
                             public_key=None):
    parameters = {}
    parameters['location'] = location
    parameters['tags'] = tags
    parameters['public_key'] = public_key
    return client.create(resource_group_name=resource_group_name,
                         ssh_public_key_name=ssh_public_key_name,
                         parameters=parameters)


def vm_ssh_public_key_update(client,
                             resource_group_name,
                             ssh_public_key_name,
                             tags=None,
                             public_key=None):
    return client.update(resource_group_name=resource_group_name,
                         ssh_public_key_name=ssh_public_key_name,
                         tags=tags,
                         public_key=public_key)


def vm_ssh_public_key_delete(client,
                             resource_group_name,
                             ssh_public_key_name):
    return client.delete(resource_group_name=resource_group_name,
                         ssh_public_key_name=ssh_public_key_name)


def vm_ssh_public_key_generate_key_pair(client,
                                        resource_group_name,
                                        ssh_public_key_name):
    return client.generate_key_pair(resource_group_name=resource_group_name,
                                    ssh_public_key_name=ssh_public_key_name)


def vm_virtual_machine_reimage(client,
                               resource_group_name,
                               vm_name,
                               temp_disk=None,
                               no_wait=False):
    return sdk_no_wait(no_wait,
                       client.reimage,
                       resource_group_name=resource_group_name,
                       vm_name=vm_name,
                       temp_disk=temp_disk)


def vm_virtual_machine_scale_set_force_recovery_service_fabric_platform_update_domain_walk(client,
                                                                                           resource_group_name,
                                                                                           vm_scale_set_name,
                                                                                           platform_update_domain):
    return client.force_recovery_service_fabric_platform_update_domain_walk(resource_group_name=resource_group_name,
                                                                            vm_scale_set_name=vm_scale_set_name,
                                                                            platform_update_domain=platform_update_domain)


def vm_virtual_machine_scale_set_redeploy(client,
                                          resource_group_name,
                                          vm_scale_set_name,
                                          instance_ids=None,
                                          no_wait=False):
    return sdk_no_wait(no_wait,
                       client.redeploy,
                       resource_group_name=resource_group_name,
                       vm_scale_set_name=vm_scale_set_name,
                       instance_ids=instance_ids)


def vm_virtual_machine_scale_set_reimage_all(client,
                                             resource_group_name,
                                             vm_scale_set_name,
                                             instance_ids=None,
                                             no_wait=False):
    return sdk_no_wait(no_wait,
                       client.reimage_all,
                       resource_group_name=resource_group_name,
                       vm_scale_set_name=vm_scale_set_name,
                       instance_ids=instance_ids)


def vm_virtual_machine_scale_set_vm_extension_list(client,
                                                   resource_group_name,
                                                   vm_scale_set_name,
                                                   instance_id,
                                                   expand=None):
    return client.list(resource_group_name=resource_group_name,
                       vm_scale_set_name=vm_scale_set_name,
                       instance_id=instance_id,
                       expand=expand)


def vm_virtual_machine_scale_set_vm_extension_show(client,
                                                   resource_group_name,
                                                   vm_scale_set_name,
                                                   instance_id,
                                                   vm_extension_name,
                                                   expand=None):
    return client.get(resource_group_name=resource_group_name,
                      vm_scale_set_name=vm_scale_set_name,
                      instance_id=instance_id,
                      vm_extension_name=vm_extension_name,
                      expand=expand)


def vm_virtual_machine_scale_set_vm_extension_create(client,
                                                     resource_group_name,
                                                     vm_scale_set_name,
                                                     instance_id,
                                                     vm_extension_name,
                                                     force_update_tag=None,
                                                     publisher=None,
                                                     type_properties_type=None,
                                                     type_handler_version=None,
                                                     auto_upgrade_minor_version=None,
                                                     enable_automatic_upgrade=None,
                                                     settings=None,
                                                     protected_settings=None,
                                                     name=None,
                                                     type_=None,
                                                     virtual_machine_extension_instance_view_type_handler_version_type_handler_version=None,
                                                     substatuses=None,
                                                     statuses=None,
                                                     no_wait=False):
    extension_parameters = {}
    extension_parameters['force_update_tag'] = force_update_tag
    extension_parameters['publisher'] = publisher
    extension_parameters = type_properties_type
    extension_parameters['type_handler_version'] = type_handler_version
    extension_parameters['auto_upgrade_minor_version'] = auto_upgrade_minor_version
    extension_parameters['enable_automatic_upgrade'] = enable_automatic_upgrade
    extension_parameters['settings'] = settings
    extension_parameters['protected_settings'] = protected_settings
    extension_parameters['instance_view'] = {}
    extension_parameters['instance_view']['name'] = name
    extension_parameters['instance_view']['type'] = type_
    extension_parameters['instance_view']['type_handler_version'] = virtual_machine_extension_instance_view_type_handler_version_type_handler_version
    extension_parameters['instance_view']['substatuses'] = substatuses
    extension_parameters['instance_view']['statuses'] = statuses
    return sdk_no_wait(no_wait,
                       client.create_or_update,
                       resource_group_name=resource_group_name,
                       vm_scale_set_name=vm_scale_set_name,
                       instance_id=instance_id,
                       vm_extension_name=vm_extension_name,
                       extension_parameters=extension_parameters)


def vm_virtual_machine_scale_set_v_ms_redeploy(client,
                                               resource_group_name,
                                               vm_scale_set_name,
                                               instance_id,
                                               no_wait=False):
    return sdk_no_wait(no_wait,
                       client.redeploy,
                       resource_group_name=resource_group_name,
                       vm_scale_set_name=vm_scale_set_name,
                       instance_id=instance_id)


def vm_virtual_machine_scale_set_v_ms_reimage_all(client,
                                                  resource_group_name,
                                                  vm_scale_set_name,
                                                  instance_id,
                                                  no_wait=False):
    return sdk_no_wait(no_wait,
                       client.reimage_all,
                       resource_group_name=resource_group_name,
                       vm_scale_set_name=vm_scale_set_name,
                       instance_id=instance_id)


def vm_virtual_machine_scale_set_v_ms_retrieve_boot_diagnostic_data(client,
                                                                    resource_group_name,
                                                                    vm_scale_set_name,
                                                                    instance_id,
                                                                    sas_uri_expiration_time_in_minutes=None):
    return client.retrieve_boot_diagnostics_data(resource_group_name=resource_group_name,
                                                 vm_scale_set_name=vm_scale_set_name,
                                                 instance_id=instance_id,
                                                 sas_uri_expiration_time_in_minutes=sas_uri_expiration_time_in_minutes)


def vm_virtual_machine_scale_set_vm_run_command_list(client,
                                                     resource_group_name,
                                                     vm_scale_set_name,
                                                     instance_id,
                                                     expand=None):
    return client.list(resource_group_name=resource_group_name,
                       vm_scale_set_name=vm_scale_set_name,
                       instance_id=instance_id,
                       expand=expand)


def vm_disk_access_delete(client,
                          resource_group_name,
                          disk_access_name,
                          private_endpoint_connection_name,
                          no_wait=False):
    return sdk_no_wait(no_wait,
                       client.delete_a_private_endpoint_connection,
                       resource_group_name=resource_group_name,
                       disk_access_name=disk_access_name,
                       private_endpoint_connection_name=private_endpoint_connection_name)


def vm_disk_access_show_private_link_resource(client,
                                              resource_group_name,
                                              disk_access_name):
    return client.get_private_link_resources(resource_group_name=resource_group_name,
                                             disk_access_name=disk_access_name)


def vm_gallery_application_list(client,
                                resource_group_name,
                                gallery_name):
    return client.list_by_gallery(resource_group_name=resource_group_name,
                                  gallery_name=gallery_name)


def vm_gallery_application_show(client,
                                resource_group_name,
                                gallery_name,
                                gallery_application_name):
    return client.get(resource_group_name=resource_group_name,
                      gallery_name=gallery_name,
                      gallery_application_name=gallery_application_name)


def vm_gallery_application_create(client,
                                  resource_group_name,
                                  gallery_name,
                                  gallery_application_name,
                                  location,
                                  tags=None,
                                  description=None,
                                  eula=None,
                                  privacy_statement_uri=None,
                                  release_note_uri=None,
                                  end_of_life_date=None,
                                  supported_os_type=None,
                                  no_wait=False):
    gallery_application = {}
    gallery_application['location'] = location
    gallery_application['tags'] = tags
    gallery_application['description'] = description
    gallery_application['eula'] = eula
    gallery_application['privacy_statement_uri'] = privacy_statement_uri
    gallery_application['release_note_uri'] = release_note_uri
    gallery_application['end_of_life_date'] = end_of_life_date
    gallery_application['supported_os_type'] = supported_os_type
    return sdk_no_wait(no_wait,
                       client.create_or_update,
                       resource_group_name=resource_group_name,
                       gallery_name=gallery_name,
                       gallery_application_name=gallery_application_name,
                       gallery_application=gallery_application)


def vm_gallery_application_delete(client,
                                  resource_group_name,
                                  gallery_name,
                                  gallery_application_name,
                                  no_wait=False):
    return sdk_no_wait(no_wait,
                       client.delete,
                       resource_group_name=resource_group_name,
                       gallery_name=gallery_name,
                       gallery_application_name=gallery_application_name)


def vm_gallery_application_version_list(client,
                                        resource_group_name,
                                        gallery_name,
                                        gallery_application_name):
    return client.list_by_gallery_application(resource_group_name=resource_group_name,
                                              gallery_name=gallery_name,
                                              gallery_application_name=gallery_application_name)
