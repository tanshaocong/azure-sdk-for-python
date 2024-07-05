# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, IO, Union

from azure.identity import DefaultAzureCredential

from azure.mgmt.appplatform import AppPlatformManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-appplatform
# USAGE
    python deployments_create_or_update_custom_container.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = AppPlatformManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="00000000-0000-0000-0000-000000000000",
    )

    response = client.deployments.begin_create_or_update(
        resource_group_name="myResourceGroup",
        service_name="myservice",
        app_name="myapp",
        deployment_name="mydeployment",
        deployment_resource={
            "properties": {
                "deploymentSettings": {
                    "environmentVariables": {"env": "test"},
                    "livenessProbe": {
                        "disableProbe": False,
                        "failureThreshold": 3,
                        "initialDelaySeconds": 30,
                        "periodSeconds": 10,
                        "probeAction": {"path": "/health", "scheme": "HTTP", "type": "HTTPGetAction"},
                    },
                    "readinessProbe": {
                        "disableProbe": False,
                        "failureThreshold": 3,
                        "initialDelaySeconds": 30,
                        "periodSeconds": 10,
                        "probeAction": {"path": "/health", "scheme": "HTTP", "type": "HTTPGetAction"},
                    },
                    "resourceRequests": {"cpu": "1000m", "memory": "3Gi"},
                    "startupProbe": None,
                    "terminationGracePeriodSeconds": 30,
                },
                "instances": None,
                "source": {
                    "customContainer": {
                        "args": ["-c", "while true; do echo hello; sleep 10;done"],
                        "command": ["/bin/sh"],
                        "containerImage": "myContainerImage:v1",
                        "imageRegistryCredential": {"password": "myPassword", "username": "myUsername"},
                        "languageFramework": "springboot",
                        "server": "myacr.azurecr.io",
                    },
                    "type": "Container",
                },
            }
        },
    ).result()
    print(response)


# x-ms-original-file: specification/appplatform/resource-manager/Microsoft.AppPlatform/stable/2023-12-01/examples/Deployments_CreateOrUpdate_CustomContainer.json
if __name__ == "__main__":
    main()
