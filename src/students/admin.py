from django.contrib import admin

from students.models import Student, Group


class StudentAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('id', 'first_name', 'last_name', 'age')
    fields = ('first_name', 'last_name', 'age')
    readonly_fields = ('age', )
    # list_filter = ['age']

    def get_queryset(self, request):
        queryset = super().get_queryset(request)

        if not request.user.is_superuser:
            queryset = queryset.filter(age__gte=18)

        return queryset


class GroupAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'head']
    list_select_related = ['head']

    # def get_queryset(self, request):
    #     return super().get_queryset(request).select_related('head')


admin.site.register(Student, StudentAdmin)
admin.site.register(Group, GroupAdmin)
