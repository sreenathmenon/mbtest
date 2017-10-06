import requests as request
from openstack_dashboard.local.local_settings import \
        ASTUTE_BASE_URL

from astutedashboard.common import get_plan

def get_user_plans(user_id, verbose=False):
        response = request.get(ASTUTE_BASE_URL + 'plan/mapping/user?id=' + str(user_id))
        data = response.json()
        print data
        for item in data:
            plan_id      = item['plan_id']
            plan_details = get_plan(plan_id)
            plan_name    = plan_details.get('name')
            item['name'] = plan_name
        return data

def get_user_invoices(user_id, verbose=False):
        response = request.get(ASTUTE_BASE_URL + 'invoice?user=' + str(user_id))
        data = response.json()
        print "%%%%%%%%%%%%%%%%%%%%%%%%%%"
        print data
        return data
    
