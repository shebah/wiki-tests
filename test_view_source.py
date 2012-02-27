#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
from unittestzero import Assert

import home_page
import view_source_page

class TestViewSource:

    def test_visitor_can_view_source(self, mozwebqa):
        home_pg = home_page.HomePage(mozwebqa)
        home_pg.go_to_home_page()
        home_pg.click_view_source()

        view_source_pg = view_source_page.ViewSourcePage(mozwebqa)

        Assert.true(view_source_pg.is_the_current_page)
        Assert.greater(len(view_source_pg.source_textarea.strip()), 0)