from fastapi import APIRouter, HTTPException

from app.config.celery import fetch_data_and_save_id_data

router_task = APIRouter(prefix="/api/v1")


@router_task.post("/task")
async def create_task(ip: str):
    result = fetch_data_and_save_id_data.delay(ip)
    return {"task_id": result.id}


@router_task.get("/status/{task_id}")
async def get_task_status(task_id: str):
    result = fetch_data_and_save_id_data.AsyncResult(task_id)
    if result.state == "PENDING":
        return {"status": "Task is pending"}
    elif result.state == "SUCCESS":
        return {"status": "Task is completed successfully"}
    elif result.state == "FAILURE":
        return {"status": "Task has failed"}
    else:
        return {"status": "Task status is unknown"}
