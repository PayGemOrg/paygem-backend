def user_metrics_helper(metrics):
    """Helper function to format user metrics"""
    return {
        "total_subscriptions": metrics[0],
        "active_subscriptions": metrics[1],
        "total_spent": metrics[2],
        "monthly_spent": metrics[3],
    }