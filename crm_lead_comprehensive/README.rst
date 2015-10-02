.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

===================
Comprehensive leads
===================

This module was written to extend the functionality of leads to support having
a lot more of information there and allow you to transfer it automatically to a
new partner.

Installation
============

If you want to transfer the lead's new trade name field to the partner, you
should install module ``l10n_es_partner``. It's not required by default because
it makes many things that you may not need.

Usage
=====

To use this module, you need to:

* Open any lead.
* Go to *Extra info*.
* Below, use the new *Company information* area.

To transfer that information automatically to a newly created partner:

* Open any lead.
* Press *Convert to opportunity* above.
* Select *Conversion action: Convert to opportunity*.
* Select *Related customer: Create a new customer*.
* Press *Create Opportunity*.

The logic that will follow is:

* If you unchecked the option *Use same adress for billing*, use that address
  information for the company and set it as invoice address.
* If there is any field that exists in the *Company information* area, use it
  when creating the company.
* For other information, use the same as what exists in the upper side of the
  lead.

.. image:: https://odoo-community.org/website/image/ir.attachment/5784_f2813bd/datas
   :alt: Try me on Runbot
   :target: https://runbot.odoo-community.org/runbot/{repo_id}/{branch}

.. repo_id is available in https://github.com/OCA/maintainer-tools/blob/master/tools/repos_with_ids.txt
.. branch is "8.0" for example

For further information, please visit:

* https://www.odoo.com/forum/help-1

Known issues / Roadmap
======================

* Add tests.

Bug Tracker
===========

Bugs are tracked on `GitHub Issues <https://github.com/OCA/ crm/issues>`_. In
case of trouble, please check there if your issue has already been reported. If
you spotted it first, help us smashing it by providing a detailed and welcomed
feedback `here <https://github.com/OCA/ crm/issues/new?body=module:%20
crm_lead_comprehensive%0Aversion:%20
8.0.1.0.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.


Credits
=======

Contributors
------------

* Rafael Blasco <rafaelbn@antiun.com>
* Jairo Llopis <yajo.sk8@gmail.com>

Maintainer
----------

.. image:: https://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: https://odoo-community.org

This module is maintained by the OCA.

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

To contribute to this module, please visit http://odoo-community.org.
