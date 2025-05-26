==========================
Fix Default Storage
==========================

Este módulo corrige el comportamiento del campo ``warehouse_id`` en ``sale.order`` para que, por defecto, se seleccione uno de los almacenes asociados al usuario actual.

.. image:: https://img.shields.io/badge/license-AGPL--3-blue.png
   :target: https://www.gnu.org/licenses/agpl
   :alt: License: AGPL-3
.. image:: https://img.shields.io/badge/GitLab-Repositorio-orange?logo=gitlab
   :target: https://gitlab.com/broobe/odoo/gc-odoo-ramos-addons
   :alt: Repositorio en GitLab

**Tabla de contenidos**

.. contents::
    :local:

Descripción
===========

Por defecto, Odoo asigna un almacén predeterminado en los pedidos de venta. Este módulo modifica ese comportamiento para que el almacén por defecto sea uno de los almacenes del usuario que crea el pedido.

Uso
===

1. Instale el módulo.
2. Cree un nuevo pedido de venta.
3. El campo ``Almacén`` se completará automáticamente con uno de los almacenes asignados al usuario actual.

Créditos
========

Autores
-------

* Gauchocode

Mantenedores
------------
* Gauchocode

Licencia
========

Este módulo está licenciado bajo la AGPL-3.
