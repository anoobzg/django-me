from django.db import models


class Printer(models.Model):
    """3D打印机模型"""
    name = models.CharField(max_length=100, verbose_name='打印机名称')
    ip_address = models.CharField(max_length=15, verbose_name='IP地址')
    port = models.IntegerField(default=7125, verbose_name='端口')
    model = models.CharField(max_length=100, blank=True, verbose_name='型号')
    description = models.TextField(blank=True, verbose_name='描述')
    is_active = models.BooleanField(default=True, verbose_name='是否激活')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name = '打印机'
        verbose_name_plural = '打印机'
        ordering = ['-created_at']

    def __str__(self):
        return self.name


class PrintJob(models.Model):
    """打印任务模型"""
    STATUS_CHOICES = [
        ('pending', '等待中'),
        ('printing', '打印中'),
        ('completed', '已完成'),
        ('failed', '失败'),
        ('cancelled', '已取消'),
    ]
    
    printer = models.ForeignKey(Printer, on_delete=models.CASCADE, verbose_name='打印机')
    filename = models.CharField(max_length=255, verbose_name='文件名')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name='状态')
    progress = models.FloatField(default=0.0, verbose_name='进度')
    started_at = models.DateTimeField(null=True, blank=True, verbose_name='开始时间')
    completed_at = models.DateTimeField(null=True, blank=True, verbose_name='完成时间')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = '打印任务'
        verbose_name_plural = '打印任务'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.printer.name} - {self.filename}"

