===========================================
Restricción de impresión de facturas por diario
===========================================

.. image:: https://img.shields.io/badge/license-LGPL--3-blue.svg
   :target: https://www.gnu.org/licenses/lgpl-3.0-standalone.html
   :alt: License: LGPL-3

Este módulo permite restringir la impresión de facturas para diarios seleccionados.
Si el diario tiene activada la opción de restricción, cualquier intento de imprimir una factura asociada a ese diario será bloqueado.

**Odoo Version:** 16.0

Features
========

- Permite marcar diarios para impedir la impresión de facturas asociadas.
- La restricción aplica a todos los reportes PDF de facturas, independientemente del botón o menú utilizado.
- Mensaje de error claro para el usuario cuando intenta imprimir una factura restringida.
- Integración compatible con el motor de informes estándar de Odoo.

Usage
=====

1. Instala el módulo desde Apps.
2. Ve al menú **Contabilidad > Configuración > Diarios**.
3. Abre el diario donde quieras aplicar la restricción.
4. Activa la casilla **Restringir impresión de factura**.
5. Al intentar imprimir una factura registrada en ese diario, se bloqueará la acción y aparecerá un mensaje de error.

.. image:: ./static/description/diario.png
   :alt: Diario con restricción

.. image:: ./static/description/error.png
   :alt: Mensaje de error al imprimir

Configuración
=============

No requiere configuración adicional.

Soporte
=======

Si tienes problemas o necesitas soporte, crea un issue en el repositorio del módulo o contacta al autor.

Credits
=======

Authors
-------

* Pedro Jabie

Contributors
------------

* Pedro Jabie <pjabie@gauchocode.com>

Maintainers
===========

.. image:: https://img.shields.io/badge/contact-pedro.jabie%40gmail.com-blue.svg
   :target: mailto:pjabie@gauchocode.com

This module is maintained by Pedro Jabie.

License
=======

LGPL-3.0

