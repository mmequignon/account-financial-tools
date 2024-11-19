# Copyright 2021 Akretion France (http://www.akretion.com/)
# Copyright 2022 Vauxoo (https://www.vauxoo.com/)
# @author: Alexis de Lattre <alexis.delattre@akretion.com>
# @author: Moisés López <moylop260@vauxoo.com>
# @author: Francisco Luna <fluna@vauxoo.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Account Move Number Sequence",
    "version": "14.0.1.4.5",
    "category": "Accounting",
    "license": "AGPL-3",
    "summary": "Generate journal entry number from sequence",
    "author": "Akretion,Vauxoo,Odoo Community Association (OCA)",
    "maintainers": ["alexis-via", "moylop260", "luisg123v"],
    "website": "https://github.com/OCA/account-financial-tools",
    "depends": [
        "account",
    ],
    # TODO: This conflicts with the account_online_sync enterprise addon
    # which is automatically installed
    # "demo": [
        # "demo/ir_sequence_demo.xml",
        # "demo/account_journal_demo.xml",
    # ],
    "data": [
        "views/account_journal_views.xml",
        "views/account_move_views.xml",
        "security/ir.model.access.csv",
    ],
    "post_init_hook": "create_journal_sequences",
    "installable": True,
}
