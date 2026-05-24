from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Gacha, Ticket
import random


def buy_ticket(request):
    open_gachas = Gacha.objects.filter(winning_nums__isnull=True)

    if request.method == 'POST':
        gacha_id = request.POST.get('gacha_id')
        mode = request.POST.get('mode')
        gacha = Gacha.objects.get(id=gacha_id)

        if mode == 'auto':
            nums = sorted(random.sample(range(1, 46), 6))
            is_auto = True
        else:
            nums = sorted([int(request.POST.get(f'n{i}')) for i in range(1, 7)])
            is_auto = False

        ticket = Ticket.objects.create(draw=gacha, nums=nums, is_auto=is_auto)

        if 'tickets' not in request.session:
            request.session['tickets'] = []
        request.session['tickets'].append(ticket.id)
        request.session.modified = True

        messages.success(request, f'구매 완료! 번호: {nums}')
        return redirect('my_tickets')

    return render(request, 'lotto/buy_ticket.html', {'open_gachas': open_gachas})


def my_tickets(request):
    ticket_ids = request.session.get('tickets', [])
    tickets = Ticket.objects.filter(id__in=ticket_ids).order_by('-id')
    return render(request, 'lotto/my_tickets.html', {'tickets': tickets})