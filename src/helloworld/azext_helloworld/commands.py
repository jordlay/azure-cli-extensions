# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=line-too-long
from azure.cli.core.commands import CliCommandType
from azext_helloworld._client_factory import cf_helloworld


def load_command_table(self, _):

    # TODO: Add command type here
    # helloworld_sdk = CliCommandType(
    #    operations_tmpl='<PATH>.operations#None.{}',
    #    client_factory=cf_helloworld)


    with self.command_group('helloworld') as g:
        g.custom_command('print', 'print_helloworld')
        g.custom_command('print-param', 'print_param')
        # g.command('delete', 'delete')
        # g.custom_command('list', 'list_helloworld')
        # g.show_command('show', 'get')
        # g.generic_update_command('update', setter_name='update', custom_func_name='update_helloworld')


    with self.command_group('helloworld', is_preview=True):
        pass

