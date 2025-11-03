from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import time

# Moonraker API 模拟视图

@csrf_exempt
def server_info(request):
    """模拟 Moonraker 服务器信息接口"""
    data = {
        "result": {
            "klippy_connected": True,
            "klippy_state": "ready",
            "components": [
                "klippy",
                "klippy_connection",
                "file_manager",
                "machine",
                "data_store",
                "shell_command",
                "update_manager",
                "power",
                "webcam",
                "history"
            ],
            "failed_components": [],
            "registered_directories": ["config", "logs", "gcodes", "config_examples"],
            "warnings": [],
            "websocket_count": 0,
            "moonraker_version": "0.8.0-124-g1234567"
        }
    }
    return JsonResponse(data)


@csrf_exempt
def printer_info(request):
    """模拟打印机信息接口"""
    data = {
        "result": {
            "state": "ready",
            "state_message": "Printer is ready",
            "hostname": "test-printer",
            "software_version": "v0.12.0-123-g4567890",
            "cpu_info": "4 core ARM processor",
            "klipper_path": "/home/pi/klipper",
            "python_path": "/usr/bin/python3",
            "log_file": "/tmp/klippy.log",
            "config_file": "/home/pi/printer.cfg"
        }
    }
    return JsonResponse(data)


@csrf_exempt
def printer_objects_query(request):
    """模拟查询打印机对象状态接口"""
    if request.method == 'POST':
        try:
            body = json.loads(request.body)
            objects = body.get('objects', {})
        except:
            objects = {}
    else:
        objects = request.GET.get('objects', '')
        if isinstance(objects, str):
            # 处理查询字符串格式：?objects=tool0,tool1,heater_bed
            objects = {obj: None for obj in objects.split(',') if obj}
    
    # 模拟对象状态
    result = {}
    current_time = time.time()
    
    # 默认查询的对象
    default_objects = [
        "tool0",
        "heater_bed",
        "extruder",
        "motion_report",
        "print_stats",
        "display_status",
        "virtual_sdcard",
        "fan",
        "idle_timeout"
    ]
    
    query_objects = list(objects.keys()) if objects else default_objects
    
    for obj_name in query_objects:
        if 'tool' in obj_name or 'extruder' in obj_name:
            result[obj_name] = {
                "temperature": 25.0,
                "target": 0.0,
                "power": 0.0,
                "pressure_advance": 0.0,
                "smooth_time": 0.04,
                "control": "pid",
                "pid_Kp": 22.2,
                "pid_Ki": 1.08,
                "pid_Kd": 114.0
            }
        elif 'heater_bed' in obj_name or 'bed' in obj_name:
            result[obj_name] = {
                "temperature": 25.0,
                "target": 0.0,
                "power": 0.0
            }
        elif 'motion_report' in obj_name:
            result[obj_name] = {
                "live_position": [0.0, 0.0, 0.0, 0.0],
                "live_velocity": 0.0,
                "live_extruder_velocity": 0.0,
                "steppers": {
                    "x": {"position": 0.0, "velocity": 0.0},
                    "y": {"position": 0.0, "velocity": 0.0},
                    "z": {"position": 0.0, "velocity": 0.0}
                }
            }
        elif 'print_stats' in obj_name:
            result[obj_name] = {
                "filename": "",
                "total_duration": 0.0,
                "print_duration": 0.0,
                "filament_used": 0.0,
                "state": "standby",
                "message": ""
            }
        elif 'display_status' in obj_name:
            result[obj_name] = {
                "progress": 0.0,
                "message": ""
            }
        elif 'virtual_sdcard' in obj_name:
            result[obj_name] = {
                "is_active": False,
                "file_position": 0,
                "file_path": ""
            }
        elif 'fan' in obj_name:
            result[obj_name] = {
                "speed": 0.0,
                "rpm": 0.0
            }
        else:
            result[obj_name] = {}
    
    response_data = {
        "result": {
            "status": result,
            "eventtime": current_time
        }
    }
    
    return JsonResponse(response_data)


@csrf_exempt
def printer_objects_list(request):
    """模拟列出所有可用打印机对象接口"""
    data = {
        "result": {
            "objects": [
                "configfile",
                "gcode_macro pause",
                "gcode_macro resume",
                "gcode_macro cancel_print",
                "mcu",
                "mcu arduino",
                "printer",
                "virtual_sdcard",
                "print_stats",
                "display_status",
                "query_endstops",
                "idle_timeout",
                "motion_report",
                "tool0",
                "heater_bed",
                "fan",
                "stepper_x",
                "stepper_y",
                "stepper_z"
            ]
        }
    }
    return JsonResponse(data)


@csrf_exempt
def printer_status(request):
    """模拟打印机完整状态接口"""
    current_time = time.time()
    data = {
        "result": {
            "status": {
                "tool0": {
                    "temperature": 25.0,
                    "target": 0.0,
                    "power": 0.0,
                    "pressure_advance": 0.0
                },
                "heater_bed": {
                    "temperature": 25.0,
                    "target": 0.0,
                    "power": 0.0
                },
                "motion_report": {
                    "live_position": [0.0, 0.0, 0.0, 0.0],
                    "live_velocity": 0.0
                },
                "print_stats": {
                    "filename": "",
                    "total_duration": 0.0,
                    "print_duration": 0.0,
                    "filament_used": 0.0,
                    "state": "standby",
                    "message": ""
                },
                "display_status": {
                    "progress": 0.0,
                    "message": ""
                },
                "virtual_sdcard": {
                    "is_active": False,
                    "file_position": 0,
                    "file_path": ""
                },
                "fan": {
                    "speed": 0.0
                }
            },
            "eventtime": current_time
        }
    }
    return JsonResponse(data)
