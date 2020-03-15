# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class FamilyAuxMassEdit(models.TransientModel):
    _inherit = 'clv.family_aux.mass_edit'

    reg_state = fields.Selection(
        [('draft', 'Draft'),
         ('revised', 'Revised'),
         ('done', 'Done'),
         ('canceled', 'Canceled')
         ], string='Register State', default=False, readonly=False, required=False
    )
    reg_state_selection = fields.Selection(
        [('set', 'Set'),
         ], string='Register State:', default=False, readonly=False, required=False
    )

    state = fields.Selection(
        [('new', 'New'),
         ('available', 'Available'),
         ('waiting', 'Waiting'),
         ('selected', 'Selected'),
         ('unselected', 'Unselected'),
         ('unavailable', 'Unavailable'),
         ('unknown', 'Unknown')
         ], string='State', default=False, readonly=False, required=False
    )
    state_selection = fields.Selection(
        [('set', 'Set'),
         ], string='State:', default=False, readonly=False, required=False
    )

    @api.multi
    def do_family_aux_mass_edit(self):
        self.ensure_one()

        super().do_family_aux_mass_edit()

        for family_aux in self.family_aux_ids:

            _logger.info(u'%s %s', '>>>>>', family_aux.name)

            if self.reg_state_selection == 'set':
                family_aux.reg_state = self.reg_state
            if self.reg_state_selection == 'remove':
                family_aux.reg_state = False

            if self.state_selection == 'set':
                family_aux.state = self.state
            if self.state_selection == 'remove':
                family_aux.state = False

        return True
