from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Printer, PrintJob


def printer_list(request):
    """打印机列表视图"""
    printers = Printer.objects.filter(is_active=True)
    data = [{
        'id': p.id,
        'name': p.name,
        'ip_address': p.ip_address,
        'port': p.port,
        'model': p.model,
        'description': p.description,
    } for p in printers]
    return JsonResponse({'printers': data})


def printer_detail(request, printer_id):
    """打印机详情视图"""
    try:
        printer = Printer.objects.get(id=printer_id, is_active=True)
        data = {
            'id': printer.id,
            'name': printer.name,
            'ip_address': printer.ip_address,
            'port': printer.port,
            'model': printer.model,
            'description': printer.description,
        }
        return JsonResponse(data)
    except Printer.DoesNotExist:
        return JsonResponse({'error': '打印机不存在'}, status=404)


@csrf_exempt
def print_job_list(request):
    """打印任务列表视图"""
    printer_id = request.GET.get('printer_id')
    if printer_id:
        jobs = PrintJob.objects.filter(printer_id=printer_id)
    else:
        jobs = PrintJob.objects.all()
    
    data = [{
        'id': j.id,
        'printer': j.printer.name,
        'filename': j.filename,
        'status': j.status,
        'progress': j.progress,
        'created_at': j.created_at.isoformat(),
        'started_at': j.started_at.isoformat() if j.started_at else None,
        'completed_at': j.completed_at.isoformat() if j.completed_at else None,
    } for j in jobs]
    return JsonResponse({'jobs': data})

