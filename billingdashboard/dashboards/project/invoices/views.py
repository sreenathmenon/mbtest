from django.views import generic

from django.core.urlresolvers import reverse
from django.core.urlresolvers import reverse_lazy
from django.utils.translation import ugettext_lazy as _

from horizon import exceptions
from horizon import forms
from horizon import tabs
from horizon import tables

from billingdashboard.common import get_user_invoices

from billingdashboard.dashboards.project.invoices \
    import tables as invoice_table
    
    
class IndexView(generic.TemplateView):
    table_class = invoice_table.UserInvoiceListingTable
    template_name = 'project/invoices/index.html'
    page_title = _("Invoices")

    def get_data(self):
           return get_user_invoices(user_id = '', verbose=True)

class UserInvoiceDetailsView(generic.TemplateView):
    template_name  = 'project/invoices/invoice.html'
    
    def get_context_data(self, **kwargs):
        context = super(UserInvoiceDetailsView, self).get_context_data(**kwargs)
        id = self.kwargs['id']
        context['invoice'] = get_plan(id, verbose=True)
        return context


