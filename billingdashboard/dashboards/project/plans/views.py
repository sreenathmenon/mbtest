from django.views import generic

from django.core.urlresolvers import reverse
from django.core.urlresolvers import reverse_lazy
from django.utils.translation import ugettext_lazy as _

from horizon import exceptions
from horizon import forms
from horizon import tabs
from horizon import tables

from billingdashboard.common import get_user_plans
from astutedashboard.common import get_plan

from billingdashboard.dashboards.project.plans \
    import tables as plan_tables
    
    
class IndexView(tables.DataTableView):
    table_class = plan_tables.UsageBasedPlansTable
    template_name = 'project/plans/index.html'
    page_title = _("Subscribed Plans")

    def get_data(self):
                print "abbbbc"
                user_id = self.request
                print user_id.__dict__
                return get_user_plans(user_id ='dgdfgdfg234ad', verbose=True)

class UserPlanDetailsView(generic.TemplateView):
    template_name  = 'project/plans/plan.html'
    
    def get_context_data(self, **kwargs):
        context = super(UserPlanDetailsView, self).get_context_data(**kwargs)
        id = self.kwargs['id']
        context['plan_details'] = get_plan(id, verbose=True)
        return context

