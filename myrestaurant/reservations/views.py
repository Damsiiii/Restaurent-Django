from django.shortcuts import render, redirect, get_object_or_404
from .forms import ReservationForm
from .models import Reservation
import qrcode
from io import BytesIO
import base64

def home_view(request):
    return render(request, 'reservations/home.html')

def menu_view(request):
    return render(request, 'reservations/menu.html')

def booking_view(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save()

            # Generate QR linked to this reservation
            url = request.build_absolute_uri(f"/booking/{reservation.id}/")
            qr = qrcode.make(url)
            buffer = BytesIO()
            qr.save(buffer, format="PNG")
            img_b64 = base64.b64encode(buffer.getvalue()).decode()

            return render(request, 'reservations/booking_success.html', {
                'reservation': reservation,
                'qr_code': img_b64
            })
    else:
        form = ReservationForm()

    return render(request, 'reservations/booking.html', {'form': form})

def contact_view(request):
    return render(request, 'reservations/contact.html')

def qr_code_view(request):
    booking_url = request.build_absolute_uri('/booking/')
    qr = qrcode.make(booking_url)
    buffer = BytesIO()
    qr.save(buffer, format="PNG")
    qr_data = base64.b64encode(buffer.getvalue()).decode()
    return render(request, 'reservations/qr.html', {'qr_code': qr_data})

def booking_detail_view(request, res_id):
    reservation = get_object_or_404(Reservation, id=res_id)
    return render(request, 'reservations/booking_detail.html', {'reservation': reservation})