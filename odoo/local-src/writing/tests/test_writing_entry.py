# Copyright 2016 Camptocamp
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo.tests import TransactionCase, tagged

@tagged("-at_install", "post_install")
class TestWritingEntry(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # No need for tracking and we scratch some seconds
        cls.env = cls.env(context=dict(cls.env.context, tracking_disable=True))
        
        cls.entry_notes = cls.env['writing.entry'].create(
            {'name': 'Notes', 'content': 'Some content'}
        )
        cls.entry_ideas = cls.env['writing.entry'].create(
            {'name': 'Ideas', 'content': ''}
        )

    def test_01_basics(self):
        """Basic tests just to practice writing test cases"""
        self.assertEqual(
            self.entry_notes.nb_symbols,
            12,
            "Notes entry should have 12 symbols",
        )
        self.assertEqual(
            self.entry_ideas.nb_symbols,
            0,
            "Ideas entry should have 0 symbols",
        )
        self.assertEqual(
            self.entry_ideas.user_id.id,
            self.env.uid,
            "The author of the entry should be the current user"
        )
