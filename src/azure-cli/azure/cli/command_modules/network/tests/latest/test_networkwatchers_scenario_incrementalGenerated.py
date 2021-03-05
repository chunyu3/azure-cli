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
from .example_steps import step_network_watcher_get_azure_reachability_report
from .example_steps import step_network_watcher_list_available_provider
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
    # STEP NOT FOUND: /NetworkWatchers/put/Create network watcher
    # STEP NOT FOUND: /NetworkWatchers/get/Get network watcher
    # STEP NOT FOUND: /NetworkWatchers/get/List network watchers
    # STEP NOT FOUND: /NetworkWatchers/get/List all network watchers
    # STEP NOT FOUND: /NetworkWatchers/post/Network configuration diagnostic
    # STEP NOT FOUND: /NetworkWatchers/post/Get troubleshoot result
    step_network_watcher_get_azure_reachability_report(test, checks=[])
    step_network_watcher_list_available_provider(test, checks=[])
    # STEP NOT FOUND: /NetworkWatchers/post/Get flow log status
    # STEP NOT FOUND: /NetworkWatchers/post/Get security group view
    # STEP NOT FOUND: /NetworkWatchers/post/Check connectivity
    # STEP NOT FOUND: /NetworkWatchers/post/Configure flow log
    # STEP NOT FOUND: /NetworkWatchers/post/Ip flow verify
    # STEP NOT FOUND: /NetworkWatchers/post/Get troubleshooting
    # STEP NOT FOUND: /NetworkWatchers/post/Get Topology
    # STEP NOT FOUND: /NetworkWatchers/post/Get next hop
    # STEP NOT FOUND: /NetworkWatchers/patch/Update network watcher tags
    # STEP NOT FOUND: /NetworkWatchers/delete/Delete network watcher
    cleanup_scenario(test)


# Test class for Scenario
@try_manual
class NetworkwatchersScenarioTest(ScenarioTest):
    def __init__(self, *args, **kwargs):
        super(NetworkwatchersScenarioTest, self).__init__(*args, **kwargs)
        self.kwargs.update({
            'subscription_id': self.get_subscription_id()
        })

        self.kwargs.update({
            'myApplicationGateway': 'appgw',
            'myNetworkInterface': 'nic1',
            'myPublicIpAddress': 'pub1',
            'myCustomIpPrefix': 'test-customipprefix',
            'myInboundNatRule': self.create_random_name(prefix='natRule1.1'[:5], length=10),
            'myDefaultSecurityRule': 'AllowVnetInBound',
            'myNetworkWatcher': 'nw1',
            'myVirtualNetwork': 'vnetName',
            'mySubnet': 'subnet1',
            'myVirtualNetworkGatewayConnection': 'vpngw',
            'myVpnSiteLink': 'vpnSiteLink1',
            'myVpnConnection': 'vpnConnection1',
            'myP2sVpnGateway': 'p2svpngateway',
            'myVirtualNetworkGateway': 'vpngateway',
        })

    @ResourceGroupPreparer(name_prefix='clitestnetwork_rg1'[:7], key='rg', parameter_name='rg')
    def test_networkwatchers_Scenario(self, rg):
        call_scenario(self)
        calc_coverage(__file__)
        raise_if()
