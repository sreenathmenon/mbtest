#
# Copyright 2017 NephoScale
#

from django.utils.translation import ugettext_lazy as _
from horizon import tables

class UsageBasedPlansTable(tables.DataTable):
    id       = tables.Column('id', verbose_name=_('Id'))
    name     = tables.Column('name', verbose_name=_('Name'), \
        link="horizon:project:customer_plans:user_plan_details")
    date     = tables.Column('created_on', verbose_name=_('Start Date'))
    status   = tables.Column('status', verbose_name=_('Status'))
    contract = tables.Column('contract_period', verbose_name=_('Contract Period'))
    
    def get_object_id(self, datum):
        return datum['id']

    class Meta(object):
        name = "usage_based_plans"
        verbose_name = _("Usage Based Plans")
        row_actions = ()
        table_actions = () 
