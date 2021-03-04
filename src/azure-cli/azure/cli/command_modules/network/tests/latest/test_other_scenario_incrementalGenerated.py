# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

import os
from azure.cli.testsdk import ScenarioTest
from azure.cli.testsdk import ResourceGroupPreparer
from .example_steps import step_vpn_site_link_connection_show
from .example_steps import step_default_security_rule_show
from .example_steps import step_resource_navigation_link_list
from .example_steps import step_service_association_link_list
from .example_steps import step_network_interface_ip_configuration_show
from .example_steps import step_default_security_rule_list
from .example_steps import step_vpn_site_link_show
from .example_steps import step_load_balancer_frontend_ip_configuration_list
from .example_steps import step_network_interface_ip_configuration_list
from .example_steps import step_network_interface_load_balancer_list
from .example_steps import step_load_balancer_network_interface_list2
from .example_steps import step_load_balancer_network_interface_list
from .example_steps import step_vpn_site_link_list
from .example_steps import step_vpn_server_configuration
from .. import (
    try_manual,
    raise_if,
    calc_coverage
)


TEST_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), '..'))


# Env setup_scenario
@try_manual
def setup_scenario(test):
    pass


# Env cleanup_scenario
@try_manual
def cleanup_scenario(test):
    pass


# Testcase: Scenario
@try_manual
def call_scenario(test):
    setup_scenario(test)
    step_vpn_site_link_connection_show(test, checks=[])
    step_default_security_rule_show(test, checks=[])
    # STEP NOT FOUND: /PeerExpressRouteCircuitConnections/get/PeerExpressRouteCircuitConnectionGet
    # STEP NOT FOUND: /LoadBalancerFrontendIPConfigurations/get/LoadBalancerFrontendIPConfigurationGet
    step_resource_navigation_link_list(test, checks=[])
    step_service_association_link_list(test, checks=[])
    step_network_interface_ip_configuration_show(test, checks=[])
    # STEP NOT FOUND: /LoadBalancerLoadBalancingRules/get/LoadBalancerLoadBalancingRuleGet
    # STEP NOT FOUND: /VpnLinkConnections/get/VpnSiteLinkConnectionList
    # STEP NOT FOUND: /HubVirtualNetworkConnections/get/HubVirtualNetworkConnectionGet
    # STEP NOT FOUND: /PeerExpressRouteCircuitConnections/get/List Peer ExpressRouteCircuit Connection
    # STEP NOT FOUND: /LoadBalancerOutboundRules/get/LoadBalancerOutboundRuleGet
    step_default_security_rule_list(test, checks=[])
    # STEP NOT FOUND: /ExpressRouteLinks/get/ExpressRouteLinkGet
    step_vpn_site_link_show(test, checks=[])
    step_load_balancer_frontend_ip_configuration_list(test, checks=[])
    # STEP NOT FOUND: /HubVirtualNetworkConnections/get/HubVirtualNetworkConnectionList
    step_network_interface_ip_configuration_list(test, checks=[])
    # STEP NOT FOUND: /LoadBalancerProbes/get/LoadBalancerProbeGet
    # STEP NOT FOUND: /AvailablePrivateEndpointTypes/get/Get available PrivateEndpoint types in the resource group
    # STEP NOT FOUND: //get/supportedSecurityProviders
    step_network_interface_load_balancer_list(test, checks=[])
    # STEP NOT FOUND: /LoadBalancerLoadBalancingRules/get/LoadBalancerLoadBalancingRuleList
    step_load_balancer_network_interface_list2(test, checks=[])
    step_load_balancer_network_interface_list(test, checks=[])
    # STEP NOT FOUND: /AvailableServiceAliases/get/Get available service aliases in the resource group
    # STEP NOT FOUND: /ExpressRouteLinks/get/ExpressRouteLinkGet
    # STEP NOT FOUND: /LoadBalancerOutboundRules/get/LoadBalancerOutboundRuleList
    # STEP NOT FOUND: /AvailableResourceGroupDelegations/get/Get available delegations in the resource group
    # STEP NOT FOUND: /LoadBalancerProbes/get/LoadBalancerProbeList
    step_vpn_site_link_list(test, checks=[])
    # STEP NOT FOUND: /AvailableEndpointServices/get/EndpointServicesList
    # STEP NOT FOUND: /AvailablePrivateEndpointTypes/get/Get available PrivateEndpoint types
    # STEP NOT FOUND: //get/Check Dns Name Availability
    # STEP NOT FOUND: /AvailableServiceAliases/get/Get available service aliases
    # STEP NOT FOUND: /AvailableDelegations/get/Get available delegations
    # STEP NOT FOUND: /ExpressRoutePortsLocations/get/ExpressRoutePortsLocationGet
    # STEP NOT FOUND: /ServiceTags/get/Get list of service tags
    # STEP NOT FOUND: /Usages/get/List usages
    # STEP NOT FOUND: /Usages/get/List usages spaced location
    # STEP NOT FOUND: /ExpressRouteServiceProviders/get/List ExpressRoute providers
    # STEP NOT FOUND: /ExpressRoutePortsLocations/get/ExpressRoutePortsLocationList
    # STEP NOT FOUND: /AzureFirewallFqdnTags/get/List all Azure Firewall FQDN Tags for a given subscription
    # STEP NOT FOUND: /BgpServiceCommunities/get/ServiceCommunityList
    # STEP NOT FOUND: /Operations/get/Get a list of operations for a resource provider
    # STEP NOT FOUND: //post/Deletes the specified active session
    # STEP NOT FOUND: //post/Create Bastion Shareable Links for the request VMs
    # STEP NOT FOUND: //post/Delete Bastion Shareable Links for the request VMs
    step_vpn_server_configuration(test, checks=[])
    # STEP NOT FOUND: //post/Returns the Bastion Shareable Links for the request VMs
    # STEP NOT FOUND: //post/Returns a list of currently active sessions on the Bastion
    # STEP NOT FOUND: //post/GenerateVirtualWanVpnServerConfigurationVpnProfile
    # STEP NOT FOUND: /VpnSitesConfiguration/post/VpnSitesConfigurationDownload
    cleanup_scenario(test)


# Test class for Scenario
@try_manual
class OtherScenarioTest(ScenarioTest):
    def __init__(self, *args, **kwargs):
        super(OtherScenarioTest, self).__init__(*args, **kwargs)
        self.kwargs.update({
            'subscription_id': self.get_subscription_id()
        })

        self.kwargs.update({
            'myApplicationGateway': 'appgw',
            'myCustomIpPrefix': 'test-customipprefix',
            'myInboundNatRule': self.create_random_name(prefix='natRule1.1'[:5], length=10),
            'myNetworkInterface': 'nic1',
            'myDefaultSecurityRule': 'AllowVnetInBound',
            'myNetworkWatcher': 'nw1',
            'myPublicIpAddress': 'pub1',
            'myVirtualNetwork': 'vnetName',
            'mySubnet': 'subnet1',
            'myVirtualNetworkGatewayConnection': 'vpngw',
            'myVpnSiteLink': 'vpnSiteLink1',
            'myVpnConnection': 'vpnConnection1',
            'myP2sVpnGateway': 'p2svpngateway',
            'myVirtualNetworkGateway': 'vpngateway',
        })

    @ResourceGroupPreparer(name_prefix='clitestnetwork_rg1'[:7], key='rg', parameter_name='rg')
    def test_other_Scenario(self, rg):
        call_scenario(self)
        calc_coverage(__file__)
        raise_if()