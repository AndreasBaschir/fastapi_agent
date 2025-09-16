from collections import defaultdict
from fastapi import FastAPI, Request, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse
from time import time

class RateLimiterMiddleware(BaseHTTPMiddleware):
    def __init__(self, app: FastAPI, max_requests: int, window_seconds: int):
        super().__init__(app)
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self.clients = defaultdict(list)

    async def dispatch(self, request: Request, call_next):
        client_ip = request.client.host
        current_time = time()

        # Clean up old requests
        self.clients[client_ip] = [
            timestamp for timestamp in self.clients[client_ip]
            if current_time - timestamp < self.window_seconds
        ]

        # Check if the client exceeds the rate limit
        if len(self.clients[client_ip]) >= self.max_requests:
            return JSONResponse(
                status_code=429,
                content={"detail": "Too many requests"}
            )

        # Record the current request
        self.clients[client_ip].append(current_time)

        return await call_next(request)