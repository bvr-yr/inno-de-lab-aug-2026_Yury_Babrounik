import json

system_telemetry = [
    ("srv_01", 12.5, 64, "online"),
    ("srv_02", 85.0, 92, "online"),
    ("srv_03", 0.0, 0, "offline"),
    ("srv_04", 45.2, 78, "online"),
    ("srv_05", 95.1, 99, "online"),
]

# lists to hold extracted values
active_nodes = []
values_ram = []
values_cpu = []

for node_name, cpu_load, ram_usage, status in system_telemetry:
    if status != "offline":
        active_nodes.append(node_name)
        values_ram.append(ram_usage)
        values_cpu.append(cpu_load)

active_nodes_count = len(active_nodes)

# separate object might be not neccessary
# it is just simplier to read and maintain
metrics = {
    # since we are interested only in active nodes, use existing active_nodes_count
    # otherwise use len(values_cpu) instead
    "average_cpu": round(sum(values_cpu) / active_nodes_count, 2),
    "max_ram": max(values_ram),
}

summary = {
    "active_nodes_count": active_nodes_count,
    "metrics": metrics,
}

print(f"Active nodes: {active_nodes}")

# builtin 'pprint' module has limited formatting options
# use json to pretty-print summary structure
print(f"Telemetry summary:\n{json.dumps(summary, indent=4)}")
