# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------


def cf_network_cl(cli_ctx, *_):
    from azure.cli.core.commands.client_factory import get_mgmt_service_client
    from azure.mgmt.network import NetworkManagementClient
    return get_mgmt_service_client(cli_ctx,
                                   NetworkManagementClient)


def cf_application_gateway(cli_ctx, *_):
    return cf_network_cl(cli_ctx).application_gateways


def cf_application_gateway_private_endpoint_connection(cli_ctx, *_):
    return cf_network_cl(cli_ctx).application_gateway_private_endpoint_connections


def cf_application_security_group(cli_ctx, *_):
    return cf_network_cl(cli_ctx).application_security_groups


def cf_web_category(cli_ctx, *_):
    return cf_network_cl(cli_ctx).web_categories


def cf_custom_ip_prefix(cli_ctx, *_):
    return cf_network_cl(cli_ctx).custom_ip_prefixes


def cf_express_route_circuit_connection(cli_ctx, *_):
    return cf_network_cl(cli_ctx).express_route_circuit_connections


def cf_express_route_circuit(cli_ctx, *_):
    return cf_network_cl(cli_ctx).express_route_circuits


def cf_express_route_cross_connection_peering(cli_ctx, *_):
    return cf_network_cl(cli_ctx).express_route_cross_connection_peerings


def cf_load_balancer_frontend_ip_configuration(cli_ctx, *_):
    return cf_network_cl(cli_ctx).load_balancer_frontend_ip_configurations


def cf_inbound_nat_rule(cli_ctx, *_):
    return cf_network_cl(cli_ctx).inbound_nat_rules


def cf_load_balancer_network_interface(cli_ctx, *_):
    return cf_network_cl(cli_ctx).load_balancer_network_interfaces


def cf_network_interface(cli_ctx, *_):
    return cf_network_cl(cli_ctx).network_interfaces


def cf_network_interface_ip_configuration(cli_ctx, *_):
    return cf_network_cl(cli_ctx).network_interface_ip_configurations


def cf_network_interface_load_balancer(cli_ctx, *_):
    return cf_network_cl(cli_ctx).network_interface_load_balancers


def cf_network_interface_tap_configuration(cli_ctx, *_):
    return cf_network_cl(cli_ctx).network_interface_tap_configurations


def cf_default_security_rule(cli_ctx, *_):
    return cf_network_cl(cli_ctx).default_security_rules


def cf_network_watcher(cli_ctx, *_):
    return cf_network_cl(cli_ctx).network_watchers


def cf_private_link_service(cli_ctx, *_):
    return cf_network_cl(cli_ctx).private_link_services


def cf_public_ip_address(cli_ctx, *_):
    return cf_network_cl(cli_ctx).public_ip_addresses


def cf_virtual_network(cli_ctx, *_):
    return cf_network_cl(cli_ctx).virtual_networks


def cf_subnet(cli_ctx, *_):
    return cf_network_cl(cli_ctx).subnets


def cf_resource_navigation_link(cli_ctx, *_):
    return cf_network_cl(cli_ctx).resource_navigation_links


def cf_service_association_link(cli_ctx, *_):
    return cf_network_cl(cli_ctx).service_association_links


def cf_virtual_network_gateway(cli_ctx, *_):
    return cf_network_cl(cli_ctx).virtual_network_gateways


def cf_virtual_network_gateway_connection(cli_ctx, *_):
    return cf_network_cl(cli_ctx).virtual_network_gateway_connections


def cf_virtual_network_tap(cli_ctx, *_):
    return cf_network_cl(cli_ctx).virtual_network_taps


def cf_vpn_site_link(cli_ctx, *_):
    return cf_network_cl(cli_ctx).vpn_site_links


def cf_vpn_gateway(cli_ctx, *_):
    return cf_network_cl(cli_ctx).vpn_gateways


def cf_vpn_connection(cli_ctx, *_):
    return cf_network_cl(cli_ctx).vpn_connections


def cf_vpn_site_link_connection(cli_ctx, *_):
    return cf_network_cl(cli_ctx).vpn_site_link_connections


def cf_nat_rule(cli_ctx, *_):
    return cf_network_cl(cli_ctx).nat_rules


def cf_p2svpn_gateway(cli_ctx, *_):
    return cf_network_cl(cli_ctx).p2_svpn_gateways


def cf_vpn_server_configuration_associated_with_virtual_wan(cli_ctx, *_):
    return cf_network_cl(cli_ctx).vpn_server_configurations_associated_with_virtual_wan


def cf_virtual_hub_bgp_connection(cli_ctx, *_):
    return cf_network_cl(cli_ctx).virtual_hub_bgp_connection


def cf_virtual_hub_bgp_connection(cli_ctx, *_):
    return cf_network_cl(cli_ctx).virtual_hub_bgp_connections


def cf_virtual_hub_ip_configuration(cli_ctx, *_):
    return cf_network_cl(cli_ctx).virtual_hub_ip_configuration