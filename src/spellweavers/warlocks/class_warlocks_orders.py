from spellweavers.default.class_default_orders import DefaultOrder, DefaultOrders


class WarlocksOrder(DefaultOrder):
    """Thin Warlocks wrapper over Default Order."""


class WarlocksOrders(DefaultOrders):
    """Thin Warlocks wrapper over Default Orders."""

    order_class = WarlocksOrder
