# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.network import NetworkManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-network
# USAGE
    python firewall_policy_query_signature_overrides.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = NetworkManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="e747cc13-97d4-4a79-b463-42d7f4e558f2",
    )

    response = client.firewall_policy_idps_signatures.list(
        resource_group_name="rg1",
        firewall_policy_name="firewallPolicy",
        parameters={
            "filters": [{"field": "Mode", "values": ["Deny"]}],
            "orderBy": {"field": "severity", "order": "Ascending"},
            "resultsPerPage": 20,
            "search": "",
            "skip": 0,
        },
    )
    print(response)


# x-ms-original-file: specification/network/resource-manager/Microsoft.Network/stable/2022-07-01/examples/FirewallPolicyQuerySignatureOverrides.json
if __name__ == "__main__":
    main()
