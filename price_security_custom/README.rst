=======================================
Price Security Custom - Gauchocode
=======================================

This module customizes the behavior of the `price_security` module by adjusting the validation logic applied to sales orders.

Key Features
============

- Inherits `sale.order` model to override the constraint on `pricelist_id` and `payment_term_id`.
- **Removes the restriction** on pricelist priority comparison.
- **Keeps the restriction** on payment term priority comparison.
- The restriction applies only to users belonging to the group `price_security.group_only_view`.

Technical Details
=================

Python
------

* Inherits `sale.order` model.
* Adds a `@api.constrains` method that checks payment term priority but skips pricelist priority.

No views or external configuration is required.

Usage
=====

Users in the group `Only View Price Security` will see a validation error if they select a payment term with a higher priority than the one defined on the partner.

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
