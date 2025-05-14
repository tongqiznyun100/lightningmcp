import time


class MetricsCollector:
    def __init__(self):
        self._metrics = {}

    def record(self, name, value):
        """Record a single metric value."""
        if name not in self._metrics:
            self._metrics[name] = []
        self._metrics[name].append(value)

    def increment_counter(self, name, value=1):
        """Increment a counter metric."""
        if name not in self._metrics:
            self._metrics[name] = 0
        self._metrics[name] += value

    def observe_duration(self, name, start_time):
        """Record the duration of an operation."""
        duration = time.time() - start_time
        self.record(name, duration)

    def get_metrics(self):
        """Retrieve all collected metrics."""
        # In a real system, this would format metrics for a monitoring system (e.g., Prometheus)
        return self._metrics

    def reset_metrics(self):
        """Reset all collected metrics (useful for testing)."""
        self._metrics = {}
