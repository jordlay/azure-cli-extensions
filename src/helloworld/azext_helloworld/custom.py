# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.util import CLIError


def print_helloworld():
    print("HELLOWORLD")


def print_param(param):
    print("hello2", param)


def create_helloworld(cmd, resource_group_name, helloworld_name, location=None, tags=None):
    raise CLIError('TODO: Implement `helloworld create`')


def list_helloworld(cmd, resource_group_name=None):
    raise CLIError('TODO: Implement `helloworld list`')


def update_helloworld(cmd, instance, tags=None):
    with cmd.update_context(instance) as c:
        c.set_param('tags', tags)
    return instance
