def route_task(task_type):
    targets = {'coding': 'OpenCode', 'analysis': 'Unbound', 'system': 'Daemon'}
    return targets.get(task_type, 'Default')
