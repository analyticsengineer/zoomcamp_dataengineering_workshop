FROM python:3.13.11-slim
# COPY --from=ghrc.io/astral-sh/uv:latest /usr/local/bin/uv /bin/uv


WORKDIR /code
RUN pip install uv --no-cache-dir uv
ENV PATH="/code/.venv/bin:$PATH"

COPY pyproject.toml .python-version uv.lock ./


COPY pipeline.py .

ENTRYPOINT ["python", "pipeline.py"]