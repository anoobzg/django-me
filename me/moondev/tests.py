from django.test import TestCase
from .models import Printer, PrintJob


class PrinterModelTest(TestCase):
    def test_printer_creation(self):
        """测试打印机创建"""
        printer = Printer.objects.create(
            name='Test Printer',
            ip_address='192.168.1.100',
            port=7125
        )
        self.assertEqual(str(printer), 'Test Printer')
        self.assertEqual(printer.is_active, True)


class PrintJobModelTest(TestCase):
    def test_print_job_creation(self):
        """测试打印任务创建"""
        printer = Printer.objects.create(
            name='Test Printer',
            ip_address='192.168.1.100'
        )
        job = PrintJob.objects.create(
            printer=printer,
            filename='test.gcode',
            status='pending'
        )
        self.assertEqual(str(job), 'Test Printer - test.gcode')
        self.assertEqual(job.progress, 0.0)

