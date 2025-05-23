=================================================
Pricelist Price List
=================================================

.. image:: https://img.shields.io/badge/license-AGPL--3-blue.png
   :target: https://www.gnu.org/licenses/agpl
   :alt: License: AGPL-3

.. image:: https://img.shields.io/badge/GitLab-Repositorio-orange?logo=gitlab
   :target: https://gitlab.com/broobe/odoo/gc-odoo-ramos-addons
   :alt: Repositorio en GitLab

Este módulo permite visualizar en una única vista todos los precios de todos los productos en todas las tarifas definidas.

Características principales:
----------------------------

- Genera automáticamente un reporte que cruza cada producto con cada tarifa.
- Permite consultar, filtrar y agrupar la información de precios por producto o por tarifa.
- Integra reglas de acceso para que los usuarios solo vean las tarifas asignadas a ellos (requiere el módulo `tarif_restriction_by_user`).
- Incluye acciones y menús para generar o regenerar el reporte cuando sea necesario.

Uso
----

1. Navegar a **Ventas > Productos > Reporte de Precios por Tarifa**.
2. Si el reporte aún no ha sido generado, se generará automáticamente.
3. Si se desea regenerar, usar la opción **Regenerar Reporte de Precios** desde el mismo menú.

El modelo `product.pricelist.report` es un modelo técnico que almacena registros calculados, sin edición manual, con los precios obtenidos vía la lógica del método `_get_products_price()` de las tarifas.

Créditos
--------

Desarrollado por:
~~~~~~~~~~~~~~~~~

* Gauchocode

Contribuidores:
~~~~~~~~~~~~~~~

* Pedro Esteban Jabie <pedro@broobe.com>

Mantenedor:
~~~~~~~~~~~

Este módulo es mantenido por Gauchocode. 

Licencia
--------

GPL-3

Dependencias
------------

- `stock`
- `tarif_restriction_by_user`

Instalación
-----------

Este módulo debe instalarse como cualquier otro módulo de Odoo. Asegúrese de tener instaladas las dependencias necesarias.

