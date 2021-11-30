from django.http import HttpResponse
from xadmin.plugins.actions import BaseActionView


class ClearAction(BaseActionView):
    """清空action"""
    action_name = 'clear_score'
    description = u'清空成绩%(verbose_name_plural)s'
    model_perm = 'change'
    icon = 'fa fa-bug'

    def do_action(self, queryset):
        for obj in queryset:
            obj.score = '0'
            obj.save()
        return None

