# -*- coding: utf-8 -*-
from odoo import models, fields, api

class WritingEntry(models.Model):
    _name = 'writing.entry'
    _description = 'Writing Entry'

    name = fields.Char(string='Title', required=True)
    content = fields.Text(string='Content')
    user_id = fields.Many2one(comodel_name='res.users', string='Author', default=lambda self: self.env.uid)
    nb_symbols = fields.Integer(string='Number of Symbols', compute='_compute_nb_symbols')

    @api.depends('content')
    def _compute_nb_symbols(self):
        for entry in self:
            entry.nb_symbols = len(entry.content) if entry.content else 0
