from django.shortcuts import render
from django.http import HttpResponse
import random
import requests
# Create your views here.

def payment(payment_id, action, txid=""):
    header = {
        'Authorization': "wesl53dt8qyekg1qm8gaiurrrjurx5h1qjspqcih2qlwjhkpu78tii6nd6cyp6z6"
    }
    approveurl = f"https://api.minepi.com/v2/payments/{payment_id}/{action}"
    data = {'txid': txid} if txid else {}
    response = requests.post(approveurl, headers=header, data=data)

    if response.status_code == 200:
        res = f"Payment {action} request sent successfully"
    else:
        res = f"Failed to send payment {action} request. Status code: {response.status_code}"
        print(response.content)
    return res

def home(request):
    payment_code = round(random.random(), 7)
    return render(request, 'index.html', {'amount': payment_code})

def key(request):
    return render(request, 'validation-key.txt')

def action_payment(request, action, payment_id):
    header = {
        'Authorization': "Key wesl53dt8qyekg1qm8gaiurrrjurx5h1qjspqcih2qlwjhkpu78tii6nd6cyp6z6"
    }
    approveurl = f"https://api.minepi.com/v2/payments/{payment_id}/{action}"
    response = requests.post(approveurl, headers=header)

    if response.status_code == 200:
        res = f"Payment {action} request sent successfully."
    else:
        res = (
            f"Failed to send payment {action} request. "
            f"Status code: {response.status_code}, Error: {response.content.decode()}"
        )
    return HttpResponse(res)

def complete_payment(request, payment_id, txid):
    header = {
        'Authorization': "Key wesl53dt8qyekg1qm8gaiurrrjurx5h1qjspqcih2qlwjhkpu78tii6nd6cyp6z6"
    }
    approveurl = f"https://api.minepi.com/v2/payments/{payment_id}/complete"
    data = {'txid': txid}
    response = requests.post(approveurl, headers=header, data=data)

    if response.status_code == 200:
        res = "Payment completion request sent successfully."
    else:
        res = (
            f"Failed to complete payment request. "
            f"Status code: {response.status_code}, Error: {response.content.decode()}"
        )
    return HttpResponse(res)
