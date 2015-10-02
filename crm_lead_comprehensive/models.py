# -*- coding: utf-8 -*-
# © 2015 Antiun Ingeniería, S.L.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import api, fields, models, tools


class Lead(models.Model):
    _inherit = "crm.lead"

    partner_trade_name = fields.Char()
    partner_vat = fields.Char()
    partner_phone = fields.Char()
    partner_mobile = fields.Char()
    partner_website = fields.Char()
    partner_online_shop = fields.Char()
    invoice_equal = fields.Boolean(
        "Use same adress for billing",
        default=True,
        help="Uncheck this option to specify a different billing address.")
    invoice_street = fields.Char()
    invoice_street2 = fields.Char()
    invoice_city = fields.Char()
    invoice_state_id = fields.Many2one("res.country.state", "Partner state")
    invoice_zip = fields.Char()
    invoice_country_id = fields.Many2one("res.country", "Partner country")

    @api.one
    @api.onchange("invoice_state_id")
    def _invoice_state_id_change(self):
        """Update country in UI."""
        if self.invoice_state_id:
            self.invoice_country_id = self.invoice_state_id.country_id

    @api.model
    def _lead_create_contact(self, lead, name, is_company, parent_id=False):
        """Mirror the right fields when creating a company."""
        if is_company:
            values = {
                "name": name,
                "user_id": lead.user_id.id,
                "comment": lead.description,
                "section_id": lead.section_id.id or False,
                "parent_id": parent_id,
                "phone": lead.partner_phone or lead.phone,
                "mobile": lead.partner_mobile or lead.mobile,
                "email": (tools.email_split(lead.email_from) and
                          tools.email_split(lead.email_from)[0] or False),
                "fax": lead.fax,
                "street": lead.street,
                "street2": lead.street2,
                "zip": lead.zip,
                "city": lead.city,
                "country_id": lead.country_id and lead.country_id.id or False,
                "state_id": lead.state_id and lead.state_id.id or False,
                "is_company": is_company,
                "type": "invoice",
            }

            if not lead.invoice_equal:
                values.update({
                    "street": lead.invoice_street or values["street"],
                    "street2": lead.invoice_street2 or values["street2"],
                    "zip": lead.invoice_zip or values["zip"],
                    "city": lead.invoice_city or values["city"],
                    "state_id": (lead.invoice_state_id and
                                 lead.invoice_state_id.id or
                                 values["state_id"]),
                    "country_id": (lead.invoice_country_id and
                                   lead.invoice_country_id.id or
                                   values["country_id"]),
                })

            # Transfer trade name if available with module ``l10n_es_partner``
            return self.env["res.partner"].with_context(
                default_comercial=lead.partner_trade_name).create(values)
        else:
            return super(Lead, self)._lead_create_contact(
                lead, name, is_company, parent_id)


class Partner(models.Model):
    _inherit = "res.partner"

    online_shop = fields.Char()
