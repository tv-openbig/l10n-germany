# Copyright 2022 Hunki Enterprises BV
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import fields, models


class AccountAccount(models.Model):
    _inherit = "account.account"

    datev_export_nonautomatic = fields.Boolean(
        "Suppress automatic calculations in DATEV",
        default=True,
        help="When this flag is set, journal items from this account will be exported "
        "with field 'BU-Schlussel' set to '40', which inhibits automatic calculations "
        "in DATEV.",
    )
