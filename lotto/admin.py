from django.contrib import admin
from .models import Gacha,Ticket
import random




def num_gacha (modeladmin, request, queryset):
    for gacha in queryset:
        gacha_nums = random.sample(range(1,46),7)
        winning_nums = sorted(gacha_nums[:6])
        bonus_num = gacha_nums[6]

        gacha.winning_nums = winning_nums
        gacha.bonus_num = bonus_num
        gacha.save()

        tickets = Ticket.objects.filter(draw=gacha)
        for ticket in tickets:
            match_count = len(set(ticket.nums) & set(winning_nums))

            if match_count == 6:
                ticket.rank = 1
            elif match_count == 5 and bonus_num in ticket.nums:
                ticket.rank = 2
            elif match_count == 5:
                ticket.rank = 3
            elif match_count == 4:
                ticket.rank = 4
            elif match_count == 3:
                ticket.rank = 5
            else:
                ticket.rank = 0
            
            ticket.save()
            
    modeladmin.message_user(request, "추첨계산 완료.")
num_gacha.short_description = "선택한 회차 추첨하기"
    

class GachaAdmin(admin.ModelAdmin):
    list_display = ('id','winning_nums', 'bonus_num')
    actions =[num_gacha]

class TicketAdmin(admin.ModelAdmin):
    list_display = ('draw', 'nums', 'is_auto', 'rank')
    list_filter = ('draw', 'rank', 'is_auto')


admin.site.register(Gacha, GachaAdmin)
admin.site.register(Ticket, TicketAdmin)

# Register your models here.
