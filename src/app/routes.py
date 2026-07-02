from datetime import datetime, UTC
import os
import platform

import psutil
from fastapi import APIRouter

router = APIRouter()


def _timestamp() -> str:
    return datetime.now(UTC).isoformat().replace("+00:00", "Z")


def health():
    return {
        "status": "ok",
        "version": "0.1.0",
        "timestamp": _timestamp(),
    }


@router.get("/health")
def health_route():
    return health()


@router.get("/cpu")
def cpu():
    return {"percent": psutil.cpu_percent(interval=0.1)}


@router.get("/memory")
def memory():
    memory_stats = psutil.virtual_memory()
    return {
        "total": memory_stats.total,
        "available": memory_stats.available,
        "used": memory_stats.used,
        "percent": memory_stats.percent,
    }


@router.get("/disk")
def disk():
    disk_stats = psutil.disk_usage("/")
    return {
        "total": disk_stats.total,
        "free": disk_stats.free,
        "used": disk_stats.used,
        "percent": disk_stats.percent,
    }


@router.get("/environment")
def environment():
    return {
        "python_version": platform.python_version(),
        "platform": platform.platform(),
        "deployment_environment": os.getenv("DEPLOYMENT_ENV", "local"),
    }


@router.get("/system")
def system():
    memory = psutil.virtual_memory()
    return {
        "platform": platform.platform(),
        "boot_time": datetime.fromtimestamp(psutil.boot_time()).isoformat(),
        "hostname": platform.node(),
        "cpu_count": psutil.cpu_count(logical=True),
        "cpu_percent": psutil.cpu_percent(interval=0.1),
        "memory_total": memory.total,
        "memory_used": memory.used,
        "memory_percent": memory.percent,
    }


@router.get("/network")
def network():
    counters = psutil.net_io_counters()
    return {
        "bytes_sent": counters.bytes_sent,
        "bytes_received": counters.bytes_recv,
        "packets_sent": counters.packets_sent,
        "packets_received": counters.packets_recv,
    }


@router.get("/machines")
def machines():
    return [
        {
            "machine_id": "MCH-1001",
            "status": "running",
            "temperature_c": 72.5,
            "utilization_percent": 83,
        },
        {
            "machine_id": "MCH-1002",
            "status": "idle",
            "temperature_c": 68.2,
            "utilization_percent": 12,
        },
        {
            "machine_id": "MCH-1003",
            "status": "maintenance",
            "temperature_c": 75.8,
            "utilization_percent": 0,
        },
    ]


@router.get("/sensors")
def sensors():
    return [
        {
            "sensor_name": "pressure_1",
            "reading": 34.2,
            "timestamp": _timestamp(),
        },
        {
            "sensor_name": "temperature_2",
            "reading": 68.9,
            "timestamp": _timestamp(),
        },
        {
            "sensor_name": "vibration_3",
            "reading": 0.013,
            "timestamp": _timestamp(),
        },
    ]
