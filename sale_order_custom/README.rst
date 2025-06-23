=============================
Sale Order Line Enhancements
=============================

This module customizes the printed quotation report to reflect tax-included unit prices.

**Main Features**:
- Extends the `sale.order.line` model to compute and display the unit price including taxes.
- Updates the quotation (`sale.order`) report template to show this new value.

Usage
=====

When generating a quotation PDF, the report will now show unit prices that include tax.

Technical Details
=================

Python
------
* Inherits `sale.order.line` to compute unit price with tax (`price_unit_taxed`).

XML
---
* Modifies report template to include new field in the printed quotation.

Credits
=======

Authors
-------

* Gauchocode

Maintainers
-----------

This module is maintained by Gauchocode.

.. image:: https://gauchocode.com/logo.png
   :alt: Gauchocode

Repository
----------

https://gitlab.com/broobe/odoo/gc-odoo-ramos-addons
