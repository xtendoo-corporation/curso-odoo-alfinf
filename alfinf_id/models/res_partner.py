# © 2023 Manuel Calero (Xtendoo, https://xtendoo.es/)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    alfinf_id = fields.Integer(
        string="Alfinf ID",
    )
