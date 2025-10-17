# -*- coding: utf-8 -*-
from odoo import models, fields, api

class ChainedRecord(models.AbstractModel):
    _name = 'chained.record.mixin'
    _description = 'Chained Record'

    previous_id = fields.Many2one(
        string='Previous Record',
        ondelete='set null'
    )
    next_id = fields.Many2one(
        string='Next Record',
        ondelete='set null'
    )

